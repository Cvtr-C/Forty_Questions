import cv2
import matplotlib.pyplot as plt
img = cv2.imread("images.jpg", 0)
imgp = cv2.resize(img, (256, 256))
hist = [0] * 256
#contagem dos pixels de cada intensidade que tem na imagem
for linha in imgp:
    for pixel in linha:
        hist[int(pixel)] += 1
#criando o histograma
plt.figure(figsize=(8, 4))
plt.bar(range(256), hist, width=1)
plt.title("Histograma")
plt.xlabel("Intensidade")
plt.ylabel("Quantidade de pixels")
plt.xlim(0, 255)
plt.savefig("histograma.png")