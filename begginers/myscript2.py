#with open("StormEleanor_2_3_Jan.csv", "r") as weatherfile:
 # for line in weatherfile:
  #  print(line.split(','))#We can break up the data by splitting the string. Change the script so it contains


#pressure_data = []#we defined pressure_data as an empty list

with open("StormEleanor_2_3_Jan.csv", "r") as weatherfile:
  next(weatherfile) #next() makes the file start at the second value in the list
  for line in weatherfile:
    data_row = line.split(',')#First we create a variable called data_row to store each line of the text file as a list as we read it in
    pressure = data_row[6] #Then we get each value of pressure by indexing the data_row list with the number 6.
    print(pressure)#Finally we print the pressure value to screen
    pressure_data.append(float(pressure)) #creates a list with the values of pressure that come from the column number 6 of the file
    float transform the variables into floating numbers


    # Oh no! This is the header line!
print(pressure_data[0])   # Prints: 'Pair_avg'

# Argh! This is a string!
print(type(pressure_data[1]))  # Prints: 'str'

print(pressure_data[0])
print(type(pressure_data[1]))


import csv

pressure_data = []   # Create an empty list as before to store values

with open('StormEleanor_2_3_Jan.csv', 'r') as csvfile:
  next(csvfile)
  for row in csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC): #The quoting=csv.QUOTE_NONNUMERIC argument tells the csv module to read all the non-quoted values in the csv file as strings, and the rest as numeric values (e.g. floats).
    pressure_data.append(row[6])

# Check our variables look okay and they are the correct type:
print(pressure_data)
print(type(pressure_data[1]))