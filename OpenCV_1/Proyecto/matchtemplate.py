import cv2
from cv2 import cv
 
template_name = "tmpp.jpg"
image_name = "img.jpg"
 
# Load
needle = cv2.imread(template_name)
haystack = cv2.imread(image_name)

 
# Convert to gray:
needle_g = cv2.cvtColor(needle, cv2.CV_32FC1) 
haystack_g = cv2.cvtColor(haystack, cv2.CV_32FC1) 
 
# Attempt match
d = cv2.matchTemplate(needle_g, haystack_g, cv2.cv.CV_TM_SQDIFF_NORMED)
cv2.imshow('matchTemplate',d)
cv2.imshow('matchTemplate_n',needle_g)
cv2.imshow('matchTemplate_h',haystack_g)
# we want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(d)
 
# Print it, for comparison
print mn
 
# Draw the rectangle
MPx,MPy = mnLoc
 
trows,tcols = needle_g.shape[:2]
 
# Normed methods give better results, ie matchvalue = [1,3,5], others sometimes shows errors
cv2.rectangle(haystack, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)
 
cv2.imshow('output',haystack)
 
cv2.waitKey(0)
import sys
sys.exit(0)