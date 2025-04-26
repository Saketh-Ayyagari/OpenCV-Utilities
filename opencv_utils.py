"""
Saketh Ayyagari
Helper Methods for OpenCV Functions.
"""
import cv2 as cv
import numpy as np
"""
Displying image
"""
def show_image(image):
   window_name = "Camera"
   window = cv.namedWindow(window_name, cv.WINDOW_NORMAL)

   cv.imshow(window_name, image)
   cv.waitKey(1)
"""
Given an image and HSV ranges, return a list of contours
"""
def find_contours(image, low: tuple, high: tuple, min_size=30)->list:
   mask = find_mask(image, low, high, min_size)
   # finding and filtering contours based on minimum size
   contours, _ = cv.findContours(mask, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
   filtered_contours = [c for c in contours if cv.contourArea(c) >= min_size]
   
   return filtered_contours
"""
Returns mask (black and white thresholding) of an image after hsv transformation
"""
def find_mask(image, low: tuple, high: tuple, min_size=30):
   # convert RGB image to HSV format
   # note the format is BGR despite the output of the camera being RGB format
   hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
   mask = cv.inRange(hsv, low, high) # thresholding image
   
   return mask
"""
Draws multiple contours given list or individual contour given single contour 
"""
def draw_contours(image, contours, color: tuple): # "color" tuple is in RGB format
   if type(contours) != list: # if the "contours" parameter is not a list (a single contour)
      cv.drawContours(image, [contours], -1, color, 3)
   elif len(contours) > 0: # if the "contours" parameter is a list w/ at least 1 element
      cv.drawContours(image, contours, -1, color, 3)
"""
Gets largest contour in size given list of contours
"""
def get_largest_contour(contours):
   if len(contours) > 0:
      max_contour = contours[0]
      max_contour_area = cv.contourArea(max_contour)
      for c in contours:
         if cv.contourArea(c) > max_contour_area:
            max_contour_area = cv.contourArea(c)
            max_contour = c
      return max_contour
   return None
"""
Finds the center of a contour given a specific contour
Format of the center is (x, y), where x is the horizontal axis and y is the vertical axis
(OPPOSITE FROM ROW-MAJOR INDEXING IN 2D ARRAYS)
"""
def get_contour_center(contour)->tuple:
   M = cv.moments(contour)
   if M['m00'] != 0:
      cx = int(M['m10']/M['m00'])
      cy = int(M['m01']/M['m00'])
      return (cx, cy)
   return None
"""
Draws a circle at a point
"""
def draw_circle(image, point: tuple, color: tuple, text=""):
      if point is not None:
         cv.circle(image, point, 7, color, -1)
         cv.putText(image, text, (point[0] - 20, point[1] - 20),
                     cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)