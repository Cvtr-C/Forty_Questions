import cv2

img = cv2.imread("arara.jpg", 0)
laplaciano = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
laplaciano8u = cv2.convertScaleAbs(laplaciano)
laplaciano_equalizado = cv2.equalizeHist(laplaciano8u)
cv2.imshow("imagem", img)
cv2.imshow("laplaciano", laplaciano8u)
cv2.imshow("laplaciano equalizado", laplaciano_equalizado)
cv2.imwrite("imagem_cinza.jpg", img)
cv2.imwrite("imagem_laplaciano.jpg", laplaciano8u)
cv2.imwrite("imagem_laplaciano_equalizado.jpg", laplaciano_equalizado)
cv2.waitKey(0)
cv2.destroyAllWindows()
