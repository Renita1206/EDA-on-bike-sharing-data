import pandas as pd
import numpy as np
from haversine import haversine, Unit
import math

import multiprocessing
from multiprocessing import Pool

data = pd.read_csv("combined_trajectories.csv")
print("Data successfully read")
#data.head()

# Calculate distance in kilometres
def getDistance(loc1, loc2):
  return round(haversine(loc1, loc2, unit='km'), 3)


#getDistance((45.7597, 4.8422), (48.8567, 2.3508))

def calcDistanceForUser(userData):
  distance = 0.0
  for i in range(len(userData)-1):
    #print(userData.iloc[i])
    lat1 = userData.iloc[i][0]
    lon1 = userData.iloc[i][1]
    lat2 = userData.iloc[i+1][0]
    lon2 = userData.iloc[i+1][1]
    #print(lat1, lon1, lat2, lon2)
        
    distance = distance + getDistance((lat1,lon1),(lat2, lon2))

  return distance

def calculate_total_distance(data):
  total_distance = {}
  with Pool() as pool:
    for user_id in data.individual_id.unique():
      userData = data[data.individual_id == user_id]
      #print(userData.head())
      print("Obtained userData for user: ", user_id)
      dataByTrajectories = [userData[userData.trajectory_id == trajectory ] 
                            for trajectory in userData.trajectory_id.unique()]
      #print(dataByTrajectories)
      distances = pool.map(calcDistanceForUser, dataByTrajectories)
      print(sum(distances))
      total_distance[user_id] = sum(distances)
    return total_distance
  
total_distance = calculate_total_distance(data)
print(total_distance)