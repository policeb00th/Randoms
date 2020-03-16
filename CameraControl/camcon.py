import libsonyapi
from libsonyapi import Actions
import requests
import time
s=time.time()
camera = libsonyapi.Camera() # create camera instance
camera_info = camera.info() # get camera camera_info
print(camera_info)

print(camera.name) # print name of camera
print(camera.api_version) # print api version of camera
a=camera.do(Actions.actZoom,["in","start"])
time.sleep(1.6)
camera.do(Actions.actZoom,["in","stop"])
print(a)    