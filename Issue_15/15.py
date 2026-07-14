import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Código igual ao outro, só aplica o filtro canny, extração de bordas finas
    frame_canny = cv2.Canny(frame_gray, 100, 200)
    cv2.imshow("imagem", frame)
    cv2.imshow("imagem cinza", frame_gray)
    cv2.imshow("imagem canny", frame_canny)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
