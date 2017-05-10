import cv2
import numpy as np
img=cv2.imread('news.png')
rows,cols,ch=img.shape
pts1=np.float32([[56,65],[368,52],[28,387],[389,390]])
# pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])
pts2=np.float32([[20,20],[300,20],[20,300],[300,300]])
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(200,200))
cv2.imshow('Input',img)
cv2.imshow('Output',dst)
cv2.imwrite('getPer.jpg',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()