import cv2
import numpy as np

semente = None
imagem_ori = None


def mouse(event, x, y, flags, param):
    global semente, imagem_ori
    if event == cv2.EVENT_LBUTTONDOWN:
        semente = (y, x)


def crescimentoBGR(img, semente, T):
    h, w, _ = img.shape
    segm = np.zeros((h, w), dtype=np.uint8)
    fila = [semente]
    segm[semente] = 255
    # Cor de referencia da semente (float 64 para evitar overflow)
    cor_referencia = np.array(img[semente], np.float64)
    # Vizinhança de 8 conectivos
    vizinho = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    while len(fila) > 0:
        y_atual, x_atual = fila.pop(0)
        for dy, dx in vizinho:
            ny, nx = y_atual + dy, x_atual + dx
            if 0 <= ny < h and 0 <= nx < w:
                if segm[ny, nx] == 0:
                    cor_vizinho = np.array(img[ny, nx], np.float64)
                    # Regra de adesão: Distância euclidiana nos canais B, G, R
                    dist = np.sqrt(np.sum((cor_referencia - cor_vizinho) ** 2))
                    if dist < T:
                        segm[ny, nx] = 255
                        fila.append((ny, nx))
    return segm


img = cv2.imread("images.jpeg")
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
# Limiar de tolerância de cor
T = 60
mask = crescimentoBGR(img, semente, T)
# Aplica a mascara no objeto para destacar o objeto
resultado = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Regiao", mask)
cv2.imshow("segmentado", resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()
