
"""
demo_q1_q3_p43.py: A guide to calulating percentile with the 43 as example, 
            along with q1(25) and q3(75). This lesson is acomapnied by
            a real-world example of using quartiles in R.
"""
__author__      = "Matthew Hodge"
__date__        = "05/12/2023"

# We begin with an unorganized array of observations. This observations are arbitrary,
# but if it helps we can think of them as test scores.
data = [31,33,108,200,80,18,12,5,39,0,2,25,6,30,22,16,32]
#print(data)

# Our first step is to organize our observations into an accending order.
data.sort()
#print(data)

# Next, we need n to equal the amount of observations we have.
n = len(data)
#print(n)

# Here we set the percentage we're interested in. We will use 43 as an example.
p = 43

# Now we must find the locator position. This is the value that tells us which numbered
# position in the sequence we need to start with.
lP = (n + 1) * (p / 100)
#print(n)

# We grab the floor value integer as our starting location
lInt = int(lP)

# We grab the value to the right of the position locators decimal. This value represents 
# the percentage of the distance between the value at our position location and the next value
# that must be accounted for.
lFloat = lP - lInt

# Now we save a referance to the observation held at the position location. In this case, we are
# subtracting one, because arrays are zero indexed.
obAtPosLoc = data[lInt-1]
#print(n)

# Next, we need to determine the distance between the value we have found, and then next
# value in the sequence. We will default the distance to 0, and ensure we are not on the
# last index of the array, to avoid an out of bounds error.
dist = 0
if lInt-1 < len(data)-1: 
    dist = data[lInt] - data[lInt-1]
#print(dist)

# Finally, we can determine our value at the 43rd percentile by multiplying our decimal
# value we held by the distance between the observation at our position location and the
# next number in the sequence.
val = obAtPosLoc + (lFloat * dist)
#print(val)

#Let's take our calculations and refactor them into a reusable function.
def observation_at_persentile(observations, percentile):
    observations.sort()
    n = len(observations)
    p = percentile
    lP = (n + 1) * (p / 100)
    lInt = int(lP)
    lFloat = lP - lInt
    obAtPosLoc = observations[lInt-1]
    dist = 0
    if lInt-1 < len(observations)-1: 
        dist = observations[lInt] - observations[lInt-1]
    return obAtPosLoc + (lFloat * dist)

# Let's confirm that our function is working by calculating the 43rd percentile
# on the same set of observations.
#print(observation_at_persentile(data, 43))

# Now lets calculate the 1st and 3rd quartile and save those results
q1 = observation_at_persentile(data, 25)
q3 = observation_at_persentile(data, 75)

# The 1st and 3rd quartiles are important, because we can use them to help
# isolate outliers. That is, any outlying values that are to low to be considered will
# be to the left of the 1st quartile, and outliers too high will be to the right of the 
# 3rd quartile.

# Knowing this, let create a new data set that eliminates outliers.
cleanedData = []
for observation in data: 
    if observation > q1 and observation < q3:
        cleanedData.append(observation)

#Let's validate that outliers have been removed
#print(cleanedData)

#With outlier data removed we can now get a more accureate 43rd percentile value
#print(observation_at_persentile(cleanedData, 43))