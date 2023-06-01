import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import seaborn as sns

#data = pd.read_csv("combined_trajectories.csv")
#print("Data successfully read")
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

def hotspot_analysis(df):
  df["time"] = pd.to_datetime(df["time"], format= '%H:%M:%S')
  df.set_index("time", inplace=True)
  #print(df.head())
  data_resampled = df.resample("H").size()
  #print(data_resampled.describe())

  axis = pd.to_datetime(data_resampled.index)
  axis = axis.hour
  print(axis)

  plt.figure(figsize = (10,5))
  plt.plot(axis, data_resampled.values)
  plt.title("Number of Data Points over Time")
  plt.xlabel("Time")
  plt.ylabel("Number of Data Points")
  plt.show()


df = pd.read_csv("combined_trajectories.csv")
print("Data successfully read")
df = getBeijingData(df)
print("Data successfully filtered")

hotspot_analysis(df)