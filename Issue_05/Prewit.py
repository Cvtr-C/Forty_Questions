import cv2
import numpy as np 
img = cv2.imread("images.jpeg", 0)
imgp = cv2.resize(img, (256, 256))
linhas, colunas = imgp.shape
#Diereção horizontal(Mudança na vertical)
Prewitx = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]
], dtype=np.int32)
#Direção vertical(Mudanças na horizontal)
Prewity = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
], dtype=np.int32)
zeros = np.zeros((linhas+2, colunas+2), dtype=np.int32)
Prewit = np.zeros((linhas, colunas), dtype=np.int32)
#Bordas de zeros
for i in range(linhas):
    for j in range(colunas):
        zeros[i+1, j+1] = imgp[i, j]
#Aplicação do Prewit para destacar bordas
for i in range(1, linhas+1):
    for j in range(1, colunas+1):
        X, Y = 0, 0
        for f in range(3):
            for g in range(3):
                X += zeros[i+f-1, j+g-1]*Prewitx[f, g]
                Y += zeros[i+f-1, j+g-1]*Prewity[f, g]
        Prewit[i-1, j-1] = (X**2+Y**2)**(0.5)
#Funções para caso passe números negativos ou altos
Prewit = np.abs(Prewit)
Prewit = np.clip(Prewit, 0, 255)
Prewit = Prewit.astype(np.uint8)
cv2.imshow("Original", imgp)
cv2.imshow("Prewit", Prewit)
cv2.imwrite("Prewit.png", Prewit)
cv2.waitKey(0)
cv2.destroyAllWindows()