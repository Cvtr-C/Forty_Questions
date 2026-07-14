import cv2
import numpy as np

# Ela começa vazia para futuramente guardar as cordenadas (Y, X)
semente = None


# Define a função callback
def mouse(event, x, y, flags, param):
    global semente  # Alterar variavel fora da função
    # Se o evento foi um click com o botão esquerdo
    if event == cv2.EVENT_LBUTTONDOWN:
        # Armazena as cordenadas (linhas, colunas)
        semente = (y, x)


img = cv2.imread("figura.jpg", 0)
linhas, colunas = img.shape
# Cria uma janela gráfica
cv2.namedWindow("figura")
# Vicula a função mouse a figura
cv2.setMouseCallback("figura", mouse)
while True:
    cv2.imshow("figura", img)
    if semente is not None:
        break
    # Parar se houver algum erro, para isso tem que apertar "q"
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        exit()
# Fecha a figura
cv2.destroyWindow("figura")

regiao = np.zeros((linhas, colunas), dtype=np.uint8)
# Cria uma fila de espera para processar a região
fila = [semente]
# Pinta o pixel da semente de branco
regiao[semente[0], semente[1]] = 255
# Define o movimento Cima, Baixo, Esquerda, Direita
deslocamento = [(-1, 0), (1, 0), (0, -1), (0, 1)]
print("Aguarde, processamento do crescimento da região...")
# Loop interativo até a fila zerar
while len(fila) > 0:
    y_atual, x_atual = fila.pop(0)
    # Varre os 4 vizinhos em cruz ao redor do pixel
    for dy, dx in deslocamento:
        # Calcular as coordenadas exatas dos vizinhos somando os deslocamentos
        y_vizinho = y_atual + dy
        x_vizinho = x_atual + dx
        # Garantir a fronteira, para não sair pelo limite da imagem
        if 0 <= y_vizinho < linhas and 0 <= x_vizinho < colunas:
            # Garante as regras de adesão
            if img[y_vizinho, x_vizinho] < 127 and regiao[y_vizinho, x_vizinho] == 0:
                # Se passar pela regra trasformar em branco
                regiao[y_vizinho, x_vizinho] = 255
                # Adicionar o vizinho a fila para entrar no proximo loop
                fila.append((y_vizinho, x_vizinho))

cv2.imshow("imagem", img)
cv2.imshow("growing", regiao)
cv2.waitKey(0)
cv2.destroyAllWindows()
