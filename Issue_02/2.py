import cv2

img = cv2.imread("arara.jpg", 0)
cv2.imshow("arara", img)
cv2.imwrite("Arara.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
