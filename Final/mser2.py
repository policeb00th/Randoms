import cv2
import matplotlib.pyplot as plt
def blob_det(img):
    img = cv2.imread(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img1=img.copy()
    ret=[]


    mser = cv2.MSER_create(_min_area=50)
    mser = cv2.MSER_create(_max_area = 450)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    regions, boxes = mser.detectRegions(gray)

    for box in boxes:
        x, y, w, h = box
        #cv2.rectangle(img, (x,y),(x+w, y+h), (255, 0, 0), 3)
        ret.append((x,y,w,h,img1[y-5:y+h+5,x-5:x+w+5],img1[y:y+h,x:x+w]))
    return ret


