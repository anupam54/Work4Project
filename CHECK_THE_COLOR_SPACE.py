import cv2
nemo = cv2.imread('./Images/nemo0.jpg')
c = cv2.cvtColor(nemo, cv2.COLOR_RGB2BGR)
cv2.imshow("Original Image",c)
cv2.waitKey(0)
cv2.destroyAllWindows()