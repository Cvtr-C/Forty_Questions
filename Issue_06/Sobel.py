import cv2
import numpy as np
img = cv2.imread("images.png", 0)
imgp = cv2.resize(img, (256, 256))
linhas, colunas = imgp.shape
#Direção horizontal (Mudanças na vertical)
Sobelx =np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
], dtype=np.int32)
#Direção vertical (Mudanças na horizontal)
Sobely = np.array([
    [-1, -2, -1],
    [0, 0 , 0],
    [1, 2, 1]
], dtype=np.int32)
zeros = np.zeros((linhas+2, colunas+2), dtype=np.int32)
Sobel = np.zeros((linhas, colunas), dtype=np.int32)
#Bordas de zeros
for i in range(linhas):
    for j in range(colunas):
        zeros[i+1, j+1] = imgp[i, j]
#Aplicação do Sobel para destacar bordas, e é melhor que o prewit, pois trata de o peso diminui a influência de ruídos de alta frequência
for i in range(1, linhas+1):
    for j in range(1, colunas+1):
        X, Y = 0, 0
        for f in range(3):
            for g in range(3):
                X += zeros[i+f-1, j+g-1]*Sobelx[f, g]
                Y += zeros[i+f-1, j+g-1]*Sobely[f, g]
        Sobel[i-1, j-1] = (X**2+Y**2)**(0.5)
#Funções para caso passe números negativos ou muito grandes
Sobel = np.abs(Sobel)
Sobel = np.clip(Sobel, 0, 255)
Sobel = Sobel.astype(np.uint8)
cv2.imshow("Original", imgp)
cv2.imshow("Sobel", Sobel)
cv2.imwrite("Sobel.png", Sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()