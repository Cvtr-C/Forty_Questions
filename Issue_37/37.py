import cv2
import numpy as np

img = cv2.imread("arara.jpg", 0)
limiar, binario = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# Criar um elemento estruturante
estruture = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
for i in range(1, 6):
    dilatação = cv2.dilate(binario, estruture, iterations=i)
    nome = f"Número da dilatação: {i}"
    cv2.imshow(nome, dilatação)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
