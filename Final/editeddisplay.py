import cv2
import numpy as np
import dominantcolor
from PIL import Image
import greendetect
import cropmin
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
import time
from keras.models import load_model
'''model = load_model('shapesmodel.h5')
a=[]
b=[]
img_size = 60
dimData = np.prod([img_size, img_size]) 
start=time.time()
img2 = cv2.imread("593.png")
imgc=img2.copy()
img1=greendetect.maskgreen(img2)
img3=greendetect.unmaskgreen(img2)
cv2.imshow('img2',img3)
cv2.waitKey(0)
img=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
bilateral=cv2.bilateralFilter(img,15,15,15)
#$edgesbilateral=cv2.Canny(bilateral,170,170)
ret, thresh = cv2.threshold(bilateral, 130, 255, 0)
contours,h=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for i in contours: 
    b.append(cv2.contourArea(i))    
for i in contours: 
    if cv2.contourArea(i)>40 and cv2.contourArea(i)<90:
        a.append(i) 
a=np.asarray(a) 
kernel=np.ones((2,2),np.uint8) 
contours1=cv2.drawContours(img,a, -1, (0,255,0),thickness=cv2.FILLED)

for c in a:   
    x,y,w,h = cv2.boundingRect(c)
    coords=(x,y)
    area = cv2.contourArea(c)
    cv2.rectangle(contours1,(x,y),(x+w,y+h),(0,255,0),2)
    #rect = cv2.minAreaRect(i)
    #c=cropmin.crop_minAreaRect(img1,rect)
    #cv2.imshow("idk",c)
    cv2.fillPoly(img3, pts =[c], color=(0,0,0))   
    roi=img3[y-15:y+h+15,x-15:x+w+10]
    #cv2.imshow('img',roi)
    #cv2.waitKey(0)  
    roi=cv2.resize(roi,(60,60))
    mask=roi.reshape(1,dimData) 
    prediction = model.predict(mask.reshape(1,dimData))[0].tolist()
    #create text --> go from categorical labels to the word for the shape.
    text=''
    p_val, th = .25, .5
    if max(prediction)> p_val:
        if prediction[0]>p_val and prediction[0]==max(prediction): text, th =  'triangle', prediction[0]
        if prediction[1]>p_val and prediction[1]==max(prediction): text, th =  'star', prediction[1] 
        if prediction[2]>p_val and prediction[2]==max(prediction): text, th =  'square', prediction[2]
        if prediction[3]>p_val and prediction[3]==max(prediction): text, th =  'circle', prediction[3]
                        
    #draw the contour
    cv2.drawContours(imgc, c, -1, (0,0,255), 1)

    #draw the text
    org, font, color = (coords[0], coords[1]+int(area/400)), cv2.FONT_HERSHEY_SIMPLEX, (0,0,255)
    cv2.putText(imgc, text, org, font, int(2.2*area/15000), color, int(6*th), cv2.LINE_AA)
    #paste the black and white image onto the source image (picture in picture)            
    if text=='':pass
    if text!='': imgc[imgc.shape[0]-200:imgc.shape[0], img.shape[1]-200:img.shape[1]] = cv2.cvtColor(cv2.resize(roi, (200,200)), cv2.COLOR_GRAY2BGR)
    cv2.imshow(text, cv2.resize(imgc, (640, 480))) #expect 2 frames per second
    cv2.waitKey(0)
    end=time.time()
print(end-start)'''
def Shape_pred(img):
        #img=cv2.imread(img)
        model = load_model('shapesmodel.h5')
        img3=greendetect.unmaskgreen(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.ones((1, 1), np.uint8) 
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        #img = cv2.GaussianBlur(img, (9, 9), 0)
        img3 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        img3 = cv2.bitwise_not(img3)
        roi=cv2.resize(img3,(60,60))
        img=cv2.resize(img,(60,60))
        cv2.imshow('ImG',img3)
        cv2.waitKey(0)
        img_size = 60
        text=''
        dimData = np.prod([img_size, img_size])
        mask=roi.reshape(1,dimData) 
        prediction = model.predict(mask.reshape(1,dimData))[0].tolist()
        p_val, th = .25, .5
        if max(prediction)> p_val:
                if prediction[0]>p_val and prediction[0]==max(prediction): text, th =  'triangle', prediction[0]
                if prediction[1]>p_val and prediction[1]==max(prediction): text, th =  'star', prediction[1] 
                if prediction[2]>p_val and prediction[2]==max(prediction): text, th =  'square', prediction[2]
                if prediction[3]>p_val and prediction[3]==max(prediction): text, th =  'circle', prediction[3]
                if prediction[4]>p_val and prediction[4]==max(prediction): text, th =  'semicircle', prediction[4]
                if prediction[5]>p_val and prediction[5]==max(prediction): text, th =  'rectangle', prediction[5]
                if prediction[6]>p_val and prediction[6]==max(prediction): text, th =  'pentagon', prediction[6]
                if prediction[7]>p_val and prediction[7]==max(prediction): text, th =  'hexagon', prediction[7]
        if text=='':pass
        if text!='':
                #print (th)
                return(text)