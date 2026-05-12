"""
Script de integración biométrica + chatbot.

Este bloque de imports está organizado por responsabilidad para que sea más
fácil entender qué aporta cada librería al flujo del programa.
"""

# =========================
# Librerías estándar de Python
# =========================
import sys
# sys: permite terminar el programa de forma controlada con sys.exit()
# cuando falla la inicialización crítica del chatbot.

import csv
# csv: se usa para exportar eventos y logs de asistencia del dispositivo
# a archivos .csv que luego se pueden abrir en Excel o analizar en pandas.

import time
# time: aporta pausas en bucles de monitoreo (time.sleep) para no saturar
# al dispositivo ni consumir CPU innecesariamente.

import traceback
import socket
import threading
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
# traceback: captura la traza completa de excepciones para guardarla en
# archivos de error durante el monitoreo continuo.

from datetime import datetime
# datetime: genera marcas de tiempo para nombres de archivos/sesiones y
# para registrar cuándo ocurrió cada evento o error.

from pathlib import Path
# Path (pathlib): manejo robusto y multiplataforma de rutas/archivos.
# Evita concatenaciones manuales de strings para rutas.


# =========================
# Librerías de terceros (pip)
# =========================
import chatterbot_corpus
# chatterbot_corpus: contiene datasets de entrenamiento predefinidos.
# Aquí se usa el corpus en español para entrenar respuestas del ChatBot.

from chatterbot import ChatBot, languages
# ChatBot: clase principal para crear el bot conversacional.
# languages: catálogo de idiomas; se usa languages.SPA para español.

from chatterbot.trainers import ChatterBotCorpusTrainer
# ChatterBotCorpusTrainer: entrena el bot con corpus de texto
# estructurado (preguntas/respuestas).

from zk import ZK
# ZK (pyzk): cliente para conectar con dispositivos ZKTeco por TCP/IP
# (por ejemplo MB360), leer usuarios y logs, y ejecutar operaciones básicas.

import cv2
# cv2 (OpenCV): acceso a la cámara local, captura de frames y guardado
# de imágenes durante registro de rostro o monitoreo opcional con fotos.

import face_recognition
# face_recognition: detección/codificación facial y comparación de rostros
# para validar si una cara en cámara coincide con la referencia conocida.

# =========================
# Configuración del dispositivo ZKTeco
# =========================
DEVICE_MODEL = "MB360"
ZKTECO_IP = "192.168.80.202"
ZKTECO_PORT = 4370
ZKTECO_PASSWORD = 23  # o la Comm Key real del reloj
EXPORT_DIR = Path(__file__).resolve().parent / "exports"
MONITOR_STOP_EVENT = threading.Event()


def obtener_host_zkteco():
    """Normaliza y valida el host configurado para evitar errores de resolución."""
    host = str(ZKTECO_IP).strip()
    if not host:
        raise ValueError("ZKTECO_IP está vacío. Configura una IP o hostname válido.")
    return host


def diagnostico_red_previo(host, port):
    """Prueba resolución DNS/IP y conectividad TCP antes de usar pyzk."""
    try:
        socket.getaddrinfo(host, port)
    except socket.gaierror as e:
        print("Error de resolución de host/IP (getaddrinfo).")
        print(f"Host configurado: '{host}'")
        print("Revisa que la IP no tenga espacios y tenga formato correcto, por ejemplo: 192.168.80.201")
        print(f"Detalle técnico: {e}")
        return False

    try:
        with socket.create_connection((host, port), timeout=3):
            return True
    except OSError as e:
        print("No se pudo abrir conexión TCP con el dispositivo.")
        print(f"Host: {host} | Puerto: {port}")
        print("Verifica red local, puerta de enlace, firewall y que el puerto 4370 esté habilitado en el reloj.")
        print(f"Detalle técnico: {e}")
        return False

