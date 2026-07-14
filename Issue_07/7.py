import cv2

img = cv2.imread("arara.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Filtro de liamirização é para transformar a imagem em binaria, 0 é o preto absoluto e 255 é o branco absoluto, e o limiar fala qual pixel vira 0 e qual vira 255
limiar, img_bin = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("imagem", img)
cv2.imshow("imagem cinza", img_gray)
cv2.imshow("imagem limiar", img_bin)
cv2.imwrite("imagem.jpg", img)
cv2.imwrite("imagem_gray.jpg", img_gray)
cv2.imwrite("imagem_binaria.jpg", img_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()
