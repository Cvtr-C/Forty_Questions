import cv2
import numpy as np
img = cv2.imread("images.png", 0)
imgp = cv2.resize(img, (256, 256))
linhas, colunas = imgp.shape
imgs = np.zeros((linhas+2, colunas+2), dtype=np.uint8)
M = np.zeros((linhas, colunas), dtype=np.uint8)
#Moldura de zeros
for i in range(linhas):
    for j in range(colunas):
        imgs[i+1, j+1] = imgp[i, j]
for i in range(1, linhas+1):
    for j in range(1, colunas+1):
        V = []
        #Laço 1 para tranformar um Kernel 3x3 em um vetor linear
        for f in range(i-1, i+2):
            for g in range(j-1, j+2):
                V.append(imgs[f, g])
        #Laço 2 para organizar em rol o vetor linear
        for f in range(8):
            for g in range(8-f):
                if V[g] > V[g+1]:
                    a = V[g+1]
                    V[g+1] = V[g]
                    V[g] = a
        #Novo pixel da nova imagem é igual ao número do meio do vetor linear em rol
        M[i-1, j-1] = V[4]                    
cv2.imshow("Original", imgp)
cv2.imshow("Mediana", M)
cv2.imwrite("Mediana.png", M)
cv2.waitKey(0)        
cv2.destroyAllWindows()