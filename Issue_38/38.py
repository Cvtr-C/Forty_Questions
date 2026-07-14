import cv2

img = cv2.imread("arara.jpg", 0)
limiar, binario = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
estruturante = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 1))
for i in range(1, 6):
    # Anchor é onde ele vai ficar "preso"
    dilatação = cv2.dilate(binario, estruturante, anchor=(0, 0), iterations=i)
    cv2.imshow(f"dilatação número: {i}", dilatação)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
