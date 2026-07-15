import cv2 
import numpy as np
#Função para calcular o kernel 1D do filtro gaussiano
def kernel_gaussiano(t, sigma):
    centro = t//2
    X = np.arange(-centro, centro+1)
    kernel1d = np.exp(-(X**2)/(2*sigma**2))
    kernel1d = kernel1d/np.sum(kernel1d)
    return kernel1d

img = cv2.imread("images.png", 0)
imgp = cv2.resize(img, (256, 256))
linhas, colunas = imgp.shape
#Variaveis (t = tamanho e sigma = desvio padrão) que vão entrar na função do kernel gaussiano e calculo da borda
sigma = 1
t = 2*int(np.ceil(3*sigma))+1
borda = t//2
zeros = np.zeros((linhas+2*borda, colunas+2*borda), dtype=np.float64)
gauss = np.zeros((linhas, colunas), dtype=np.float64)
T = np.zeros((linhas+2*borda, colunas+2*borda), dtype=np.float64)
gaussiano = kernel_gaussiano(t, sigma)
#Criar borda de zeros
for i in range(linhas):
    for j in range(colunas):
        zeros[i+borda, j+borda] = imgp[i, j]
#Aplicação do kernel separado, linha e coluna
for i in range(borda, linhas+borda):
    for j in range(borda, colunas+borda):
        T[i, j] = 0
        #kernel coluna
        for f in range(t):
            T[i, j] += zeros[i, j+f-borda]*gaussiano[f]
for i in range(borda, linhas+borda):
    for j in range(borda, colunas+borda):
        gauss[i-borda, j-borda] = 0   
        #kernel linha     
        for g in range(t):  
            gauss[i-borda, j-borda] += T[i+g-borda, j]*gaussiano[g]
#Funções para normalizar os número se eles explodirem ou se entrar número negativos   
gauss = np.clip(gauss, 0, 255)
gauss = gauss.astype(np.uint8)
cv2.imshow("Original", imgp)
cv2.imshow("Gaussiano", gauss)
cv2.imwrite("Gaussiano.png", gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()