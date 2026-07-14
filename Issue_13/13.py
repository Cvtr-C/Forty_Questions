import cv2
import numpy as np

img = cv2.imread("arara.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
linhas, colunas = img_gray.shape
mimg = np.zeros((linhas, colunas), dtype=np.uint8)
zeros = np.zeros((linhas + 2, colunas + 2), dtype=np.uint8)
Sobel = np.zeros((linhas, colunas), dtype=np.uint8)
SobelX = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.int32)
SobelY = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.int32)
for i in range(linhas):
    for j in range(colunas):
        mimg[i, j] = img_gray[i, j]
for i in range(linhas):
    for j in range(colunas):
        zeros[i + 1, j + 1] = mimg[i, j]
for i in range(1, linhas + 1):
    for j in range(1, colunas + 1):
        Sx = 0
        Sy = 0
        for f in range(3):
            for g in range(3):
                Sx += zeros[i + f - 1, j + g - 1] * SobelX[f, g]
                Sy += zeros[i + f - 1, j + g - 1] * SobelY[f, g]
        Sobel[i - 1, j - 1] = (Sx**2 + Sy**2) ** 0.5
cv2.imshow("Arara sobel", Sobel)
cv2.imshow("Arara cinza", img_gray)
cv2.imshow("Arara", img)
cv2.imwrite("Arara_Sobel", Sobel)
cv2.imwrite("Arara_cinza", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
