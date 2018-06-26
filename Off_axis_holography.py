"""
    Sample code for doing off-axis holography analysis
    .. lastedit:: 20/6/2018
    .. sectionauthor:: Pritam Pai <p.pai@uu.nl> and
    .. Dashdeleg Baasanjav <d.baasanjav@uu.nl>
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

from scipy import ndimage
from mpl_toolkits.axes_grid1 import make_axes_locatable
from Useful_functions import angle_map


# Load images
path = 'C:/Users/Baasa001/Desktop'+'/'
ref = cv2.imread(path + 'Reference.tiff', 0)
sig = cv2.imread(path + 'Hologram.tiff', 0)

# Fourier image containing 1st order blob translated to the origin
fourierTranslated = np.zeros((960, 1280), dtype=complex)
#%%
"""Off-axis holography"""

fourier = np.fft.fftshift(np.fft.fft2(sig))  # take 2d fourier transform of signal image
fourier1stOrderCenter = np.rint(np.asarray(ndimage.measurements.center_of_mass(np.abs(fourier[450:465, 540:560])))).astype(int)  #returns coordinates of COM

# select box around 1st order COM
fourierTrunc = fourier[450+fourier1stOrderCenter[0]-10:450+fourier1stOrderCenter[0]+10, 540+fourier1stOrderCenter[1]-10:540+fourier1stOrderCenter[1]+10]

# fourier image with 1st order translated to origin (q=0)
fourierTranslated[480-10:480+10, 640-10:640+10] = fourierTrunc

invfourier = np.fft.ifft2(np.fft.ifftshift(fourierTranslated))   # IFT of selected spectrum in fourier space
invfourier_by_ref = np.divide(invfourier,np.sqrt(ref))     # divide by reference field amplitude
#%%
"""Plotting the results"""

hsluv_anglemap = angle_map(N=256, use_hpl=False)

fig = plt.figure(1, figsize=(18, 15))
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
divider1 = make_axes_locatable(ax1)
cax1 = divider1.append_axes("right", size="5%", pad=0.05)
divider2 = make_axes_locatable(ax2)
cax2 = divider2.append_axes("right", size="5%", pad=0.05)
divider3 = make_axes_locatable(ax3)
cax3 = divider3.append_axes("right", size="5%", pad=0.05)
divider4 = make_axes_locatable(ax4)
cax4 = divider4.append_axes("right", size="5%", pad=0.05)

im1 = ax1.imshow(np.abs(fourier[380:580, 500:780]), clim=(0.0, 1e5), interpolation='None')
ax1.tick_params(axis='both', labelsize=20)
cbar1 = plt.colorbar(im1, cax1)
cbar1.ax.tick_params(labelsize=20)
cbar1.set_label("Intensity (counts)", size=26)
cbar1.formatter.set_powerlimits((0, 0))
cbar1.ax.yaxis.offsetText.set_fontsize(20)
cbar1.update_ticks()
ax1.set_xlabel("$k_x$ (px$^{-1}$)", size=26)
ax1.set_ylabel("$k_y$ (px$^{-1}$)", size=26)
ax1.set_title('FFT of camera image', size=24)
ax1.get_xaxis().set_ticklabels([])
ax1.get_yaxis().set_ticklabels([])


im2 = ax2.imshow(np.abs(fourierTranslated[470:490, 630:650]), clim=(0.0, 1e5), interpolation='None')
ax2.tick_params(axis='both', labelsize=20)
cbar2 = plt.colorbar(im2, cax2)
cbar2.ax.tick_params(labelsize=20)
cbar2.set_label("Intensity (counts)", size=26)
cbar2.formatter.set_powerlimits((0, 0))
cbar2.ax.yaxis.offsetText.set_fontsize(20)
cbar2.update_ticks()
ax2.set_xlabel("$k_x$ (px$^{-1}$)", size=26)
ax2.get_xaxis().set_ticklabels([])
ax2.get_yaxis().set_ticklabels([])
ax2.set_title('First order (q=0)', size=24)

im3 = ax3.imshow(np.abs(invfourier_by_ref), interpolation='None', vmin=0, vmax=4.2)
ax3.tick_params(axis='both', labelsize=20)
cbar3 = plt.colorbar(im3, cax3, ticks=[0, 1.6, 3.2])
cbar3.ax.tick_params(labelsize=20)
cbar3.set_label("Field amplitude (counts$^{1/2}$)", size=26)
ax3.set_xlabel("Pixels", size=26)
ax3.set_ylabel("Pixels", size=26)
ax3.set_title('Retrived field amplitude', size=24)

im4 = ax4.imshow(np.angle(invfourier_by_ref), interpolation='None', cmap=hsluv_anglemap, vmin = -np.pi, vmax = np.pi)
ax4.tick_params(axis='both', labelsize=20)
cbar4 = plt.colorbar(im4, cax4, ticks=[-np.pi, 0, np.pi])
cbar4.ax.tick_params(labelsize=20)
cbar4.set_label("Phase (rad)", size=26)
cbar4.set_ticklabels(['$-\pi$', '$0$', '$\pi$'])
ax4.set_xlabel("Pixels", size=26)
ax4.set_title('Retrieved field phase', size=24)

plt.show()
fig.savefig("offaxisholography.png", transparent=True, bbox_inches="tight", dpi=300)
