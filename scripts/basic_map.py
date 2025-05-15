import geopandas as gpd
import matplotlib.pyplot as plt
import os

# Define the path to the shapefiles
countries_path = "../data/ne_110m_admin_0_countries.shp"
rivers_path = "../data/Kenya_Major_Rivers/Kenya â Major_Rivers.shp"
lakes_path = "../data/Kenya_Lake/Kenya â Lake.shp"

# Load the data
africa = gpd.read_file(countries_path)[lambda df: df["CONTINENT"] == "Africa"]
lakes = gpd.read_file(lakes_path).to_crs("EPSG:4326")
rivers = gpd.read_file(rivers_path).to_crs("EPSG:4326")


# Plot the data
fig, ax = plt.subplots(figsize=(15, 10))
africa.plot(ax=ax, edgecolor='black', color='lightgrey', linewidth=0.8, label="Countries")
rivers.plot(ax=ax, color='blue', linewidth=0.8, alpha=0.7, label="Rivers")
lakes.plot(ax=ax, color='cyan', edgecolor='darkblue', linewidth=0.8, alpha=0.7, label="Lakes")

# Set the extent to focus on Kenya
ax.set_xlim(33, 42)  # Longitude range
ax.set_ylim(-5, 6)   # Latitude range

# Add grid lines for better orientation
ax.grid(color='grey', linestyle='--', linewidth=0.5, alpha=0.5)

# Add title and legend
plt.title("Kenya Major Rivers and Lakes", fontsize=20, fontweight='bold', pad=20)
plt.legend(loc="upper right", fontsize=12, frameon=True, edgecolor="black", shadow=True, title="Legend")
plt.show()
