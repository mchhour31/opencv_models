import cv2 as cv
import os.path

def readImage(path):
    img=cv.imread(path)
    cv.imshow('Cat', img)
    cv.moveWindow("Cat", 500,300)

def readVideo(path):
    capture = cv.VideoCapture(0)
    
    while True:
        isTrue, frame = capture.read()
        cv.imshow('Video', frame)

        if cv.waitKey(20) & 0xFF==ord('d'): # if letter d is pressed, stop video
            break
    
    capture.release()
    cv.destroyAllWindows()


imgPath = "./Resources/Photos/cat.jpg"
videoPath = "./Resources/Videos/dog.mp4"
readImage(imgPath)
readVideo(videoPath)
cv.waitKey(0)