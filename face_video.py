import cv2

# Cargar la cascada
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Video de la webcam.
cap = cv2.VideoCapture(0)
# Para usar un video
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Leer framexframe
    _, img = cap.read()

    # Convertir a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar las caras
    caras = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Dibujar el rectangulo alrededor de la cara
    for (x, y, w, h) in caras:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Mostrar el programa
    cv2.imshow('img', img)

    # Frenar si se apreta ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
