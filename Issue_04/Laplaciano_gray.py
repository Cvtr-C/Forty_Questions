import cv2
import numpy as np
img = cv2.imread("images.jpeg", 0)
imgp = cv2.resize(img, (256, 256))
linhas, colunas = imgp.shape
zeros = np.zeros((linhas+2, colunas+2), dtype=np.int32)
Lap = np.zeros((linhas, colunas), dtype=np.int32)
#Filtro de 4 vizinho, bordas claras e fundo escuro
laplace1 = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]
], dtype=np.int32)
#Filtro 4 vizinhos, bordas escuras e fundo claro
laplace2 = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
], dtype=np.int32)
#Filtro 8 vizinhos, bordas claras e fundo escuro
laplace3 = np.array([
    [1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]
], dtype=np.int32)
#Filtro 8 vizinhos, bordas escuras e fundo claro
laplace4 = np.array([
    [-1, -1, -1],
    [-1, 8, -1],
    [-1, -1, -1]
], dtype=np.int32)
#Esclher o tipo de Kernel
mascara = laplace4
#Borda de zeros
for i in range(linhas):
    for j in range(colunas):
        zeros[i+1, j+1] = imgp[i, j]
#Apliação do Kernel
for i in range(1, linhas+1):
    for j in range(1, colunas+1):
        Lap[i-1, j-1] = 0
        for f in range(3):
            for g in range(3):
                Lap[i-1, j-1] += zeros[i+f-1, j+g-1]*mascara[f, g]
#Função para tratar de valores negativos e números altos                
Lap = np.abs(Lap)
Lap = np.clip(Lap, 0, 255)
Lap = Lap.astype(np.uint8)
cv2.imshow("Original", imgp)
cv2.imshow("Laplaciano", Lap)
cv2.imwrite("Laplaciano.png", Lap)
cv2.waitKey(0)
cv2.destroyAllWindows()