# =========================
# Inicializar ChatBot
# =========================
try:
    chatbot = ChatBot("MiBot", tagger_language=languages.SPA)
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train(str(Path(chatterbot_corpus.__file__).parent / "data" / "spanish"))
except Exception as e:
    print("ChatBot error:", e)
    print("Instala el modelo de spaCy en español con:")
    print("C:/Users/julia/AppData/Local/Programs/Python/Python310/python.exe -m spacy download es_core_news_sm")
    sys.exit(1)
# =========================
# Registrar nuevo usuario en ZKTeco
# =========================
def registrar_usuario(nombre, user_id="1234", role=0):
    host = obtener_host_zkteco()
    if not diagnostico_red_previo(host, ZKTECO_PORT):
        return

    zk = ZK(host, port=ZKTECO_PORT, timeout=5, password=ZKTECO_PASSWORD)
    try:
        conn = zk.connect()
        conn.disable_device()

        # Registrar usuario (sin huella)
        conn.set_user(uid=int(user_id), name=nombre, privilege=role, password='', group_id='', user_id=user_id)
        print(f"Usuario {nombre} (ID: {user_id}) registrado exitosamente.")
        print(f"En {DEVICE_MODEL}, la huella se registra directamente en el reloj (no desde Python).")
        conn.enable_device()
        conn.disconnect()
    except Exception as e:
        print(f"Error registrando usuario: {e}")

# =========================
# Registrar rostro con la cámara
# =========================
def registrar_rostro(nombre_archivo="persona_conocida.jpg"):
    ruta_rostro = Path(__file__).resolve().parent / nombre_archivo
    cam = cv2.VideoCapture(0)
    print("Coloca tu rostro frente a la cámara y presiona 's' para capturar.")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Registrar Rostro", frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite(str(ruta_rostro), frame)
            print(f"Rostro capturado y guardado como '{ruta_rostro}'")
            break

        elif cv2.waitKey(1) & 0xFF == ord('q'):
            print("Registro cancelado.")
            break

    cam.release()
    cv2.destroyAllWindows()

# =========================
# Verificación con ZKTeco MB360 (huella registrada)
# =========================
def verificar_huella_con_zkteco():
    host = obtener_host_zkteco()
    if not diagnostico_red_previo(host, ZKTECO_PORT):
        return False

    zk = ZK(host, port=ZKTECO_PORT, timeout=5, password=ZKTECO_PASSWORD)
    try:
        print("Conectando al dispositivo ZKTeco...")
        conn = zk.connect()
        conn.disable_device()

        users = conn.get_users()
        if users:
            print("Usuarios encontrados en el dispositivo:")
            for user in users:
                print(f" - ID: {user.user_id}, Nombre: {user.name}")
            conn.enable_device()
            conn.disconnect()
            return True
        else:
            print("No hay usuarios registrados en el dispositivo.")
            conn.disconnect()
            return False

    except Exception as e:
        error_msg = str(e)
        if "Unauthenticated" in error_msg:
            print("Error conectando al dispositivo: autenticación fallida.")
            print("Revisa la Comm Key del reloj y el valor de ZKTECO_PASSWORD.")
        elif "getaddrinfo failed" in error_msg:
            print("Error conectando al dispositivo: IP/host inválido.")
            print("Revisa ZKTECO_IP y asegúrate de que no tenga espacios extra.")
        elif "can't reach device" in error_msg or "TimedOut" in error_msg:
            print("Error conectando al dispositivo: no hay comunicación de red.")
            print("Revisa IP, cable/Wi-Fi y puerto 4370 del dispositivo.")
        else:
            print(f"Error conectando al dispositivo: {e}")
        return False


