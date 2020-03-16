import libsonyapi
from libsonyapi import Actions
import requests
import time
s=time.time()
camera = libsonyapi.Camera() # create camera instance
camera_info = camera.info() # get camera camera_info
print(camera_info)
i=0
print(camera.name) # print name of camera
print(camera.api_version) # print api version of camera
while True:
    i+=1
    s=time.time()
    time.sleep(2)
    a=camera.do(Actions.actTakePicture)
    #print(a['result']) # take a picture

    #fNumber = camera.do(Actions.getFNumber)
    #print(fNumber) # prints response from camera, which includes f-number
    image_url=a['result'][0][0]
    r = requests.get(image_url)
    #camera.do(Actions.setFNumber, '5') # set fnumber to 5
    with open("image "+str(i)+".jpg",'wb') as f: 
    
        # Saving received content as a png file in 
        # binary format 
    
        # write the contents of the response (r.content) 
        # to a new file in binary mode. 
        f.write(r.content)
    e=time.time()
    print(e-s)
