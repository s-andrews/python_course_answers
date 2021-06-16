#!python

# Initialise a data structure to hold variant counts
variant_counts = {
    "E23A": 0, 
    "P12S": 0, 
    "W88Y": 0,
    "R32N": 0
}

# Ask the user for variants

while True:
    variant = input("Which variant? ")
    
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

for variant,count in variant_counts.items():
    print(variant,"was seen",count,"times")

