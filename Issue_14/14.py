import cv2

# Abrir uma conexão com a camera, 0 é o padrão da webcam
cap = cv2.VideoCapture(0)
while True:
    # Capturar o frame atual
    ret, frame = cap.read()
    # Se tiver erro é para parar o loop
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("imagem", frame)
    cv2.imshow("imagem cinza", frame_gray)
    # Espere 1ms pela tecla "q" para quebrar o loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
# Liberar a câmera e fechar a janelas
cap.release()
cv2.destroyAllWindows()
