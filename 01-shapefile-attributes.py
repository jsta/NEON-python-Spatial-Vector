import geopandas as gpd
import matplotlib.pyplot as plt

poly_harv = gpd.read_file('_data-jsta/HARV/HarClip_UTMZ18.shp')
lines_harv = gpd.read_file('_data-jsta/HARV/HARV_roads.shp')
points_harv = gpd.read_file('_data-jsta/HARV/HARVtower_UTM18N.shp')

print(points_harv.geom_type)
len(points_harv)
points_harv.crs
print(points_harv.bounds)
points_harv

print(lines_harv.head())


f, ax = plt.subplots(1)
lines_harv_footpath <- lines_harv['TYPE' == 'footpath']
for line in test['geometry']:
	gpd.plotting.plot_multilinestring(ax, line, color = 'black', linewidth = 3)
