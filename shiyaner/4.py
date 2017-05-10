import cv2
import numpy as np
img=cv2.imread('3.png',0)
img1=cv2.add(img,80)
img2=cv2.subtract(img,80)
cv2.imshow('img',img)
img3=cv2.multiply(img,1.5)
cv2.imshow('img3',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()