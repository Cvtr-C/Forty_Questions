import cv2
import numpy as np

img = cv2.imread("arara.jpg", 0)
# Limiarização OTSU
limiar, binario = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
mascara = np.ones((3, 3), dtype=np.uint8)
# Teste de diferença de números de dilatação
for i in range(1, 6):
    dilatação = cv2.dilate(binario, mascara, iterations=i)
    nome = f"Dilatação número: {i}"
    cv2.imshow(nome, dilatação)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
