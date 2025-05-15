import geopandas as gpd
import matplotlib.pyplot as plt
import os

# Define the path to the shapefile
shapefile_path = "../data/ne_110m_admin_0_countries.shp"

# Read the shapefile
gdf = gpd.read_file(shapefile_path)

# Plot the data
gdf.plot(figsize=(15, 10), edgecolor='black', cmap='tab20')
plt.title("World Map")
plt.show()
