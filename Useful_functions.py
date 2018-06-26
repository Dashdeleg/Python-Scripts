import matplotlib.colors as colors
import hsluv  # install via pip
import numpy as np


def angle_map(N=256, use_hpl=True):
    """
    Generate custom colormaps
    """
    h = np.ones(N)  # hue
    h[:N//2] = 11.6  # red
    h[N//2:] = 258.6  # blue
    s = 100  # saturation
    l = np.linspace(0, 100, N//2)  # luminosity
    l = np.hstack((l, l[::-1]))
    colorlist = np.zeros((N, 3))

    for i in range(N):
        if use_hpl:
            colorlist[i, :] = hsluv.hpluv_to_rgb((h[i], s, l[i]))
        else:
            colorlist[i, :] = hsluv.hsluv_to_rgb((h[i], s, l[i]))
    colorlist[colorlist > 1] = 1  # correct numeric errors
    colorlist[colorlist < 0] = 0
    return colors.ListedColormap(colorlist)
