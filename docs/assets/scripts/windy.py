#!/home/marin/anaconda3/bin/python
# -*- coding: utf-8 -*-

import matplotlib as mpl
import numpy as np

# from 0 - 30 knots, in m/s
v = np.linspace(0,30,21)*0.5144

# Choose colormap
# viridis = cm.get_cmap('viridis', len(v))
viridis = mpl.colormaps['viridis']

# generate color at each windspeed
my_cmap = viridis(np.linspace(0,1,len(v)))

# save to file,  needs converting to RGB(0-255)
output = open("windy_viridis.txt","w")
output.write("[")
for i in range(len(v)):
    text = "[%.4f,[" % v[i]
    text += "%d,%d,%d,%d]],\n" % (my_cmap[i,0]*255,
                                  my_cmap[i,1]*255,
                                  my_cmap[i,2]*255,
                                  my_cmap[i,3]*255)
    if(i==len(v)-1): text = text[:-2]+"]"
    output.write(text)
output.close()
