import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Polygon

plt.style.use("Journal")

def cm_(x, y): return (x/2.56, y/2.56)

# transform MN03 into WGS84
def MN03_to_WGS84(x,y,height):
    x = (x - 200000)/1000000
    y = (y - 600000)/1000000
    lat = 16.9023892 + 3.238272 * x - 0.270978 * y**2 - 0.002528 * x**2 - 0.0447 * y**2 * x - 0.0140 * x**3 
    lon = 2.6779094 + 4.728982 * y  + 0.791484 * y*x + 0.1306 * y * x**2 - 0.0436 * y**3
    lat = lat * 100/36
    lon = lon * 100/36
    height = height + 49.55 - 12.60 * y - 22.64 * x
    return lat, lon, height


# read elevation data
data = np.genfromtxt("Data/DHM200.xyz")
print(data.shape)

# extract xyz data, MN03 NF02 coordinate system
x = data[:,1]
y = data[:,0]
height = data[:,2]

# Read file using gpd.read_file()
data = gpd.read_file("Data/swissBOUNDARIES3D_1_3_TLM_LANDESGEBIET.shp")
data.drop([1,2,3], axis=0, inplace=True)
data = gpd.GeoSeries(data.geometry)
data = data.to_crs("EPSG:4326")

# transform manually
lat, lon, height = MN03_to_WGS84(x,y,height)
print(min(height), max(height))

# generate mask for switzerland
mask = gpd.GeoSeries(Polygon([(min(lon),min(lat)),
                              (min(lon),max(lat)),
                              (max(lon),max(lat)),
                              (max(lon),min(lat))]), crs="EPSG:4326")
mask = mask.difference(data) 

# plot contour
fig, ax = plt.subplots(1, 1, figsize=cm_(18,8))
cntr = ax.tricontourf(lon, lat, height, levels=np.linspace(0,5000,101), cmap="gist_earth")
fig.colorbar(cntr, ax=ax, shrink=0.84, ticks=np.linspace(0,5000,5), label="Elevation (m)")

# plot boundary
mask.plot(ax=ax, color="white")
plt.axis("off")
plt.savefig("topo_map_Switzerland.png", dpi=1200, bbox_inches="tight")
plt.show()
