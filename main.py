import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

cap = cv2.VideoCapture(0)
detection_enabled = False  # Variable para habilitar/deshabilitar la detección

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if detection_enabled:
        # Detección de caras
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, 'Cara', (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Detección de cuerpos
        bodies = body_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in bodies:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(img, 'Cuerpo', (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    cv2.imshow('Deteccion de Caras y Cuerpos', img)

    k = cv2.waitKey(30)

    if k == 27 or cv2.getWindowProperty('Deteccion de Caras y Cuerpos',
                                        cv2.WND_PROP_VISIBLE) < 1:  # 27 es ASCII para Esc
        break
    elif k == ord('s') or k == ord('S'):  # Si se presiona la tecla 's' o 'S', se activa/desactiva la detección
        detection_enabled = not detection_enabled

cap.release()
cv2.destroyAllWindows()