def validar_usuario_biometrico(timeout_segundos=30, intervalo_segundos=2):
    """Espera una nueva marcacion en el reloj y valida que pertenezca a un usuario registrado."""
    conn = None
    try:
        conn = conectar_dispositivo()
        users = conn.get_users() or []
        mapa_usuarios = {
            str(getattr(user, "user_id", "")).strip(): user
            for user in users
            if str(getattr(user, "user_id", "")).strip()
        }

        if not mapa_usuarios:
            print("No hay usuarios cargados en el dispositivo para validar acceso al bot.")
            return None

        logs_base = conn.get_attendance() or []
        vistos = {
            (
                str(getattr(log, "user_id", "")).strip(),
                str(getattr(log, "timestamp", "")),
                getattr(log, "status", ""),
                getattr(log, "punch", ""),
            )
            for log in logs_base
        }

        print("Esperando validacion biometrica en el reloj para habilitar ChatBot...")
        print(f"Tiempo maximo de espera: {timeout_segundos} segundos.")
        fin_espera = time.time() + timeout_segundos

        while time.time() < fin_espera:
            logs = conn.get_attendance() or []
            for log in logs:
                evento = (
                    str(getattr(log, "user_id", "")).strip(),
                    str(getattr(log, "timestamp", "")),
                    getattr(log, "status", ""),
                    getattr(log, "punch", ""),
                )
                if evento in vistos:
                    continue

                vistos.add(evento)
                user_id = evento[0]
                if user_id in mapa_usuarios:
                    usuario = mapa_usuarios[user_id]
                    print(f"Validacion OK. Usuario detectado: {usuario.name} (UserID: {user_id}).")
                    return usuario

                print(f"Evento detectado con UserID no reconocido ({user_id}).")

            time.sleep(intervalo_segundos)

        print("Tiempo agotado sin una validacion biometrica nueva.")
        return None
    except Exception as e:
        print(f"Error validando biometrico para ChatBot: {e}")
        return None
    finally:
        if conn:
            try:
                conn.enable_device()
            except Exception:
                pass
            try:
                conn.disconnect()
            except Exception:
                pass


def conectar_dispositivo():
    host = obtener_host_zkteco()
    if not diagnostico_red_previo(host, ZKTECO_PORT):
        raise ConnectionError("No fue posible validar conectividad con el dispositivo.")

    zk = ZK(host, port=ZKTECO_PORT, timeout=5, password=ZKTECO_PASSWORD)
    conn = zk.connect()
    conn.disable_device()
    return conn


def listar_usuarios_dispositivo():
    conn = None
    try:
        conn = conectar_dispositivo()
        users = conn.get_users()
        if not users:
            print("No hay usuarios registrados en el dispositivo.")
            return

        print(f"\nUsuarios registrados en {DEVICE_MODEL}:")
        for user in users:
            print(f" - UID: {user.uid} | UserID: {user.user_id} | Nombre: {user.name}")
    except Exception as e:
        print(f"Error listando usuarios: {e}")
    finally:
        if conn:
            try:
                conn.enable_device()
            except Exception:
                pass
            try:
                conn.disconnect()
            except Exception:
                pass


def ver_logs_dispositivo(limit=20):
    conn = None
    try:
        conn = conectar_dispositivo()
        logs = conn.get_attendance()
        if not logs:
            print("No hay logs de asistencia en el dispositivo.")
            return

        print(f"\nUltimos {min(limit, len(logs))} logs de asistencia:")
        for log in logs[-limit:]:
            estado = getattr(log, "status", "")
            punch = getattr(log, "punch", "")
            print(f" - UserID: {log.user_id} | Fecha: {log.timestamp} | Status: {estado} | Punch: {punch}")
    except Exception as e:
        print(f"Error leyendo logs: {e}")
    finally:
        if conn:
            try:
                conn.enable_device()
            except Exception:
                pass
            try:
                conn.disconnect()
            except Exception:
                pass


