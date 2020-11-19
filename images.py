#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import cm_xml_to_matplotlib as cm

plt.style.use('mystyle')

if __name__ == "__main__":
    
    cmap = cm.make_cmap('../SciVisColor/blue-5.xml')
    w = np.round(np.genfromtxt("vort_000015.dat", delimiter=" ")[1:,:], 5)
    sizes = np.shape(w)
    width = float(sizes[1]); height = width/4.
    fig = plt.figure()
    fig.set_size_inches(width/height, 1, forward=False)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    off = 128
    ax.contourf(w[int(off):int(height+off),:], levels=11, cmap=cmap)
    plt.savefig("background.png", dpi=4*height, bbox_inches="tight", pad_inches=0) 
    plt.close()
