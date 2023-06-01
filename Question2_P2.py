import pandas as pd
import numpy as np
from haversine import haversine, Unit
import math

import folium
from folium.plugins import HeatMap

import multiprocessing
from multiprocessing import Pool

data = pd.read_csv("combined_trajectories.csv")
print("Data successfully read")
#data.head()

def getBeijingData(data):
  # Define city boundaries
  lat_min = 39.4428 #southmost lat
  lat_max = 41.0619 #northmost lat
  lon_min = 115.4204 #westernmost
  lon_max = 116.7815 #easternmost 
  
  # Filter data
  df_filtered = data.loc[(data['latitude'] >= lat_min) &
                         (data['latitude'] <= lat_max) & 
                         (data['longitude'] >= lon_min) & 
                         (data['longitude'] <= lon_max)]

  return df_filtered


# Create a map centered on Beijing City
map = folium.Map(location=[39.9042, 116.4074], zoom_start=11)
filtered_data = getBeijingData(data)
print("Successfully filtered data")
# Create a heatmap layer using the filtered data
heatmap = HeatMap(data=filtered_data[["latitude", "longitude"]], radius=15)
# Add the heatmap layer to the map
heatmap.add_to(map)
print("Heatmap added")

# Draw bounding box over city
bounds = [[39.4428, 115.4204], [41.0619, 116.7815]]
# Create a rectangle overlay for the bounding box
rect = folium.Rectangle( bounds, fill=False, color='red', weight=2, opacity=1)
# Add the rectangle overlay to the map
rect.add_to(map)
print("Bounding Box added")

# Save the map as an HTML file
map.save("beijing_heatmap_bb.html")