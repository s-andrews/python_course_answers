#!python

# Calculate the amount of material needed
# to make a solution of a certain molarity

# We're going to ask the user for the three
# values we need for the calculation.

print("Solution Calculator")
print("===================\n")

molecular_mass = input("What is the molecular mass? ")
volume_ml = input("What is the solution volume (ml)? ")
conc_molar = input("What molarity do you require? ")

# We need to convert the strings we get from input
# into floats for the calculation

molecular_mass = float(molecular_mass)
volume_ml = float(volume_ml)
conc_molar = float(conc_molar)

# Convert the volume to litres
volume_l = volume_ml/1000

# Do the calculation
mass = conc_molar * volume_l * molecular_mass

# Write the output

print("\n\nTo create",volume_ml,"ml of a",
conc_molar, "M solution of a compound with molecular mass",
molecular_mass,"you need",round(mass,2),"g of material")