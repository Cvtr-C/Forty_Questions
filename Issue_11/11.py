import cv2
import numpy as np

img = cv2.imread("Qadrado.jpg", 0)
linhas, colunas = img.shape
mimg = np.zeros((linhas, colunas), dtype=np.uint8)
Xt, Yt, T = 0, 0, 0
for i in range(linhas):
    for j in range(colunas):
        mimg[i, j] = img[i, j]
        if mimg[i, j] == 0:
            Xt += i
            Yt += j
            T += 1
Xc = int(np.ceil(Xt / T))
Yc = int(np.ceil(Yt / T))
mimg[Xc, Yc] = 255
cv2.imshow("Quadrado", img)
cv2.imshow("Centro", mimg)
cv2.imwrite("Centro.jpg", mimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
