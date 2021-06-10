#!python
import random
import statistics
import math

# We're going to make a small simulated dataset
random_data = []
random_mean = 10
random_stdev = 3

# This is klunky at the moment because we haven't done loops yet!
random_data.append(random.normalvariate(random_mean, random_stdev))
random_data.append(random.normalvariate(random_mean, random_stdev))
random_data.append(random.normalvariate(random_mean, random_stdev))
random_data.append(random.normalvariate(random_mean, random_stdev))
random_data.append(random.normalvariate(random_mean, random_stdev))
random_data.append(random.normalvariate(random_mean, random_stdev))
random_data.append(random.normalvariate(random_mean, random_stdev))
random_data.append(random.normalvariate(random_mean, random_stdev))
random_data.append(random.normalvariate(random_mean, random_stdev))
random_data.append(random.normalvariate(random_mean, random_stdev))

# Now we can calculate some values
calculated_mean = statistics.mean(random_data)
calculated_stdev = statistics.stdev(random_data)
calculated_sem = calculated_stdev / math.sqrt(len(random_data)-1)

print("Input\n=====")
print("Mean=",random_mean,sep="")
print("StDev=",random_stdev,sep="")
print("N points=10")

print("\nOutput\n======")
print("Mean=",calculated_mean,sep="")
print("StDev=",calculated_stdev,sep="")
print("SEM=",calculated_sem,sep="")

