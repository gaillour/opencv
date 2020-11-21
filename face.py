import cv2

# Cargar la cascaad
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Leer la imagen
img = cv2.imread('messi.jpg')

# Convertir a escala de grises
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detectar las caras
caras = face_cascade.detectMultiScale(gray, 1.1, 4)

# Dibujaar el rextangulo al rededor de la cara
for (x, y, w, h) in caras:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Mostrar el resultado
cv2.imshow('img', img)
cv2.waitKey()
