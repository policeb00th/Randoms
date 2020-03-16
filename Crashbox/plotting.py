'''# import gmplot package
import gmplot
latitude_list = [ 12.968088,12.968025, 12.968067]
longitude_list = [ 79.155943, 79.155963, 79.155668 ]
gmap = gmplot.GoogleMapPlotter(12.968067, 79.155668, 11)
gmap.scatter( latitude_list, longitude_list, '# FF0000', size = 40, marker = False)
# polygon method Draw a polygon with
# the help of coordinates
gmap.polygon(latitude_list, longitude_list, color = 'cornflowerblue')   
gmap.apikey="AIzaSyC8KzOoic-qhW0TJYuWS17AdI7MIvH8l24"
gmap.draw( "/home/diptanshu/Desktop/abc.html" )

'''
import gmplot
import numpy as np 
import pandas as pd 
from sklearn.cluster import MeanShift 
from sklearn.datasets.samples_generator import make_blobs 
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D 
   
# We will be using the make_blobs method 
# in order to generate our own data. 

clusters = [[12.968069, 79.155871], [12.968123, 79.154541], [12.967411, 79.158666] ]
  
X, _ = make_blobs(n_samples = 70, centers = clusters, 
                                   cluster_std = 0.0001) 
   
# After training the model, We store the 
# coordinates for the cluster centers 
ms = MeanShift() 
ms.fit(X) 
cluster_centers = ms.cluster_centers_ 
from sklearn.externals import joblib
joblib.dump(ms, 'model.joblib')
knn_from_joblib = joblib.load('model.joblib')   
#print(knn_from_joblib.cluster_centers_)
print(cluster_centers[knn_from_joblib.predict([[12.967474, 79.158237]])]) 
# Finally We plot the data points 
# and centroids in a 3D graph. 
fig = plt.figure() 
  
ax = fig.add_subplot(111) 
  
ax.scatter(X[:, 0], X[:, 1], marker ='o') 
  
ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], marker ='x', color ='red', 
           s = 300, linewidth = 5, zorder = 10) 
  
plt.show() 
#print(cluster_centers)
gmap = gmplot.GoogleMapPlotter(12.968067, 79.155668, 20)
gmap.scatter( X[:,0],X[:,1], '#FF0000',size = 5, marker = False )
gmap.apikey="AIzaSyC8KzOoic-qhW0TJYuWS17AdI7MIvH8l24"
gmap.draw( "/home/diptanshu/Desktop/abc.html" )
