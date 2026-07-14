import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread("arara.jpg", 0)
plt.hist(img.ravel(), bins=256, range=[0, 256])
plt.title("Histograma")
plt.xlabel("Intensidade")
plt.ylabel("Quantidade de pixels")
plt.savefig("Histograma.jpg")
plt.close()
cv2.imwrite("Arara.jpg", img)
linhas, colunas = img.shape
L = 256
S = [0] * 256
equalizado = np.zeros((linhas, colunas))
n = linhas * colunas
for f in range(L):
    nj = 0
    for linha in img:
        for pixel in linha:
            if pixel == f:
                nj += 1
    S[f] = nj / n
for f in range(1, L):
    S[f] += S[f - 1]
for i in range(linhas):
    for j in range(colunas):
        r = img[i, j]
        equalizado[i, j] = int((L - 1) * S[r])
plt.hist(equalizado.ravel(), bins=256, range=[0, 256])
plt.title("Histograma equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Quantidade de pixels")
plt.savefig("Histograma_equalizado.jpg")
plt.close()
cv2.imwrite("Arara_equalizada.jpg", equalizado)
