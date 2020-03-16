import cv2
import numpy as np

def subimage(image, center, theta, width, height):

   ''' 
   Rotates OpenCV image around center with angle theta (in deg)
   then crops the image according to width and height.
   '''

   # Uncomment for theta in radians
   #theta *= 180/np.pi
   shape = ( image.shape[1], image.shape[0] ) # cv2.warpAffine expects shape in (length, height)

   matrix = cv2.getRotationMatrix2D( center=center, angle=theta, scale=1 )
   image = cv2.warpAffine( src=image, M=matrix, dsize=shape )
   

   x = int( center[0] - width/2  )
   y = int( center[1] - height/2 )
   image = image[ y-5:y+height+5, x-5:x+width+5 ]
   return image