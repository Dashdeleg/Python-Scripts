"""
Sample code for converting HDF5 stack of images into avi movie
    .. last edit: 3/5/2018
    .. section author:: Dashdeleg Baasanjav <d.baasanjav@uu.nl>
"""

import numpy as np
import matplotlib.pyplot as plt
import h5py
import cv2

dir = 'F:/Data/2017-06-07/'
filepath = dir+'Blue10mW30AuParticle.hdf5'
f = h5py.File(filepath, 'r') # open existing file in read-only mode

k = next(iter(f.keys())) # getting the first key
dset = f[k] ['timelapse'] # corresponding dataset
print(dset.shape)
data = np.array(dset[:,:,:50]).T # stack of images of the dset

#%% 
snap = data[10,:,:] # read out a single frame from the stack
plt.figure()
plt.imshow(snap)
plt.colorbar()

#%% 
FPS = 8 
maxPixelValue = np.amax(data)

if(maxPixelValue > 255):    
    data  = (1.0*data/maxPixelValue)*255.0

data = np.array(data)
data = data.astype(np.uint8)

fourcc = cv2.VideoWriter_fourcc(*'XVID')  # XVID format works on Windows, for Linux, use something else.
videoFile = cv2.VideoWriter(dir+'movie.avi', fourcc, FPS, (len(data[0][0]), len(data[0])), False) 

for i in range(np.shape(data)[0]):
    videoFile.write(np.uint8(data[i,:,:]))
    
videoFile.release()
