import cv2
import numpy as np

img = cv2.imread("img.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
canny = cv2.Canny(blur, 50, 250)
contornos, hierarquia = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
for i, contor in enumerate(contornos, start=1):
    x, y, w, h = cv2.boundingRect(contor)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # Criar subimagens
    subimagem = img[y : y + h, x : x + w]
    cv2.imshow(f"subimagem {i}", subimagem)
cv2.imshow("contornos", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
