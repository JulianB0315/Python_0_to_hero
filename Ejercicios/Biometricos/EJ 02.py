from zk import ZK
import cv2
import face_recognition
from transformers import pipeline

# =========================
# Configuración del dispositivo ZKTeco
# =========================
ZKTECO_IP = "192.168.1.201"
ZKTECO_PORT = 4370

# =========================
# Inicializar ChatBot con Transformers
# =========================
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

# =========================
# Registrar nuevo usuario en ZKTeco
# =========================
def registrar_usuario(nombre, user_id="1234", role=0):
    try:
        conn = ZK(ZKTECO_IP, port=ZKTECO_PORT, timeout=5, password=0).connect()
        conn.disable_device()
        conn.set_user(uid=user_id, name=nombre, privilege=role, password='', group_id='', card=0)
        print(f"Usuario {nombre} registrado exitosamente.")
    except Exception as e:
        print(f"Error registrando usuario: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.enable_device()
            conn.disconnect()

# =========================
# Registrar rostro con la cámara
# =========================
def registrar_rostro(nombre_archivo="persona_conocida.jpg"):
    video_capture = cv2.VideoCapture(0)
    print("Por favor, mira a la cámara para registrar tu rostro.")
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error accediendo a la cámara.")
            break
        cv2.imshow('Registro de Rostro', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite(nombre_archivo, frame)
            print(f"Rostro registrado y guardado como {nombre_archivo}.")
            break
    video_capture.release()
    cv2.destroyAllWindows()

# =========================
# Verificación con ZKTeco MB360 (huella registrada)
# =========================
def verificar_huella_con_zkteco():
    try:
        conn = ZK(ZKTECO_IP, port=ZKTECO_PORT, timeout=5, password=0).connect()
        conn.disable_device()
        print("Coloca tu dedo en el lector de huellas.")
        # Simulación de verificación de huella
        autenticado = True  # Cambiar según la lógica de verificación
        conn.enable_device()
        return autenticado
    except Exception as e:
        print(f"Error verificando huella: {e}")
        return False
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.disconnect()

# =========================
# Verificación Facial
# =========================
def verificar_rostro():
    video_capture = cv2.VideoCapture(0)
    print("Por favor, mira a la cámara para la verificación facial.")
    rostro_conocido = face_recognition.load_image_file("persona_conocida.jpg")
    encoding_rostro_conocido = face_recognition.face_encodings(rostro_conocido)[0]
    autenticado = False
    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Error accediendo a la cámara.")
            break
        rgb_frame = frame[:, :, ::-1]
        encodings_rostros = face_recognition.face_encodings(rgb_frame)
        for encoding in encodings_rostros:
            autenticado = face_recognition.compare_faces([encoding_rostro_conocido], encoding)[0]
            if autenticado:
                print("Verificación facial exitosa.")
                break
        if autenticado or cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    return autenticado

# =========================
# Iniciar ChatBot
# =========================
def iniciar_chatbot():
    print("\nChatBot activado. Escribe 'salir' para terminar.")
    while True:
        entrada = input("Tú: ")
        if entrada.lower() == 'salir':
            print("Bot: ¡Hasta luego!")
            break
        respuesta = chatbot(entrada)
        print("Bot:", respuesta[0]['generated_text'])

# =========================
# Menú principal
# =========================
def mostrar_menu():
    print("\nMenú Principal:")
    print("1. Registrar nuevo usuario")
    print("2. Registrar rostro")
    print("3. Verificar y acceder al ChatBot")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == '1':
        nombre = input("Ingresa el nombre del usuario: ")
        registrar_usuario(nombre)
    elif opcion == '2':
        registrar_rostro()
    elif opcion == '3':
        autenticado = verificar_huella_con_zkteco() and verificar_rostro()
        if autenticado:
            iniciar_chatbot()
        else:
            print("Acceso denegado.")
    elif opcion == '4':
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