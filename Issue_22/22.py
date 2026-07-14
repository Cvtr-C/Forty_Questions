import cv2
import numpy as np

img = cv2.imread("figura.jpg", 0)
linhas, colunas = img.shape
profundidade = 10
# Volume(z, y, x)
volume = np.zeros((profundidade, linhas, colunas), dtype=np.uint8)
# Empilhar imagens para criar da terceira dimensão (profundidade)
for z in range(profundidade):
    volume[z] = img.copy()
semente = (5, 120, 160)
# like = copiar dimensões da matriz já existente
# Criando mascara região
regiao = np.zeros_like(volume, dtype=np.uint8)
lista = [semente]
regiao[semente] = 255
vizinho = [
    (-1, 0, 0),
    (1, 0, 0),  # (Z)profundiade
    (0, -1, 0),
    (0, 1, 0),  # (Y)linhas
    (0, 0, -1),
    (0, 0, 1),  # (X)colunas
]
while len(lista) > 0:
    z_atual, y_atual, x_atual = lista.pop(0)
    for dz, dy, dx in vizinho:
        nz, ny, nx = z_atual + dz, y_atual + dy, x_atual + dx
        if 0 <= nz < profundidade and 0 <= ny < linhas and 0 <= nx < colunas:
            if volume[nz, ny, nx] < 127 and regiao[nz, ny, nx] == 0:
                regiao[nz, ny, nx] = 255
                lista.append((nz, ny, nx))
segm = np.where(regiao == 255)
if len(segm[0]) > 0:
    centroide_z = int(np.mean(segm[0]))
    centroide_y = int(np.mean(segm[1]))
    centroide_x = int(np.mean(segm[2]))
else:
    print("Nenhuma região foi segmentada")
    centroide_z = 0
result = cv2.cvtColor(volume[centroide_z], cv2.COLOR_GRAY2BGR)
# Pintar região segmentada de Azul
result[regiao[centroide_z] == 255] = [255, 0, 0]
# Centroide verde
cv2.circle(result, (centroide_x, centroide_y), 10, [0, 255, 0], -1)
# Pegar a imagem 2d da region growing
region = regiao[centroide_z]
cv2.imshow("Resultado", result)
cv2.imshow("Growing", region)
cv2.waitKey(0)
cv2.destroyAllWindows()
