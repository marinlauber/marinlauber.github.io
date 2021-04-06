---
layout: posts
title: "Advanced Scientific Matplotlib - Part 1/n"
date: 2020-03-03
---

This series of blog post is here to give some of the tricks I use to produce high-quality figures, suitable for publications for example.

## Introduction

Of course I am using `matplotlib` to create all sorts of figures and animations! Coupled with `numpy` and somethimes `pandas` to read and handle all sorts of data, these are some very powerful tools. I am not going to cover the basics of matplotlib, such as importing the library, or doing simple plots. There have been a lot a excellent example on the subjects already.

Instead I will dig a bit deeper in what `matplotlib` has to offer and how we can benefit from it to show the results of our research.

## Using Style Sheets

Custom stylesheets are a very efficient way to improve the default plotting style from matplotlib. You can get some excellent one from [here](https://github.com/garrettj403/SciencePlots). Once they are installed in the correct directory, you can simply use them with

```python
plt.use.style("my_amazing_style")
```




```bash
# Matplotlib style for general scientific plots

# Set color cycle
axes.prop_cycle : cycler('color', ['0C5DA5', '00B945', 'FF9500', 'FF2C00', '845B97', '474747', '9e9e9e'])

# Set default figure size
figure.figsize : 2.75, 2.75
figure.dpi : 600

# Font sizes
font.size : 7

# Set x axis
xtick.direction : out
xtick.major.size : 2
xtick.major.width : 0.5
xtick.minor.size : 1.
xtick.minor.width : 0.5
xtick.minor.visible :   True
xtick.top : True

# Set y axis
ytick.direction : out
ytick.major.size : 3
ytick.major.width : 0.5
ytick.minor.size : 1.5
ytick.minor.width : 0.5
ytick.minor.visible :   True
ytick.right : True

# Set line widths
axes.linewidth : 0.5
grid.linewidth : 0.5
lines.linewidth : 1.

# Remove legend frame
legend.frameon : False

# Always save as 'tight'
savefig.bbox : tight
savefig.pad_inches : 0.05

# Use serif fonts
font.serif : Times New Roman
font.family : serif

# Use LaTeX for math formatting
text.usetex : True
text.latex.preamble : \usepackage{amsmath}
```

> **_Note:_**  Under `OSX` the directory that stores your stylsheets is located at `.matplotlib/stylelib/` and in Linux (Ubuntu 18.04) under `.config/matplotlib/stylelib/`.

## Custom Line style and colors

```
(offset, on-off-seq)
```

```python
stl = [(0,()),
       (0,(1.1,1.1)),
       (0,(2.8,1.1)),
       (0,(2.8,1.1,1.1,1.1)),
       (0,(3,1,1,1,1,1)),
       (0,(3,1,3,1,1,1,1,1)),
       (0,(7,1,1,1,1,1))]
```

```python
from matplotlib.colors import to_hex
cols = ['C0','#2ca02c','red',to_hex(255.,255.,255.)]
```

## Subplots
fig = plt.figure(constrained_layout=True,figsize=(13.7*cm,6.85*cm))
gs = plt.GridSpec(2, 2, figure=fig)
ax1 = fig.add_subplot(gs[0,0])
ax2 = fig.add_subplot(gs[1,0], sharex=ax1)
ax3 = fig.add_subplot(gs[:,1])


```python
def Richardson(phi, r=2.):
    p = np.log((phi[2]-phi[1])/(phi[1]-phi[0]))/np.log(r)
    phi_ext = phi[0] + (phi[0]-phi[1])/(2**p-1.)
    return p, phi_ext
```


## Images
```python
import matplotlib.image as mpimg
```

## Fill Between

## Colrobars in contourf

```python
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
```

## XML color format

## Plots for publications

```python
cm= 1./2.56
```