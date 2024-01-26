import random

import cv2
img=cv2.imread("canny.jpg",1)

print(img)
print(type(img))
print(img.shape)
# print(img[1000])

for i in range(100):
    for j in range(img.shape[0]):
        img[i][j]=[random.randint(0,255), random.randint(0,255), random.randint(0,255)]

cv2.imshow("anh",img)
cv2.waitKeyEx()