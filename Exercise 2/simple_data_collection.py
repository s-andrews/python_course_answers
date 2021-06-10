#!python

# As the user for 5 numeric values 
# and put them into a list

# We start with an empty list
numeric_values = []

# Now we collect 5 values and add the
# numeric versions of them to the list

numeric_values.append(float(input("Number 1: ")))
numeric_values.append(float(input("Number 2: ")))
numeric_values.append(float(input("Number 3: ")))
numeric_values.append(float(input("Number 4: ")))
numeric_values.append(float(input("Number 5: ")))

# Next we sort the list.  The values have
# been converted to numbers, so it's just
# a simple sort

numeric_values.sort()

# Finally we can print them out
print("\nSorted Values\n=============")
print("Value 1:",numeric_values[0])
print("Value 2:",numeric_values[1])
print("Value 3:",numeric_values[2])
print("Value 4:",numeric_values[3])
print("Value 5:",numeric_values[4])

# We also want to know how many times the
# number 2 was entered
print("\nNumber 2 was present",numeric_values.count(2),"times")