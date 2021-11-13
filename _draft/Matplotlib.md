---
layout: posts
---

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

## Colorbars in contourf

```python
from matplotlib.collections import LineCollection
from matplotlib.colors import ListedColormap, BoundaryNorm
```

## XML color format

## Plots for publications

```python
cm= 1./2.56
```