weatherfile = open("StormEleanor_2_3_Jan.csv", "r") #the variable 'r' tell python that we want to open the file as readers

for line in weatherfile:
  print(line)#this print what is in the line
  print(type(line))#this print which type of data is in each line
weatherfile.close()