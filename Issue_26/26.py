import cv2
import numpy as np

cliques = []  # Guardar sementes
exibição = None


def mouse(event, x, y, flags, parem):
    global cliques, img
    # Captura até tot cliques com o botão esquerdo
    if event == cv2.EVENT_LBUTTONDOWN and len(cliques) < tot:
        cliques.append((y, x))


def crescimento(img, semente, T, rotulo, matriz_rotulo):
    linhas, colunas = img.shape
    fila = [semente]
    # Define rótulo da semente  na matriz de controle
    matriz_rotulo[semente] = rotulo
    # Valor de intensidade de cinza
    reference = float(img[semente])
    vizinho = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while len(fila) > 0:
        y_atual, x_atual = fila.pop(0)
        for dy, dx in vizinho:
            ny, nx = y_atual + dy, x_atual + dx
            if 0 <= ny < linhas and 0 <= nx < colunas:
                # So processar se não tiver rótulo
                if matriz_rotulo[ny, nx] == 0:
                    vv = float(img[ny, nx])
                    # Regra de adesão: diferença absoluta em tons de cinza
                    dist = abs(reference - vv)
                    if dist < T:
                        matriz_rotulo[ny, nx] = rotulo
                        fila.append((ny, nx))


img = cv2.imread("img.jpg", 0)
# Tranforma a imagem em binario
_, binario = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# Proucura contornos variações bruscas do preto para o branco
contornos, _ = cv2.findContours(binario, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Contagem do número de objetos detectados na foto
tot = len(contornos)
cv2.namedWindow("imagem")
cv2.setMouseCallback("imagem", mouse)
# Espera tot cliques do úsuario
while True:
    cv2.imshow("imagem", img)
    # Se tiver os tot cliques prosseguir
    if len(cliques) == tot:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        exit()
cv2.destroyWindow("imagem")
linhas, colunas = img.shape
# Ela guardara os valores de 1 à tot para cada região encontrada
matriz_rotulos = np.zeros((linhas, colunas), dtype=np.uint8)
# Limiar de tolerância (como o fundo é branco[255] e o objeto é preto[0])
T = 50
# Cria tot sementes e aplica no crescimento
for n in range(1, tot + 1):
    crescimento(img, cliques[(n - 1)], T, rotulo=(n), matriz_rotulo=matriz_rotulos)
# Inicializa uma imagem completamente preta
resultado = np.zeros((linhas, colunas, 3), dtype=np.uint8)
# Cores geradas semi-automaticas
np.random.seed(42)
cores = np.random.randint(0, 256, size=(tot + 1, 3), dtype=np.uint8)
for r in range(1, tot + 1):
    # Resultado para pintar os objetos na foto
    resultado[matriz_rotulos == r] = cores[r]
cv2.imshow("Resultado", resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
