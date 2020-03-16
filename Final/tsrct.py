import cv2
import pytesseract
import rotateimg
import numpy as np
import string
import greendetect
from PIL import Image
'''
img = cv2.imread('X.png')
img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#rows,cols = img.shape
#print(rows,cols) 
#M = cv2.getRotationMatrix2D((cols/2,rows/2),0,1)
#img= cv2.warpAffine(img,M,(cols,rows))

# Apply dilation and erosion to remove some noise
kernel = np.ones((2, 2), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

# Apply blur to smooth out the edges
img = cv2.GaussianBlur(img, (5, 5), 0)
# OR explicit beforehand converting
img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
cv2.imshow('img',img) 
cv2.waitKey(0)
config = ("-l eng --oem 1 --psm 10")
result = pytesseract.image_to_string(img,config=config)
#print(pytesseract.image_to_osd(Image.open('X.png')))
print(result)
'''
def orient_tsrct(image,x,y,w,h):
    image=cv2.imread(image)
    for i in range(0,361,30):
        img=rotateimg.subimage(image,(x+w/2,y+h/2),i,w,h)
        img=greendetect.unmaskgreen(img)
        img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rows,cols = img.shape
        # Apply dilation and erosion to remove some noise
        kernel = np.ones((3, 3), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)

        # Apply blur to smooth out the edges
        #img = cv2.GaussianBlur(img, (9, 9), 0)
        # OR explicit beforehand converting
        img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        cv2.imshow('imshow',img)
        cv2.waitKey(0)
        config = ("-l eng --oem 1 --psm 10")
        result = pytesseract.image_to_string(img,config=config)
        c=0
        if result in list(string.ascii_letters):
            c+=1 
            return result,i
        else:
            pass
    if c==0:
        return ('No letter','orientation not applicable')