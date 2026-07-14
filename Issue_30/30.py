import cv2

img = cv2.imread("img.jpg", 0)
blur = cv2.GaussianBlur(img, (3, 3), 0)
canny = cv2.Canny(
    blur,
    50,
    200,
)
# Encontrar contornos
contorno, hierarquia = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
# Diz quantos objetos tem a partir da contagem de contornos
print(f"Número de objetos = {len(contorno)}")
cv2.imshow("Imagem", img)
cv2.imshow("contorno", canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
