import cv2 as cv

def readImage(path):
    img=cv.imread(path)
    resizedImg = rescaleFrame(img)
    
    # gray
    gray = cv.cvtColor(resizedImg, cv.COLOR_BGR2GRAY)
    
    # blur
    blur = cv.GaussianBlur(resizedImg, (7,7), cv.BORDER_DEFAULT)
        
    # edge cascade
    canny = cv.Canny(img, 125, 175)
        
    # dilating the image
    dilated = cv.dilate(canny, (3,3), iterations=5)
        
    # erosion
    eroded = cv.erode(canny, (4,4), iterations=5)
    
    # resizing
    resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
    
    # cropping
    cropped = img[50:200, 200:400]
    
    cv.imshow("Image", resizedImg)
    cv.imshow('Gray', gray)   
    cv.imshow("Blur", blur)
    cv.imshow('Canny Edges', canny)
    cv.imshow('Dilated', dilated)
    cv.imshow("Eroded", eroded)
    cv.imshow('Resized', resized)
    cv.imshow('Cropped', cropped)
    
    cv.moveWindow("Image", 500,300)

def readVideo(path=0):
    """
    This function reads a video from a specified path or from the default camera.
    
    :param path: The path parameter is the path to the video file that you want to read. If no path is
    provided, the default value of 0 is used, which means that the video will be read from the default
    camera device, defaults to 0 (optional)
    """
    capture = cv.VideoCapture(path)
    
    while True:
        isTrue, frame = capture.read()
        frame_resized = rescaleFrame(frame)
        
        cv.imshow('Video', frame_resized)

        if cv.waitKey(20) & 0xFF==ord('d'): # if letter d is pressed, stop video
            break
    
    capture.release()
    cv.destroyAllWindows()
    
def rescaleFrame(frame, scale=0.75):
    """
    The function rescales a given frame by a specified scale factor using OpenCV's resize function.
    
    :param frame: The input frame that needs to be resized
    :int scale: The scale parameter is a float value that determines the scaling factor for the input frame.
    """
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# only works for live videos (videos fed from an external camera or webcam)
def changeRes(capture, width, height):
    """
    This function changes the resolution of a video capture object in Python.
    
    :param capture: This is a variable that represents the video capture object. It is used to capture
    frames from a video file or camera
    :param width: The width parameter is the desired width of the video frame in pixels. It is used to
    set the width of the video capture object
    :param height: The height parameter in the changeRes function is used to set the height of the video
    capture frame. It is a numeric value that represents the number of pixels in the vertical direction
    of the frame
    """
    capture.set(3, width)
    capture.set(4, height)

imgPath = "./Resources/Photos/park.jpg"
videoPath = "./Resources/Videos/dog.mp4"
readImage(imgPath)
# readVideo(videoPath)

cv.waitKey(0)