def exportar_logs_csv():
    conn = None
    try:
        conn = conectar_dispositivo()
        logs = conn.get_attendance()
        if not logs:
            print("No hay logs para exportar.")
            return

        EXPORT_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = EXPORT_DIR / f"logs_mb360_{ts}.csv"

        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["uid", "user_id", "timestamp", "status", "punch"])
            for log in logs:
                writer.writerow([
                    getattr(log, "uid", ""),
                    getattr(log, "user_id", ""),
                    getattr(log, "timestamp", ""),
                    getattr(log, "status", ""),
                    getattr(log, "punch", ""),
                ])

        print(f"Logs exportados correctamente a: {output_file}")
    except Exception as e:
        print(f"Error exportando logs: {e}")
    finally:
        if conn:
            try:
                conn.enable_device()
            except Exception:
                pass
            try:
                conn.disconnect()
            except Exception:
                pass


def monitorear_acciones_dispositivo(intervalo_segundos=3, tomar_fotos=False, stop_event=None):
    conn = None
    cam = None
    try:
        conn = conectar_dispositivo()
        EXPORT_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        sesion_dir = EXPORT_DIR / f"monitor_mb360_{ts}"
        fotos_dir = sesion_dir / "fotos"
        sesion_dir.mkdir(parents=True, exist_ok=True)
        fotos_dir.mkdir(parents=True, exist_ok=True)

        output_file = sesion_dir / f"eventos_{ts}.csv"
        error_file = sesion_dir / f"errores_{ts}.log"

        if tomar_fotos:
            cam = cv2.VideoCapture(0)
            if not cam.isOpened():
                with open(error_file, "a", encoding="utf-8") as ef:
                    ef.write(f"[{datetime.now().isoformat()}] No se pudo abrir la camara.\n")
                print("Advertencia: no se pudo abrir la cámara. Se continuará sin fotos.")
                cam = None

        logs_iniciales = conn.get_attendance() or []
        vistos = set()
        for log in logs_iniciales:
            vistos.add((getattr(log, "user_id", ""), str(getattr(log, "timestamp", "")), getattr(log, "status", ""), getattr(log, "punch", "")))

        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["user_id", "timestamp", "status", "punch", "foto"])

            print("\nMonitoreo en vivo iniciado.")
            print(f"Guardando eventos en: {output_file}")
            print(f"Guardando errores en: {error_file}")
            if tomar_fotos:
                print(f"Guardando fotos en: {fotos_dir}")
            else:
                print("Modo dispositivo: solo se registran eventos del MB360 (sin fotos de laptop).")
            print("Usa el boton 'Detener monitoreo' para finalizar.\n")

            while not (stop_event and stop_event.is_set()):
                try:
                    logs = conn.get_attendance() or []
                    for log in logs:
                        evento = (
                            getattr(log, "user_id", ""),
                            str(getattr(log, "timestamp", "")),
                            getattr(log, "status", ""),
                            getattr(log, "punch", ""),
                        )
                        if evento not in vistos:
                            vistos.add(evento)

                            foto_path = ""
                            if cam is not None:
                                ok, frame = cam.read()
                                if ok:
                                    foto_nombre = f"evento_{evento[0]}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                                    foto_archivo = fotos_dir / foto_nombre
                                    cv2.imwrite(str(foto_archivo), frame)
                                    foto_path = str(foto_archivo)
                                else:
                                    with open(error_file, "a", encoding="utf-8") as ef:
                                        ef.write(f"[{datetime.now().isoformat()}] No se pudo capturar foto para evento {evento}.\n")

                            print(f"Nuevo evento -> UserID: {evento[0]} | Fecha: {evento[1]} | Status: {evento[2]} | Punch: {evento[3]}")
                            writer.writerow([evento[0], evento[1], evento[2], evento[3], foto_path])
                            f.flush()

                    time.sleep(intervalo_segundos)
                except Exception as loop_error:
                    with open(error_file, "a", encoding="utf-8") as ef:
                        ef.write(f"[{datetime.now().isoformat()}] Error en loop de monitoreo: {loop_error}\n")
                        ef.write(traceback.format_exc())
                        ef.write("\n")
                    print(f"Error en monitoreo (continuando): {loop_error}")
                    time.sleep(intervalo_segundos)

            print("Monitoreo finalizado por solicitud del usuario.")

    except KeyboardInterrupt:
        print("\nMonitoreo detenido por usuario.")
    except Exception as e:
        print(f"Error en monitoreo: {e}")
    finally:
        if cam is not None:
            cam.release()
        if conn:
            try:
                conn.enable_device()
            except Exception:
                pass
            try:
                conn.disconnect()
            except Exception:
                pass


