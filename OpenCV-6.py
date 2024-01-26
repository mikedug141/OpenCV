import cv2
import os
import time

cap=cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
