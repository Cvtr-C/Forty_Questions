import cv2
import numpy as np

img = cv2.imread("arara.jpg", 0)
limiar, binario = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
mascara = np.ones((3, 3), dtype=np.uint8)
# Teste de diferença de número de erosões
for i in range(1, 6):
    erosão = cv2.erode(binario, mascara, iterations=i)
    nome = f"Erosão número: {i}"
    cv2.imshow(nome, erosão)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