def diagnostico_dispositivo():
    print("\n=== DIAGNOSTICO MB360 ===")
    print(f"Modelo: {DEVICE_MODEL}")
    print(f"IP: {ZKTECO_IP}")
    print(f"Puerto: {ZKTECO_PORT}")
    print("Probando conexión y lectura de usuarios...")
    conectado = verificar_huella_con_zkteco()
    if conectado:
        print("Diagnóstico: OK. El dispositivo responde correctamente.")
    else:
        print("Diagnóstico: FALLIDO. Revisa red/Comm Key del dispositivo.")


def ayuda_mb360():
    print("\n=== AYUDA MB360 ===")
    print("1) El alta de huella/rostro se hace en el reloj, no desde laptop.")
    print("2) Este script solo consulta y exporta datos del dispositivo.")
    print("3) Si ves 'Unauthenticated', ajusta Comm Key/ZKTECO_PASSWORD.")
    print("4) Si no conecta, verifica IP, gateway y puerto 4370.")
    print("5) Usa la opcion de exportar para sacar logs en CSV.")
    print("6) Usa monitoreo en vivo para registrar nuevas acciones en tiempo real.")

# =========================
# Verificación Facial
# =========================
def verificar_rostro():
    ruta_rostro = Path(__file__).resolve().parent / "persona_conocida.jpg"
    if not ruta_rostro.exists():
        print(f"No se encontró la imagen de referencia: {ruta_rostro}")
        print("Primero usa la opción 2 para registrar un rostro.")
        return False

    video_capture = cv2.VideoCapture(0)
    known_image = face_recognition.load_image_file(str(ruta_rostro))
    known_encodings = face_recognition.face_encodings(known_image)
    if not known_encodings:
        print("No se detectó ningún rostro en la imagen de referencia.")
        print("Vuelve a registrar el rostro con la opción 2.")
        video_capture.release()
        cv2.destroyAllWindows()
        return False

    known_encoding = known_encodings[0]
    known_faces = [known_encoding]

    print("🧠 Escaneando rostro... Presiona 'q' para cancelar.")

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("No se pudo leer la cámara.")
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_encodings = face_recognition.face_encodings(rgb_frame)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_faces, face_encoding)
            if True in matches:
                print("Rostro reconocido.")
                video_capture.release()
                cv2.destroyAllWindows()
                return True

        cv2.imshow('Reconocimiento Facial', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
    return False

# =========================
# Iniciar ChatBot
# =========================
def iniciar_chatbot():
    print("\n ChatBot activado. Escribe 'salir' para terminar.")
    while True:
        entrada = input("Tú: ")
        if entrada.lower() == 'salir':
            print("Bot: ¡Hasta luego!")
            break
        respuesta = chatbot.get_response(entrada)
        print("Bot:", respuesta)

# =========================
# Menú principal
# =========================
def mostrar_menu():
    print(f"\n=== MENÚ {DEVICE_MODEL} ===")
    print("1. Diagnostico de conexion MB360")
    print("2. Listar usuarios del dispositivo")
    print("3. Ver ultimos logs de asistencia")
    print("4. Exportar logs a CSV")
    print("5. Monitorear acciones en vivo")
    print("6. Ayuda para MB360")
    print("7. Salir")
    
    opcion = input("Selecciona una opcion (1-7): ")

    if opcion == '1':
        diagnostico_dispositivo()
    elif opcion == '2':
        listar_usuarios_dispositivo()
    elif opcion == '3':
        ver_logs_dispositivo()
    elif opcion == '4':
        exportar_logs_csv()
    elif opcion == '5':
        monitorear_acciones_dispositivo(tomar_fotos=False)
    elif opcion == '6':
        ayuda_mb360()
    elif opcion == '7':
        print("¡Hasta luego!")
        exit()
    else:
        print("Opción no válida. Intenta de nuevo.")


class TextRedirector:
    """Redirige prints hacia un widget de texto y también conserva salida en consola."""

    def __init__(self, text_widget, original_stream):
        self.text_widget = text_widget
        self.original_stream = original_stream

    def write(self, message):
        self.original_stream.write(message)
        if not message:
            return

        def append_text():
            self.text_widget.configure(state="normal")
            self.text_widget.insert("end", message)
            self.text_widget.see("end")
            self.text_widget.configure(state="disabled")

        self.text_widget.after(0, append_text)

    def flush(self):
        self.original_stream.flush()


def abrir_chatbot_visual(parent, usuario_nombre="Usuario"):
    ventana = tk.Toplevel(parent)
    ventana.title("ChatBot - Asistente")
    ventana.geometry("620x460")

    marco = ttk.Frame(ventana, padding=10)
    marco.pack(fill="both", expand=True)

    historial = ScrolledText(marco, wrap="word", font=("Consolas", 10), height=18)
    historial.pack(fill="both", expand=True, pady=(0, 8))
    historial.insert("end", f"Bot: Bienvenido/a {usuario_nombre}. ChatBot activado.\n")
    historial.insert("end", "Bot: Escribe tu mensaje y presiona Enter.\n")
    historial.configure(state="disabled")

    fila = ttk.Frame(marco)
    fila.pack(fill="x")

    entrada_var = tk.StringVar()
    entrada = ttk.Entry(fila, textvariable=entrada_var)
    entrada.pack(side="left", fill="x", expand=True, padx=(0, 6))
    entrada.focus_set()

    def anexar_linea(texto):
        historial.configure(state="normal")
        historial.insert("end", texto + "\n")
        historial.see("end")
        historial.configure(state="disabled")

    def enviar_mensaje(_event=None):
        mensaje = entrada_var.get().strip()
        if not mensaje:
            return

        entrada_var.set("")
        anexar_linea(f"Tu: {mensaje}")
        try:
            respuesta = chatbot.get_response(mensaje)
            anexar_linea(f"Bot: {respuesta}")
        except Exception as e:
            anexar_linea(f"Bot: Error procesando mensaje ({e}).")

    ttk.Button(fila, text="Enviar", command=enviar_mensaje).pack(side="right")
    entrada.bind("<Return>", enviar_mensaje)


def iniciar_interfaz_visual():
    root = tk.Tk()
    root.title(f"Panel {DEVICE_MODEL} - Biometricos")
    root.geometry("980x650")

    style = ttk.Style(root)
    try:
        style.theme_use("clam")
    except Exception:
        pass

    contenedor = ttk.Frame(root, padding=12)
    contenedor.pack(fill="both", expand=True)

    titulo = ttk.Label(
        contenedor,
        text=f"Control {DEVICE_MODEL} (modo visual)",
        font=("Segoe UI", 14, "bold"),
    )
    titulo.pack(anchor="w", pady=(0, 8))

    subtitulo = ttk.Label(
        contenedor,
        text="Ejecuta acciones del dispositivo sin usar el menu de consola.",
    )
    subtitulo.pack(anchor="w", pady=(0, 12))

    panel_botones = ttk.Frame(contenedor)
    panel_botones.pack(fill="x", pady=(0, 10))

    salida = ScrolledText(contenedor, wrap="word", font=("Consolas", 10), height=26)
    salida.pack(fill="both", expand=True)
    salida.configure(state="disabled")

    original_stdout = sys.stdout
    original_stderr = sys.stderr
    sys.stdout = TextRedirector(salida, original_stdout)
    sys.stderr = TextRedirector(salida, original_stderr)

    estado = {"monitor_hilo": None}

    def ejecutar_async(func):
        hilo = threading.Thread(target=func, daemon=True)
        hilo.start()

    def iniciar_monitoreo_gui():
        hilo_actual = estado.get("monitor_hilo")
        if hilo_actual and hilo_actual.is_alive():
            print("El monitoreo ya se encuentra en ejecucion.")
            return

        MONITOR_STOP_EVENT.clear()
        hilo = threading.Thread(
            target=lambda: monitorear_acciones_dispositivo(tomar_fotos=False, stop_event=MONITOR_STOP_EVENT),
            daemon=True,
        )
        estado["monitor_hilo"] = hilo
        hilo.start()

    def detener_monitoreo_gui():
        MONITOR_STOP_EVENT.set()
        print("Solicitud de detencion enviada al monitoreo.")

    def entrar_chatbot_por_dispositivo():
        def tarea_chat():
            print("Iniciando validacion biometrica para acceso al ChatBot...")
            usuario_validado = validar_usuario_biometrico(timeout_segundos=30, intervalo_segundos=2)
            if usuario_validado:
                nombre_usuario = getattr(usuario_validado, "name", "Usuario") or "Usuario"
                root.after(0, lambda: abrir_chatbot_visual(root, nombre_usuario))
                print("Acceso concedido al ChatBot por validacion biometrica.")
            else:
                print("Acceso denegado al ChatBot: no hubo validacion biometrica valida.")

        ejecutar_async(tarea_chat)

    ttk.Button(
        panel_botones,
        text="Diagnostico",
        command=lambda: ejecutar_async(diagnostico_dispositivo),
    ).pack(side="left", padx=4)

    ttk.Button(
        panel_botones,
        text="Listar usuarios",
        command=lambda: ejecutar_async(listar_usuarios_dispositivo),
    ).pack(side="left", padx=4)

    ttk.Button(
        panel_botones,
        text="Ver logs",
        command=lambda: ejecutar_async(ver_logs_dispositivo),
    ).pack(side="left", padx=4)

    ttk.Button(
        panel_botones,
        text="Exportar CSV",
        command=lambda: ejecutar_async(exportar_logs_csv),
    ).pack(side="left", padx=4)

    ttk.Button(
        panel_botones,
        text="Monitorear",
        command=iniciar_monitoreo_gui,
    ).pack(side="left", padx=4)

    ttk.Button(
        panel_botones,
        text="Detener monitoreo",
        command=detener_monitoreo_gui,
    ).pack(side="left", padx=4)

    ttk.Button(
        panel_botones,
        text="Ayuda",
        command=lambda: ejecutar_async(ayuda_mb360),
    ).pack(side="left", padx=4)

    ttk.Button(
        panel_botones,
        text="Entrar ChatBot",
        command=entrar_chatbot_por_dispositivo,
    ).pack(side="left", padx=4)

    def cerrar_aplicacion():
        MONITOR_STOP_EVENT.set()
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        root.destroy()

    ttk.Button(panel_botones, text="Salir", command=cerrar_aplicacion).pack(side="right", padx=4)

    print(f"Interfaz visual iniciada para {DEVICE_MODEL}.")
    print("Usa los botones superiores para ejecutar acciones.")
    print("Atajo: Ctrl+C dentro de la ventana para cerrar la app.")
    root.bind_all("<Control-c>", lambda _event: cerrar_aplicacion())
    root.protocol("WM_DELETE_WINDOW", cerrar_aplicacion)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        cerrar_aplicacion()

# =========================
# Programa Principal
# =========================
if __name__ == "__main__":
    iniciar_interfaz_visual()
    