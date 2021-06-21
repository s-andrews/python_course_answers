#!python

# Initialise a dictionary structure to hold variant counts
# with variants as keys and counts as values.
variant_counts = {
    "E23A": 0, 
    "P12S": 0, 
    "W88Y": 0,
    "R32N": 0
}

# Ask the user for variants in an infinite loop
while True:
    variant = input("Which variant? ")
    
    # Remove any leading or trailing whitespace
    variant = variant.strip()

    # If there's nothing then stop asking
    if variant == "":
        break

    # If this isn't one we care about then
    # print a warning and move on
    if variant not in variant_counts:
        print("We're not counting",variant)
        continue

    variant_counts[variant] += 1


# We can finally print out the results. We're
# iterating over items which means we get both
# the key and the value in a tuple, which we'll
# split into two separate variables
for variant,count in variant_counts.items():
    print(variant,"was seen",count,"times")

