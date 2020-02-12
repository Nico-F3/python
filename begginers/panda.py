import pandas as pd #we can now use functions in pandas using the abbreviated form pd

data = pd.read_csv('StormEleanor_2_3_Jan.csv', delimiter=',', header=0) #functions and data structures by putting a dot . after pd, and then typing the name of the function we want to use.

pressure_data = data['Pair_Avg']

#Get me the read_csv function from the pandas module

#In this case, we are using the read_csv function to load a text based file (after all, a csv file is just a text file). We need to give the read_csv function three arguments:

#1. The path and name of the file (“StormEleanor_2_3_Jan.csv”). (This assumes you have downloaded the text file to the same folder you are writing your Python scripts.)
#2. The delimiter used in this type of text file, or the character used to separate the values in the file. Since we are using a csv file (comma separated variable file), the delimiter is a comma (','). The delimiter must go inside quotation marks.
#3. The header argument, which tells pandas which row contains the column header names. Remember Python starts counting from zero, so we want to use row 0.

print (type(data))

print (pressure_data)