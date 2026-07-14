import cv2
from matplotlib import pyplot as plt

img = cv2.imread("arara.jpg", 0)
plt.hist(img.ravel(), bins=256, range=[0, 256])
plt.title("Histograma")
plt.xlabel("Intensidade")
plt.ylabel("Quantidade de pixels")
plt.savefig("histograma.jpg")
plt.close()
cv2.imwrite("Arara.jpg", img)

img_equalizada = cv2.equalizeHist(img)
plt.hist(img_equalizada.ravel(), bins=256, range=[0, 256])
plt.title("Histograma_Equalizado")
plt.xlabel("Intensidade")
plt.ylabel("Quantidade de pixels")
plt.savefig("histograma_equalizado.jpg")
plt.close()
cv2.imwrite("Arara_equalizada.jpg", img_equalizada)
