import cv2
import numpy as np

img = cv2.imread("arara.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
linhas, colunas = img_gray.shape
# limiar
T = 127
mimg = np.zeros((linhas, colunas), dtype=np.uint8)
# Transformando a imagem em uma matriz estatica e aplicando um limiar na matriz
for i in range(linhas):
    for j in range(colunas):
        if img_gray[i, j] > T:
            mimg[i, j] = 255
        elif img_gray[i, j] <= T:
            mimg[i, j] = 0
# Transformando a matriz limiarizada em um .txt
np.savetxt("arara.txt", mimg, fmt="%d")
cv2.imshow("imagem", img)
cv2.imshow("imagem cinza", img_gray)
cv2.imwrite("imagem.jpg", img)
cv2.imwrite("imagem_cinza.jpg", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
