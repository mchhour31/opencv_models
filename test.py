import cv2 as cv
import os.path

def readImage(path):
    img=cv.imread(path)
    resizedImg = rescaleFrame(img, scale=0.5)
    cv.imshow('Resized Image', resizedImg)
    
    cv.imshow('Cat', img)
    cv.moveWindow("Cat", 500,300)
    cv.moveWindow("Resized Image", 800,300, 1)

def readVideo(path):
    capture = cv.VideoCapture(path)
    
    while True:
        isTrue, frame = capture.read()

        frame_resized = rescaleFrame(frame, scale=0.3)
        
        cv.imshow('Video', frame)
        cv.imshow('Video Resized', frame_resized)

        if cv.waitKey(20) & 0xFF==ord('d'): # if letter d is pressed, stop video
            break
    
    capture.release()
    cv.destroyAllWindows()

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# only works for live videos (videos fed from an external camera or webcam)
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

imgPath = "./Resources/Photos/cat.jpg"
videoPath = "./Resources/Videos/dog.mp4"
readImage(imgPath)

cv.waitKey(0)