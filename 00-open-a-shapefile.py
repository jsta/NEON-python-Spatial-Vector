
#tested shapely, ogr

#==========================================#

#conda create --name fiona python=3 fiona=1.1.6
#source activate fiona
#conda install fiona=1.1.6
#conda install -c ioos geopandas=0.2.0.dev0
#conda install rasterio=0.25

import geopandas as gpd
import matplotlib.pyplot as plt

poly_harv = gpd.read_file('_data-jsta/HARV/HarClip_UTMZ18.shp')

print(poly_harv.geom_type)
print(poly_harv.crs)
print(poly_harv.bounds)

print(poly_harv.head())

poly_harv.plot(cmap = 'Greens')
plt.suptitle("NEON Harvard Forest\nField Site")
plt.show()

##
lines_harv = gpd.read_file('_data-jsta/HARV/HARV_roads.shp')
points_harv = gpd.read_file('_data-jsta/HARV/HARVtower_UTM18N.shp')

f, ax = plt.subplots(1)
for poly in poly_harv['geometry']:
	gpd.plotting.plot_multipolygon(ax, poly, facecolor = 'green', alpha = 0.25, linewidth = 0.1)
for line in lines_harv['geometry']:
	gpd.plotting.plot_multilinestring(ax, line, color = 'black', linewidth = 3)
for point in points_harv['geometry']:
 	gpd.plotting.plot_point(ax, point, color = 'purple')

plt.show()

import rasterio
import numpy as np

raster_harv = rasterio.open('_data-jsta/HARV/CHM/HARV_chmCrop.tif')
#http://nbviewer.jupyter.org/github/OSGeo/osgeolive-jnb/blob/master/python2-notebooks/IRIS/cartopy-rasterio-plot.ipynb
xmin = raster_harv.transform[0]
xmax = raster_harv.transform[0] + raster_harv * raster_harv.width
ymin = raster_harv.transform[3] + raster_harv * raster_harv.Height
ymax = raster_harv.transform[3]
raster_harv = raster_harv.read()

plt.imshow(raster_harv)

red = raster_harv.read(1)
bounds = (raster_harv.bounds.left, raster_harv.bounds.right, raster_harv.bounds.bottom, raster_harv.bounds.top)
# green = raster_harv.read(2)
# blue = raster_harv.read(3)
pix = np.dstack((red))
plt.imshow(pix, extent = bounds)
