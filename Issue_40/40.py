import cv2

img = cv2.imread("arara.jpg", 0)
limiar, binario = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
for i in range(1, 6):
    erosão = cv2.erode(binario, estruturante, anchor=(0, 0), iterations=i)
    nome = f"Erosão número: {i}"
    cv2.imshow(nome, erosão)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
