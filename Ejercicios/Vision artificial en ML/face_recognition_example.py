import cv2
import datetime

# Cargar el modelo de detección de caras (Haar cascades)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Inicializar la cámara con manejo de errores
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("Error: No se pudo acceder a la cámara.")
    exit()

# Parámetros para calcular la distancia
KNOWN_DISTANCE = 50.0  # Distancia conocida en cm
KNOWN_WIDTH = 14.0  # Ancho promedio de una cara humana en cm
FOCAL_LENGTH = 600  # Longitud focal calibrada (ajustar según la cámara)

def save_biometric_data(image, biometric_data):
    """Guardar la imagen y los datos biométricos en un archivo."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    image_filename = f"foto_{timestamp}.png"
    data_filename = f"datos_biometricos_{timestamp}.txt"

    # Guardar la imagen
    cv2.imwrite(image_filename, image)

    # Guardar los datos biométricos
    with open(data_filename, "w") as file:
        file.write("Datos biométricos:\n")
        for data in biometric_data:
            file.write(f"Distancia: {data['distance']:.2f} cm, Ancho: {data['width']} px\n")

    print(f"Foto guardada como {image_filename}")
    print(f"Datos biométricos guardados en {data_filename}")

while True:
    # Capturar un cuadro de la cámara
    ret, frame = video_capture.read()
    if not ret:
        print("Advertencia: No se pudo leer el cuadro de la cámara.")
        continue  # Intentar leer el siguiente cuadro

    # Convertir a escala de grises para la detección de caras
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar caras en el cuadro
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Calcular la distancia en cm para cada cara detectada
        distance = (KNOWN_WIDTH * FOCAL_LENGTH) / w
        distance_text = f"Distancia: {distance:.2f} cm"

        # Dibujar el cuadro delimitador y las etiquetas para cada cara
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, distance_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)  # Texto en verde

        # Dibujar puntos en una cuadrícula dentro del área del rostro
        step_x = w // 10
        step_y = h // 10
        for i in range(0, w, step_x):
            for j in range(0, h, step_y):
                cv2.circle(frame, (x + i, y + j), 2, (0, 255, 255), -1)  # Puntos amarillos

    # Mostrar el cuadro procesado con mapeo y distancias
    cv2.imshow("Mapeo de Rostro y Distancias", frame)

    # Tomar una foto y guardar datos biométricos con la tecla 's'
    if cv2.waitKey(1) & 0xFF == ord('s'):
        biometric_data = [{"distance": (KNOWN_WIDTH * FOCAL_LENGTH) / w, "width": w} for (x, y, w, h) in faces]
        save_biometric_data(frame, biometric_data)

    # Salir con la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
video_capture.release()
cv2.destroyAllWindows()
