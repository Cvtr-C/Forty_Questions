import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("images.png", 0)
imgp = cv2.resize(img, (256, 256))
linhas, colunas = imgp.shape
lim = np.zeros((linhas, colunas), dtype=np.uint8)
hist = [0] * 256
#Variavel para devinir o valor de limiarização
T = 128
#Aplicação da limiarização
for i in range(linhas):
    for j in range(colunas):
        if imgp[i,j]>T:
            lim[i, j] = 255
        elif imgp[i, j]<=T:
            lim[i, j] = 0
#Contagem de pixels com cada intensidade de cor
for linha in lim:
    for pixel in linha:
        hist[pixel] += 1
#Criação do histograma
plt.figure(figsize=(8, 4))
plt.bar(range(256), hist, width=4)
plt.title("Histograma limiarização")
plt.xlabel("Intensidade")
plt.ylabel("Quantidade de pixels")
plt.xlim(0, 255)
plt.savefig("Histlimi.png")
cv2.imwrite("Limiarizada.png", lim)