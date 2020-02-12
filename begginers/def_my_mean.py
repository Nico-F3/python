daily_precipitation_edinburgh = [2,7,1,9,0,2,4,5]
daily_precipitation_glasgow =  [5,5,3,6,7,3,2,8]
daily_precipitation_dundee =  [4,2,5,7,2,6,8,7]

# the def keyword tells python you are about to make a function
# the variable name that comes after 'def' is the function name
# in this case our function is called my_mean
# x is a stand in for our input. We call it x but it could have been any variable name at all
def my_mean(x):
  # we make a variable total which we can add the items from the list to
  total=0

  # in this next line we say we will repeat this adding loop 8 times
  # during this loop the variable i will take on the values 0-7, increasing by 1 on each pass
  for i in range(len(x)):
      # on each pass we add the next number to the total we have so far
  	total = total + x[i]

  # finally we will divide by the number of items to get the mean
  mean_value = total / len(x)

  # in this final line we return the answer
  # the rest of the variables here, like total, will be thrown away
  return mean_value


mean_precipitation_edinburgh = my_mean(daily_precipitation_edinburgh)


print(mean_precipitation_edinburgh)