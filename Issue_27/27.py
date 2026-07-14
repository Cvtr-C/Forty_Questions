import cv2
import numpy as np

cliques = []
exibição = None


def mouse(event, x, y, flags, parem):
    global cliques, img
    if event == cv2.EVENT_LBUTTONDOWN and len(cliques) < tot:
        cliques.append((y, x))


def crescimento(img, semente, T, rotulo, matriz_rotulo):
    linhas, colunas = img.shape
    fila = [semente]
    matriz_rotulo[semente] = rotulo
    reference = float(img[semente])
    vizinho = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while len(fila) > 0:
        y_atual, x_atual = fila.pop(0)
        for dy, dx in vizinho:
            ny, nx = y_atual + dy, x_atual + dx
            if 0 <= ny < linhas and 0 <= nx < colunas:
                if matriz_rotulo[ny, nx] == 0:
                    vv = float(img[ny, nx])
                    dist = abs(reference - vv)
                    if dist < T:
                        matriz_rotulo[ny, nx] = rotulo
                        fila.append((ny, nx))


img = cv2.imread("img.jpg", 0)
_, binario = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
contornos, _ = cv2.findContours(binario, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
tot = len(contornos)
cv2.namedWindow("figura")
cv2.setMouseCallback("figura", mouse)
while True:
    cv2.imshow("figura", img)
    if len(cliques) == tot:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        exit()
cv2.destroyWindow("figura")
linhas, colunas = img.shape
matriz_rotulos = np.zeros((linhas, colunas), dtype=np.uint8)
T = 50
for r in range(1, tot + 1):
    crescimento(img, cliques[r - 1], T, rotulo=r, matriz_rotulo=matriz_rotulos)
resultado = np.zeros((linhas, colunas, 3), dtype=np.uint8)
np.random.seed(42)
cores = np.random.randint(0, 256, size=(tot + 1, 3), dtype=np.uint8)
for r in range(1, tot + 1):
    resultado[matriz_rotulos == r] = cores[r]
    mask = np.zeros((linhas, colunas), dtype=np.uint8)
    mask[matriz_rotulos == r] = 255
    objeto = mask
    coords = cv2.findNonZero(mask)
    # Recortar subimagens da imagem original
    if coords is not None:
        x, y, w, h = cv2.boundingRect(coords)
        subimagem = objeto[y : y + h, x : x + w]
        cv2.imshow(f"objeto{r}", subimagem)
cv2.imshow("Resultado geral", resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
