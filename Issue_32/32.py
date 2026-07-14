import cv2

img = cv2.imread("img.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
canny = cv2.Canny(blur, 50, 200)
contorno, hierarquia = cv2.findContours(
    canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
print(f"Tem {len(contorno)} objetos")
for contor in contorno:
    x, y, w, h = cv2.boundingRect(contor)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    # Area do objeto por contagem de pontos
    area = cv2.contourArea(contor)
    print(f"O objeto tem área {area}")
cv2.imshow("Contornos", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
