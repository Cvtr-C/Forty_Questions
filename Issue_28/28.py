import cv2

img = cv2.imread("arara.jpg", 0)
# Limiarização automatica, sem interferencia de luminosidade
automatica = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2
)
cv2.imshow("imagem", automatica)
cv2.waitKey(0)
cv2.destroyAllWindows()
