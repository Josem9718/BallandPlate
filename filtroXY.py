# Algoritmo de Filtrado y Posicionamiento
# Miguel Benavides Jimenez
# Mayo 2020


import cv2
import numpy as np

cap = cv2.VideoCapture(0)
kernel = np.ones((5,5),np.uint8)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_orang = np.array([10,150,150]) 
    upper_orang = np.array([30,255,255])

    mask = cv2.inRange(hsv, lower_orang, upper_orang)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN,kernel)
    x,y,w,h = cv2.boundingRect(opening)
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.circle(frame,(x+w/2,y+h/2),5,(255,0,0),-1)#
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    x=(x+w/2)-320; 
    cv2.putText(frame,str(x),(50,470), font, 0.8, (200,255,155), 2, cv2.LINE_AA)
    cv2.putText(frame,'X=',(10,470), font, 0.8, (0,0,255), 2, cv2.LINE_AA)
    y=(y+h/2)-220;
    cv2.putText(frame,str(y),(170,470), font, 0.8, (200,255,155), 2, cv2.LINE_AA)
    cv2.putText(frame,'Y=',(130,470), font, 0.8, (0,0,255), 2, cv2.LINE_AA)

    cv2.imshow('JOSE MIGUEL',frame)
    cv2.imshow('mask', opening)
   

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
        
cv2.destroyAllWindows
cap.release()