import geopandas as gpd
import matplotlib.pyplot as plt

f, ax = plt.subplots(1)

state_boundary_us = gpd.read_file('_data-jsta/US-Boundary-Layers/US-State-Boundaries-Census-2014.shp')
state_boundary_us.geom_type
for poly in state_boundary_us['geometry']:
	gpd.plotting.plot_multipolygon(ax, poly, alpha = 0, linewidth = 1)

state_boundary_us_dissolve = gpd.read_file('_data-jsta/US-Boundary-Layers/US-Boundary-Dissolved-States.shp')
state_boundary_us_dissolve.geom_type
for poly in state_boundary_us_dissolve['geometry']:
	gpd.plotting.plot_multipolygon(ax, poly, alpha = 0, linewidth = 4)

points_harv = gpd.read_file('_data-jsta/HARV/HARVtower_UTM18N.shp')
points_harv.geom_type
for point in points_harv['geometry']:
 	gpd.plotting.plot_point(ax, point, color = 'purple')

plt.show()

points_harv.crs
state_boundary_us.crs

points_harv = points_harv.to_crs(crs = state_boundary_us.crs)

f, ax = plt.subplots(1)
for poly in state_boundary_us['geometry']:
	gpd.plotting.plot_multipolygon(ax, poly, alpha = 0, linewidth = 1)

for poly in state_boundary_us_dissolve['geometry']:
	gpd.plotting.plot_multipolygon(ax, poly, alpha = 0, linewidth = 4)

for point in points_harv['geometry']:
 	gpd.plotting.plot_point(ax, point, color = 'purple')

plt.show()
