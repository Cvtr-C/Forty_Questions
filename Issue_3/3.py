import cv2

img = cv2.imread("arara.jpg")
# Separando a imagem em BGR, ordem Azul, Verde, Vermelho
B, G, R = cv2.split(img)
cv2.imshow("araraB", B)
cv2.imshow("araraG", G)
cv2.imshow("araraR", R)
cv2.imwrite("AraraB.jpg", B)
cv2.imwrite("AraraG.jpg", G)
cv2.imwrite("AraraR.jpg", R)
cv2.imshow("arara", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
