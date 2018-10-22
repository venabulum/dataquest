## 2. NYC Taxi-Airport Data ##

import csv
import numpy as np

# import nyc_taxi.csv as a list of lists
f = open("nyc_taxis.csv", "r")
taxi_list = list(csv.reader(f))

# remove the header row
taxi_list = taxi_list[1:]

# convert all values to floats
converted_taxi_list = []
for row in taxi_list:
    converted_row = []
    for item in row:
        converted_row.append(float(item))
    converted_taxi_list.append(converted_row)

# start writing your code below this comment
taxi = np.array(converted_taxi_list)

## 3. Understanding NumPy ndarrays ##

taxi_five = taxi[:5]
taxi_ten = taxi[:10]
print(taxi_ten)

## 4. Selecting and Slicing Rows and Items from ndarrays ##

row_0 = taxi[0]
rows_391_to_500 = taxi[391:501]
row_21_column_5 = taxi[21,5]

## 5. Selecting Columns and Custom Slicing ndarrays ##

cols = [1,4,7]
columns_1_4_7 = taxi[:, cols]
row_99_columns_5_to_8 = taxi[99, 5:9]
rows_100_to_200_column_14 = taxi[100:201, 14]

## 6. Vector Math ##

trip_distance_miles = taxi[:,7]
trip_length_seconds = taxi[:,8]

trip_length_hours = trip_length_seconds / 3600 # 3600 seconds is one hour
trip_mph = trip_distance_miles / trip_length_hours
print(trip_mph)

## 8. Calculating Statistics For 1D ndarrays ##

mph_min = trip_mph.min()
mph_max = trip_mph.max()
mph_mean = trip_mph.mean()

## 9. Calculating Statistics For 2D ndarrays ##

taxi_column_means = taxi.mean(axis=0)
print(taxi_column_means)

## 10. Adding Rows and Columns to ndarrays ##

trip_mph_2d = np.expand_dims(trip_mph, axis = 1)
taxi = np.concatenate([taxi, trip_mph_2d], axis = 1)
print(taxi)

print(trip_mph)

## 11. Sorting ndarrays ##

# Use numpy.argsort() to get the indices which would sort the trip_mph column from the taxi ndarray. The trip_mph column is at column index 15.
# Use the indices from the previous instruction to sort the taxi ndarray, and assign the result to taxi_sorted.
# Use the print() function to examine the taxi_sorted ndarray.
mph_column = taxi[:, 15]
sorted_order = np.argsort(mph_column)
taxi_sorted = taxi[sorted_order]
print(taxi_sorted)