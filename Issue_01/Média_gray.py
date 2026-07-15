import cv2
import numpy as np
img = cv2.imread("images.png", 0)
imgp = cv2.resize(img, (256, 256))
linhas, colunas = imgp.shape
M = np.zeros((linhas+2, colunas+2))
Sa = np.zeros((linhas,colunas), dtype=np.uint8)
#Laço de moldura de zeros
for i in range(linhas):
    for j in range(colunas):
        M[i+1, j+1] = imgp[i, j]
for i in range(1, linhas+1):
    for j in range (1, colunas+1):
        S = 0
        #Kernel 3x3
        for f in range (i-1, i+2):
            for g in range (j-1, j+2):
                S += M[f, g]
        #Nova pixel com a média dos pixels vizinhos
        Sa[i-1, j-1] = S/9
cv2.imshow("original", imgp)
cv2.imshow("Média", Sa)             
cv2.imwrite("Media.png", Sa)
cv2.waitKey(0)
cv2.destroyAllWindows()