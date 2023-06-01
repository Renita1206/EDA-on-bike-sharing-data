# Renita Kurian
# Test 1 - Python - Question 1

import pandas as pd
import numpy as np
from datetime import datetime
import time

# Read Data
data = pd.read_csv("bike_data_new.csv")

#data.head()

# Convert start time col from string to datetime
def convertStartToDateTime(inp):
  time1 = inp[1]
  #time2 = inp[2]
  t1 = datetime.strptime(time1, '%d-%m-%Y %H:%M')
  #t2 = datetime.strptime(time2, '%d-%m-%Y %H:%M')
  return t1

# Convert end time col from string to datetime
def convertEndToDateTime(inp):
  #time1 = inp[1]
  time2 = inp[2]
  #t1 = datetime.strptime(time1, '%d-%m-%Y %H:%M')
  t2 = datetime.strptime(time2, '%d-%m-%Y %H:%M')
  return t2

data["started_at"]= data.apply(convertStartToDateTime, axis = 1)
data["ended_at"]= data.apply(convertEndToDateTime, axis = 1)


#---------------------------------------------------Question 1 --------------------------------------------------------------
def calctimediff(inp):
  #print(inp)
  time1 = inp["started_at"]
  time2 = inp["ended_at"]
  timediff = time2 - time1
  return (timediff.seconds)/60


def getDurationStats(durations):
  print("Maximum Duration: ", max(durations))
  print("Minimum Duration: ", min(durations))

  mintimetrips = durations.count(min(durations))
  print("Number of trips with minimum duration: ", mintimetrips)


def checkCircular(inp):
  start_latitude = inp[3]
  start_longitude = inp[4]
  end_latitude = inp[5]
  end_longitude = inp[6]

  if(start_latitude == end_latitude and start_longitude==end_longitude):
    return 1
  else:
     return 0


def Question1():
  # Start of runtime
  start = time.time()

  # Find duration of each ride/trip
  data["duration"] = data.apply(calctimediff,axis=1)
  # Remove trips with time = 0 minutes
  cleaned_data = data[data.duration > 0]

  # Calculating minimun, maximum duration and also no of trips with minimum time duration
  getDurationStats(cleaned_data.duration.values.tolist())
  
  # Finding number of round trips
  totalRides = cleaned_data.shape[0]
  roundTrips = cleaned_data.apply(checkCircular,axis=1)
  numberOfRoundTrips = roundTrips.sum()
  print("Number of Round Trips: ", numberOfRoundTrips)
  print("Total trips: ", totalRides)
  print("Percentage of Round Trips: ", (numberOfRoundTrips*100)/totalRides)

  # End of runtime
  end = time.time()

  print("Runtime of Functionfor Part I : %.3f" %((end-start) * 10**3), "ms")

Question1()

print()

#---------------------------------------------------Sub-question 2--------------------------------------------------------------

# Check if data point is between 6AM and 6PM
def checkTime(inp):
  t1 = inp["started_at"]
  t2 = inp["ended_at"]

  start6am = datetime(2023, 2, 1, 6, 0, 0)
  end6pm = datetime(2023, 2, 1, 18, 0, 0)

  if(t1.time()>start6am.time() and t2.time()<end6pm.time()):
    return 1
  else:
    return 0

# Find total number of feasible pairs
def findFeasiblePairs(filtered_data):
  count = 0
  feasiblePairs = []
  for i in range(0, filtered_data.shape[0]):
    end_latitude = filtered_data.iloc[i]["end_lat"]
    end_longitude = filtered_data.iloc[i]["end_lng"]
    end_time = filtered_data.iloc[i]["ended_at"]
    first_trip = filtered_data.iloc[i]["trip_id"]

    tmp = filtered_data[filtered_data.start_lat == end_latitude]
    tmp = tmp[tmp.start_lng == end_longitude]
    tmp = tmp[tmp.started_at > end_time]

    #print(filtered_data.iloc[i]["trip_id"], tmp.trip_id.tolist())
    for trip in (tmp.trip_id.tolist()):
      newPair = [first_trip, trip]
      if newPair not in feasiblePairs:
        feasiblePairs.append(newPair)
        count = count + 1

  return count


def Question2():
  start = time.time()

  # Filter data to get only those within 6AM and 6PM
  data["timeSlotCheck"] = data.apply(checkTime,axis=1)
  filtered_data = data[data.timeSlotCheck == 1]
  filtered_data = filtered_data.iloc[: , :-1]
  #filtered_data.tail()

  count = findFeasiblePairs(filtered_data)
  print("Number of Feasible Pairs: ", count)


  end = time.time()

  print("Runtime of Function for Part II: %.3f" %((end-start) * 10**3), "ms")

Question2()

