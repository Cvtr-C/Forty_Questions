import cv2

img = cv2.imread("arara.jpg")
# Separando em três espaços de cores, H (Hue/Matriz) é a cor em si, S (Saturation) é a saturação e V (Value) que é Brilho
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
H, S, V = cv2.split(img_hsv)
cv2.imshow("araraH", H)
cv2.imshow("araraS", S)
cv2.imshow("araraV", V)
cv2.imwrite("AraraH.jpg", H)
cv2.imwrite("AraraS.jpg", S)
cv2.imwrite("AraraV.jpg", V)
cv2.waitKey(0)
cv2.destroyAllWindows()
