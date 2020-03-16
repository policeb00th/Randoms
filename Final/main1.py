#import predict
import argparse
import editeddisplay
import cv2
import trial2
import tsrct
import mser2
parser = argparse.ArgumentParser()
parser.add_argument('-i', type = str, required = True, help = "Image Path")
opt = parser.parse_args()
ret=mser2.blob_det(opt.i)
for j in ret:
    x,y,w,h,image,img1=j[0],j[1],j[2],j[3],j[4],j[5]
    result,l=tsrct.orient_tsrct(opt.i,x,y,w,h)
    #predict.predict(image, 'CharSave/awesome_model-99000')
    z=editeddisplay.Shape_pred(image)
    a,b=trial2.coldet(img1)
    print('letter: '+str(result)+'\nshape: '+str(z)+'\ncolors: '+str(a)+','+str(b)+'\norientation(degrees)'+str(l)+'\nPixel coordinates:'+str(x)+','+str(y))

