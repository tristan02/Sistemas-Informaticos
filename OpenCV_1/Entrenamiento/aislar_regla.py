import cv2
import numpy as np


def nothing():
    cv2.imshow("Canny",edges)




for i in range(100):
    path = 'ima/img (' + str(i+1) + ').jpg'
    img = cv2.imread(path,0)
    edges = cv2.Canny(img,250,500)
    cv2.imshow("Original",img)
    cv2.imshow("Canny",edges)
    
    u1 = cv2.getTrackbarPos("Umbral1", "umbrales")
    u2 = cv2.getTrackbarPos("Umbral2", "umbrales")
    
    if cv2.waitKey(1) == 27:
        cv2.imwrite("canny.jpg", edges)
        break

cv2.destroyAllWindows()