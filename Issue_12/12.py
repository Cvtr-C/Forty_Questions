import cv2
import numpy as np

mimg = np.loadtxt("arara.txt", dtype=np.uint8)
cv2.imshow("Arara", mimg)
cv2.imwrite("Arara.jpg", mimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
