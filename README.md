# EDA-on-bike-sharing-data
CISTUP Summer Internship Round 1 test  
https://www.kaggle.com/competitions/summer-internship-cistup-iisc-2023/overview

### Question 1
In a bicycle-sharing system, bicycles are stored at fixed docking stations throughout the city. Users can rent
bicycles from one docking station and return them to any other docking station. These systems are often used
for short trips around the city, providing users with a convenient and eco-friendly mode of transportation. A
dataset (link) containing 6,867 bicycle trips over one day is provided. The column descriptions are provided
below.
  • trip id: Unique trip identifier.
  • started at: Start time of the trip
  • ended at: End time of the trip
  • start lat/start lng: Latitude/Longitude of the starting depot
  • end lat/end lng: Latitude/Longitude of the end depot

1. Write a function that removes all trips of duration 0 minutes and prints the following values on the
console. Mention the same values in the report.
• Maximum duration of the trip (in minutes).
• Minimum duration of the trip (in minutes).
• Total number of trips corresponding to the minimum duration.
• Percentage of total circular trips. A trip is defined as circular if it starts and ends at the same
location.
• Total runtime for the function
Hint: The question is designed to judge your basic skills in exploratory data analysis.

2. Filter the original dataset to include only the trips starting between 06:00 AM and 06:00 PM. Find
the total number of feasible pairs of trips. Two trips, A and B, are defined as a feasible pair if they
can be served in succession by the same bicycle, i.e., if the end location of trip A is the same as the
start location of trip B and the start time of the trip B is greater than or equal to the end time of the
trip A. For example, Trip Id 1733 and 1965 are feasible. In the report, mention the total feasible pairs
of trips and runtime.
Hint: The question is designed to judge your critical and analytical thinking.

3. Filter the original dataset to include only the first 100 trips (i.e., trip id 1 to 100). In the report,
mention the number of unique depots used to serve these trips. Next, find the shortest path distance
between all the depots. To do so, do the following steps:
• Download the underlying graph using the OSMnX module (reference) in Python.
• Find the nearest node in the graph corresponding to each depot.
• For every pair of nodes, run a shortest path algorithm (for example, Dijkstra’s (reference)) to
get the length of the shortest path. If the nodes are not reachable from each other, the function
should return -1.
In the report, mention the total runtime and the maximum and minimum (greater than 0) distance.  
  
### Question 2
The dataset (link) contains location data of users collected from GPS-enabled mobile devices over a period
of time. It includes latitude, longitude, altitude, and time-stamp information for each location point. The
data is organized by individual users, with each user having multiple trajectories. Trajectories correspond
to outdoor movements, including daily routines such as commuting and non-routine activities like leisure
and sports. The dataset can be used to analyze mobility patterns and develop location-based applications.
Using the dataset, answer the following questions:
1. Write a function to calculate the total distance traveled by each user in the dataset.
Hint: The question is designed to judge your proficiency in Python. Instead of writing simple for-loops,
think of efficient implementation using parallel programming using multiprocessing (reference).
2. Write a function to extract and visualize the spatial and temporal hotspots of Bejing City. Summarize
findings and attach all images in the report.  

3. Imagine that you have access to a GPS-tracking dataset containing the trajectories of thousands of
individuals over an extended period of time. The dataset includes anonymized information such as
latitude, longitude, altitude, date, and time. In 500 words, describe a problem that you would like to
solve using this data and what methodology you would use to solve it. You could focus on solving an
issue that interests you.
