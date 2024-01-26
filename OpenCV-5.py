import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

# ve line
    img=cv2.line(frame,(0,0),(width,height),(0,0,0),5)
    img=cv2.line(frame,(0,height),(width,0),(255,0,123),3)

# ve chu nhat
    img=cv2.rectangle(frame,(100,100),(200,400),(70,50,80,2),5)

# ve hinh tron
    img=cv2.circle(frame,(150,150),120,(100,125,25),5)

# chen text
    font=cv2.FONT_HERSHEY_COMPLEX
    img=cv2.putText(frame,"NguyenDucViet",(10,height-10),font,1,5)




    cv2.imshow("win", img)
    if cv2.waitKeyEx(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()