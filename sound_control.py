import cv2
import mediapipe as mp 
import matplotlib.pyplot as plt
from math import *
from subprocess import call 

plt.ion()

cam = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

x1,x2,y1,y2 = [0,0,0,0]
while True:
    success, frame = cam.read()
    frame = cv2.flip(frame,1)
    imageRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    h,w = frame.shape[:2]
    dist = 0.0001
    x1, y1 = x1*w, y1*h
    try:
        cv2.circle(frame,(int(x1),int(y1)),10,[0,0,255])
        cv2.imshow('image',frame)
        cv2.waitKey(1)
    except OverflowError:
        pass
    if results.multi_hand_landmarks:
        if len(results.multi_hand_landmarks) == 1:
                hand1 = results.multi_hand_landmarks[0]
                x1,y1 = hand1.landmark[8].x, hand1.landmark[8].y
                call(["amixer", "-D", "pulse", "sset", "Master", f"{(1-y1)*100}%"])