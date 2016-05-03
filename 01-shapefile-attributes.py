import geopandas as gpd

poly_harv = gpd.read_file('_data-jsta/HARV/HarClip_UTMZ18.shp')
lines_harv = gpd.read_file('_data-jsta/HARV/HARV_roads.shp')
points_harv = gpd.read_file('_data-jsta/HARV/HARVtower_UTM18N.shp')

print(points_harv.geom_type)
len(points.harv)
points_harv.crs
print(points_harv.bounds)
points_harv

print(lines_harv.head())
