import cv2 as cv
import numpy as np

def draw(obj, colour, thn, radius=0.0):
    # Rectangle
    rectangle = cv.rectangle(obj, (0,0), (obj.shape[1]//2, obj.shape[0]//2), (0,255,0), thickness=thn)
    
    # Circle
    circle = cv.circle(obj, (obj.shape[1]//2, obj.shape[0]//2), radius, colour, thickness=-1)
    
    # Line
    line = cv.line(obj, (0,0), (obj.shape[1]//2, obj.shape[0]//2), colour, thickness=1)
    
    # Text
    text = cv.putText(obj, 'wagwan bro', (225,150), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 2)
    
    return rectangle, circle, line, text

blank = np.zeros((500, 500, 3), dtype='uint8')

r, c, l, t = draw(blank, (255,0,0), -1, radius=40)
cv.imshow('Window', r)

cv.waitKey(0)