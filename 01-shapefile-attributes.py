# http://sensitivecities.com/so-youd-like-to-make-a-map-using-python-EN.html
# waterprogramming.wordpress.com/2014/04/30

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

lines_harv_footpath = lines_harv[lines_harv.TYPE == 'footpath']

len(lines_harv_footpath)

f, ax = plt.subplots(1)
for line in lines_harv_footpath['geometry']:
	gpd.plotting.plot_multilinestring(ax, line, color = ('black'), linewidth = 3)

lines_harv_footpath.plot()
plt.show()


lines_harv_boardwalk = lines_harv[lines_harv.TYPE == 'boardwalk']
len(lines_harv_boardwalk)

f, ax = plt.subplots(1)
for line in lines_harv_boardwalk['geometry']:
	gpd.plotting.plot_multilinestring(ax, line, color = ('green'), linewidth = 3)

plt.show()

lines_harv_stonewall = lines_harv[lines_harv.TYPE == 'stone wall']
len(lines_harv_stonewall)

f, ax = plt.subplots(1)
for line in lines_harv_stonewall['geometry']:
	gpd.plotting.plot_multilinestring(ax, line, color = ('green'), linewidth = 3)

plt.show()

lines_harv.TYPE.unique()
lines_harv.dtypes.TYPE
lines_harv.TYPE.value_counts()

lines_colorkey = {'boardwalk':'blue','footpath':'green','stone wall':'grey','woods road':'purple'}
f, ax = plt.subplots(1)
for line, row in lines_harv.iterrows():
	gpd.plotting.plot_multilinestring(ax, row['geometry'], color = lines_colorkey[row['TYPE']], linewidth = 3)

plt.show()


f, ax = plt.subplots(1)
for line, row in lines_harv.iterrows():
	gpd.plotting.plot_multilinestring(ax, row['geometry'], color = lines_colorkey[row['TYPE']], linewidth = 6)

plt.show()

lines_widthkey = {'boardwalk':1,'footpath':2,'stone wall':3,'woods road':4}
f, ax = plt.subplots(1)
for line, row in lines_harv.iterrows():
	gpd.plotting.plot_multilinestring(ax, row['geometry'], color = lines_colorkey[row['TYPE']], linewidth = lines_widthkey[row['TYPE']])

plt.show()
