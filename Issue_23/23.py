import cv2
import numpy as np
import matplotlib.pyplot as plt

semente = None


# Pega as dimensões do pixel que a pessoa clicar
def mouse(event, x, y, flags, param):
    global semente
    if event == cv2.EVENT_LBUTTONDOWN:
        semente = (y, x)


img = cv2.imread("images.jpeg", 0)
linhas, colunas = img.shape
cv2.namedWindow("figura")
cv2.setMouseCallback("figura", mouse)
while True:
    cv2.imshow("figura", img)
    if semente is not None:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        exit()
cv2.destroyWindow("figura")
profundidade = 10
volume = np.zeros((profundidade, linhas, colunas), dtype=np.uint8)
for z in range(profundidade):
    volume[z] = img.copy()
# Transforma a semente em 3D
semente = (5, semente[0], semente[1])
# Pega o valor que corresponde ao pixel que a pessoa clicou
Vs = volume[semente]
regiao = np.zeros_like(volume, dtype=np.uint8)
lista = [semente]
regiao[semente] = 255
# Limiar para limitar o nivel de diferença que o pixel vizinho pode ter em relação a semente para ser processado
T = 90
vizinho = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
while len(lista) > 0:
    z_atual, y_atual, x_atual = lista.pop(0)
    for dz, dy, dx in vizinho:
        nz, ny, nx = z_atual + dz, y_atual + dy, x_atual + dx
        if 0 <= nz < profundidade and 0 <= ny < linhas and 0 <= nx < colunas:
            # Verifica se o vizinho já foi processado
            if regiao[nz, ny, nx] == 0:
                # Pegunta se a diferença entre o vizinho e o pixel semente são menores que o limiar, se for menor ele é semelhante o suficiente se comparado a outros pixels
                if abs(int(volume[nz, ny, nx]) - int(Vs)) < T:
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
result[regiao[centroide_z] == 255] = [255, 0, 0]
cv2.circle(result, (centroide_x, centroide_y), 10, [0, 255, 0], -1)
region = regiao[centroide_z]
cv2.imshow("Resultado", result)
cv2.imshow("Region growing", region)
cv2.waitKey(0)
cv2.destroyAllWindows()
