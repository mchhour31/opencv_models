import cv2 as cv
import numpy as np

img = cv.imread('./Resources/Photos/cats.jpg')

# convert from BGR (Blue-Green-Red) colour space to grayscale.
grayScale = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# black image w same dimensions as the input image, img.shape[:2] returns the height and width of the image
# Used to draw contours found in input img
blank = np.zeros(img.shape, dtype='uint8')

# Applies canny edge detection algorithm. 
# Output is a binary img where edges = white pixels and non-edges = black pixels
canny = cv.Canny(img, 125, 175)

# blur = cv.GaussianBlur(grayScale, (5,5), cv.BORDER_DEFAULT)
# blurredCanny = cv.Canny(blur, 125, 175)

# Conditional edge detection using thresholds 
# All pixel values below 125 are set to 0 and all pixel values above 125 are set to 255. 
ret, thresh = cv.threshold(grayScale, 125, 255, cv.THRESH_BINARY) 

# Finds contours (outline) in a binary image. 
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!' )

# Drawing the contours found in the input img on the black image
cv.drawContours(blank, contours, -1, (0,0,255), 1)

cv.imshow('Cats', grayScale)
# cv.imshow('Blurred', blur)
cv.imshow('Canny', canny)
# cv.imshow("Threshold", thresh)
# cv.imshow('Blurred Canny', blurredCanny)
cv.imshow('Contours', blank)

cv.waitKey(0)