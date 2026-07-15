import cv2 
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("images.png", 0)
imgp = cv2.resize(img, (256, 256))
linhas, colunas = imgp.shape
hist = [0] * 256
#Contagem de pixels de cada intensidade
for linha in imgp:
    for pixel in linha:
        hist[pixel] += 1
#Criação de um histograma para usar como base para fazer a multilimiarização
plt.figure(figsize=(8, 4))
plt.bar(range(256), hist, width=1)
plt.title("Histograma Original")
plt.xlabel("Intensidade")
plt.ylabel("Quantidade de pixels")
plt.xlim(0, 255)
plt.savefig("HistOri.png")
multlim = np.zeros((linhas, colunas), dtype=np.uint8)
hist2 = [0] * 256
#Variaveis que criam intervalos para multilimiarização
T1, T2, T3, T4, T5 = 250, 200, 150, 100, 50
#Aplicação da multilimiarização dividida em 6 partes
for i in range(linhas):
    for j in range(colunas):
        if imgp[i, j]>T1:
           multlim[i, j] = 255 
        elif T2<imgp[i, j]<=T1:
           multlim[i, j] = 127 
        elif T3<imgp[i, j]<=T2:
           multlim[i, j] = 255 
        elif T4<imgp[i, j]<=T3:
           multlim[i, j] = 0
        elif  T5<imgp[i, j]<=T4:
            multlim[i, j] = 255
        elif imgp[i, j]<=T5:
            multlim[i, j] = 0
#Contagem de pixels de cada intensidade da imagem multilimiarizada
for linhan in multlim:
    for pix in linhan:
        hist2[pix] += 1
#Histograma da imagem multilimiarizada
plt.figure(figsize=(8, 4))
plt.bar(range(256), hist2, width=1)
plt.title("Histograma multilimiarizado")
plt.xlabel("Intensidade")
plt.ylabel("Quantidade de pixels")
plt.xlim(0, 255)
plt.savefig("Histmtlim.png")
cv2.imwrite("Multilim.png", multlim)