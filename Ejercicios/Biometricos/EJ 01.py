import sys
import csv
import time
import traceback
from datetime import datetime

import chatterbot_corpus
from zk import ZK
import cv2
import face_recognition
from chatterbot import ChatBot, languages
from chatterbot.trainers import ChatterBotCorpusTrainer
from pathlib import Path

# =========================
# Configuración del dispositivo ZKTeco
# =========================
DEVICE_MODEL = "MB360"
ZKTECO_IP = "192.168.106.201"
ZKTECO_PORT = 4370
ZKTECO_PASSWORD = 23  # o la Comm Key real del reloj
EXPORT_DIR = Path(__file__).resolve().parent / "exports"
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
    zk = ZK(ZKTECO_IP, port=ZKTECO_PORT, timeout=5, password=ZKTECO_PASSWORD)
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
    zk = ZK(ZKTECO_IP, port=ZKTECO_PORT, timeout=5, password=ZKTECO_PASSWORD)
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
        elif "can't reach device" in error_msg or "TimedOut" in error_msg:
            print("Error conectando al dispositivo: no hay comunicación de red.")
            print("Revisa IP, cable/Wi-Fi y puerto 4370 del dispositivo.")
        else:
            print(f"Error conectando al dispositivo: {e}")
        return False


def conectar_dispositivo():
    zk = ZK(ZKTECO_IP, port=ZKTECO_PORT, timeout=5, password=ZKTECO_PASSWORD)
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


def monitorear_acciones_dispositivo(intervalo_segundos=3, tomar_fotos=False):
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
            print("Presiona Ctrl+C para detener.\n")

            while True:
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

# =========================
# Programa Principal
# =========================
if __name__ == "__main__":
    while True:
        mostrar_menu()
    