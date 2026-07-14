import cv2

img = cv2.imread("arara.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Filtro que retira bordas, ele aplica o filtro gaussiano para tirar imperfeições, aplica o filtro gradiente para tirar bordas e aplica um limiar para deixar as bordas finas
Canny = cv2.Canny(img_gray, 100, 200)
cv2.imshow("imagem", img)
cv2.imshow("imagem cinza", img_gray)
cv2.imshow("Canny", Canny)
cv2.imwrite("imagem.jpg", img)
cv2.imwrite("imagem_cinza.jpg", img_gray)
cv2.imwrite("Canny.jpg", Canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
