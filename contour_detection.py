import cv2 as cv
import numpy as np
import opencv_utils as cv_utils
from hsv_tuner_class import HSVTuner

############
# Constants
############
YELLOW = ((17, 25, 25), (35, 255, 255)) # The HSV range for the color yellow
RED = ((0, 60, 23), (10, 255, 255))  # The HSV range for the color red
GUI = HSVTuner()
CAMERA_INDEX = 2 # configures which camera is used for contour detection
# NOTE: 0 is the default computer webcam, but you may need to use other indecies
############
# Methods
############
'''
Given an image, return the new image with drawn contours around objects of a specific color

Format
color: ((), ()) containing lower and upper HSVs
contains_center: should contours be labeled with a center?
get_max: should only the max contour + center be drawn?
'''
def get_contoured_image(image, color, contains_center=False, get_max=True):
   contours = cv_utils.find_contours(image, color[0], color[1], min_size=0)
   if get_max: # draws one contour if we only need largest one
      cv_utils.draw_contours(image, [cv_utils.get_largest_contour(contours)], (0, 255, 0))
   else: # draws all contours
      cv_utils.draw_contours(image, contours, (0, 255, 0))
   if contains_center:
      center = cv_utils.get_contour_center(cv_utils.get_largest_contour(contours))
      cv_utils.draw_circle(frame, center, (0, 255, 0)) # draws circle in green color 
   return image


if __name__ == '__main__':

   print("Starting contour detection...")
   # initializing camera, camera window, and GUI window
   camera = cv.VideoCapture(CAMERA_INDEX)
   
   while True:
      hasFrame, frame = camera.read()
      if hasFrame:
         # finds mask given the lower and upper bounds (first and second tuple in 'range' respectively)
         mask = cv_utils.find_mask(frame, 
                                   GUI.get_range()[0], 
                                   GUI.get_range()[1]) 
         GUI.run()
         cv_utils.show_image(mask)
      else:
         break
   # camera.release()
   # camera.destroyAllWindows() 
   