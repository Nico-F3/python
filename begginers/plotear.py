import pandas as pd
import matplotlib.pyplot as plt
# import the required libraries and modules
import datetime # We add datetime to our import statements at the start of the script

data = pd.read_csv('StormEleanor_2_3_Jan.csv', delimiter=',', header=0)

pressure_data = data['Pair_Avg']


# Code to create the timeseries values
date_time_series = []#We create an empty list to store our dates
date_time = datetime.datetime(2018, 1, 2)#We set the first date in the series, which is Midnight (00:00) on the 2nd January 2018. (Midnight is set by default if no hours/minutes are specified)
date_at_end = datetime.datetime(2018, 1, 3, 23, 59)#We set the end date for our date, which is 23:59 on the 3rd January 2018.
step = datetime.timedelta(minutes=1)#Set the timestep as a timedelta object. (Remember, the weather station data is recorded every minute.

while date_time <= date_at_end: # Iterate by adding the time delta to the start time, and appending the new time step to the list, until we reach the final time.
  date_time_series.append(date_time)
  date_time += step

plt.plot(date_time_series, pressure_data) #The plot function will plot a line chart by default, and the first argument is the dataseries you wish to plot. 

plt.ylabel("Pressure (hPa)")
plt.xlabel("Time")
plt.title("Average Pressure, JCMB Weather Station, 2-3rd Jan 2018")
#To write the plot out to an image file, the savefig function is used, with the filename specified.
#The image filetype is inferred from the filename (e.g. “.png”) and a wide range of common image file types are supported in matplotlib, including vector and raster formats.
plt.xticks(rotation=-60)#(Optional) It will probably look nice if the x-labels are rotated slightly so that the times don’t overlap. We can do this by setting the rotation argument in the plt.xticks() function.
plt.tight_layout()# To tidy up the axes, and scale them correctly, we can add a call to plt.tight_layout() just before we save the figure.


plt.savefig("pressure.png")#always at the end!