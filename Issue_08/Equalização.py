import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread("images.png", 0)
imgp = cv2.resize(img, (256, 256))
linhas, colunas = imgp.shape
L = 256
S = [0] * 256
hist = [0] * 256
eq = np.zeros((linhas, colunas), dtype=np.uint8)
n = linhas*colunas
#S[f] vai assumir o valor da probabilidade de cada intensidade
for f in range(256):
    nj = 0
    for linha in imgp:
        for pixel in linha:
            if pixel == f:
                nj += 1
    S[f] = (nj/n)
#Aqui S[f] vai assumir os valores do somatorio da intensidade com os anteriores
for f in range(1, 256):
    S[f] += S[f-1]
#Aplicação da formula da equalização
for i in range(linhas):
    for j in range (colunas):
        r = imgp[i, j] 
        eq[i, j] = int((L-1)*S[r])
#Contagem de quantos pixels tem cada intensidade
for linhan in eq:
    for pix in linhan:
        hist[pix] += 1
#Criação do histograma
plt.figure(figsize=(8, 4))
plt.bar(range(256), hist, width=1)
plt.title("Histograma equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Quantidade de pixels")
plt.xlim(0, 255)
plt.savefig("Histeq.png")
cv2.imwrite("imageeq.png", eq)