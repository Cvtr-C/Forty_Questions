import cv2
import numpy as np

img = cv2.imread("img.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
# Extração de circulo, em uma imagem cheia de outras formas
circles = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    dp=1,
    minDist=50,
    param1=50,
    param2=30,
    minRadius=10,
    maxRadius=350,
)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 4)
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 5)
cv2.imshow("Circulo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
