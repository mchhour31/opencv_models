import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/park.jpg')
cv.imshow('Park', img)

def translate(img, x, y):
    """
    This function translates an image by a given amount in the x and y directions using an affine
    transformation. Affine transformations preserve the parallelism of lines, this ensures objects in 2D/3D remain unchanged 
    during a given transformation.
    
    :param img: The input image that needs to be translated
    :param x: The amount of horizontal translation (in pixels) to be applied to the image. A positive
    value of x will shift the image to the right, while a negative value of x will shift the image to
    the left
    :param y: The y parameter in the translate function is the amount of vertical translation (in
    pixels) that will be applied to the input image. A positive value of y will shift the image
    downwards, while a negative value of y will shift the image upwards
    :return: a translated image, where the original image has been shifted by x pixels horizontally and
    y pixels vertically using an affine transformation matrix.
    """
    xShift = np.float32([[1,0,x],[0,1,y]])
    yShift = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, xShift, yShift)

# rotation
def rotation(img, angle, rotPoint=None):
    """
    This function rotates an image by a specified angle around a specified rotation point.
    
    :param img: The input image that needs to be rotated
    :param angle: The angle parameter is the amount of rotation in degrees that the image will be
    rotated by. A positive angle value will rotate the image clockwise, while a negative angle value
    will rotate the image counterclockwise
    :param rotPoint: The point around which the image will be rotated. If not specified, the center of
    the image will be used as the rotation point
    :return: The function `rotation` returns the rotated image using the OpenCV function `warpAffine`.
    """
    (height, width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimensions)

translated = translate(img, -100, 100)
rotated = rotation(img, -15)
resize = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
flip = cv.flip(img, 1)
cropped = img[200:400, 300:600]

cv.imshow("Rotated", rotated)
cv.imshow("Translated", translated)
cv.imshow("Resized", resize)
cv.imshow("Flipped", flip)
cv.imshow("Cropped", cropped)

cv.waitKey(0)