import cv2

#doc anh

img=cv2.imread("me.jpg",1)

#resize anh

# img=cv2.resize(img,(1800,1960))
img=cv2.resize(img,(0,0),fx=0.3,fy=0.3)
#xuat anh
cv2.imshow("window",img)
k=cv2.waitKeyEx()
print(k)
if k==ord("s"):
    cv2.imwrite("new.jpg",img)


