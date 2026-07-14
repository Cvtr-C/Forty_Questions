import cv2

img = cv2.imread("paisagem.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Redimensionamento e interpolação para não perder muito a nitidez, mas do pequeno para o maior perde
imgp = cv2.resize(img_gray, (160, 120), cv2.INTER_AREA)
imgg = cv2.resize(imgp, (640, 480), cv2.INTER_CUBIC)
cv2.imshow("imagem", img)
cv2.imshow("imagem cinza", img_gray)
cv2.imshow("Pequena", imgp)
cv2.imshow("Grande", imgg)
cv2.imwrite("imagem.jpg", img)
cv2.imwrite("imagem_cinza.jpg", img_gray)
cv2.imwrite("imagem_pequena.jpg", imgp)
cv2.imwrite("imagem_grande.jpg", imgg)
cv2.waitKey(0)
cv2.destroyAllWindows()
