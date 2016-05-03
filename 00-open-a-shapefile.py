#==========================================#

# conda create --name fiona python=3 fiona=1.1.6
# source activate fiona
# conda install fiona=1.1.6
# conda install -c ioos geopandas=0.2.0.dev0
# conda install rasterio=0.25
# conda install -c ioos cartopy=0.14.2

# see also:
# https://github.com/darribas/gds15/blob/v0.9/content/labs/lab_03.pdf
# http://nbviewer.jupyter.org/github/OSGeo/osgeolive-jnb/blob/master/python2-notebooks/IRIS/cartopy-rasterio-plot.ipynb
# https://snorfalorpagus.net/blog/2014/06/26/using-cartopy-with-rasterio/

#==========================================#

import geopandas as gpd
import matplotlib.pyplot as plt
import rasterio
import numpy as np

poly_harv = gpd.read_file('_data-jsta/HARV/HarClip_UTMZ18.shp')

print(poly_harv.geom_type)
print(poly_harv.crs)
print(poly_harv.bounds)

print(poly_harv.head())

poly_harv.plot(cmap = 'Greens')
plt.suptitle("NEON Harvard Forest\nField Site")
plt.show()


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

raster_harv = rasterio.open('_data-jsta/HARV/CHM/HARV_chmCrop.tif')
data = raster_harv.read()
data = np.transpose(data, [1,2,0])
xmin = raster_harv.transform[0]
xmax = raster_harv.transform[0] + raster_harv.transform[1] * raster_harv.width
ymin = raster_harv.transform[3] + raster_harv.transform[5] * raster_harv.height
ymax = raster_harv.transform[3]

plt.imshow(data[:,:,0], origin='upper', extent = [xmin, xmax, ymin, ymax], zorder = 1)

plt.show()
