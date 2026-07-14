import cv2
import numpy as np

img = cv2.imread("figura.jpg", 0)
linhas, colunas = img.shape
# Definir a semente no opencv e numpy (Y, X)
Semente = (120, 160)
região = np.zeros((linhas, colunas), dtype=np.uint8)
# Fila de espera para marcar os vizinhos
fila = [Semente]
# Marcar a própria semente
região[Semente[0], Semente[1]] = 255
# Definição dos vizinhos (Cima, Baixo, Esquerda, Direita)
deslocamentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
print("Aguarde, processando crescimento de região...")
# Loop interativo até a fila esvaziar
while len(fila) > 0:
    # Pega o proximo vizinho da fila para ver os vizinhos
    y_atual, x_atual = fila.pop(0)
    # Verifica os 4 vizinhos
    for dy, dx in deslocamentos:
        y_vizinho = y_atual + dy
        x_vizinho = x_atual + dx
        # Garantir que os vizinhos não estão fora dos limites 340x240
        if 0 <= y_vizinho < linhas and 0 <= x_vizinho < colunas:
            # Regra de adesão: Tom de cinza < 127 E ainda não foi adicionado a região
            if img[y_vizinho, x_vizinho] < 127 and região[y_vizinho, x_vizinho] == 0:
                # Agrega os vizinhos a região
                região[y_vizinho, x_vizinho] = 255
                # Adiciona o vizinho a fila para expandir a partir dele
                fila.append((y_vizinho, x_vizinho))
cv2.imshow("Imagem", img)
cv2.imshow("Região growing", região)
cv2.imwrite("region_growing.jpg", região)
cv2.waitKey(0)
cv2.destroyAllWindows()
