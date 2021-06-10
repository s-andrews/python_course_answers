#!python

# Calculate the amount of material needed
# to make a solution of a certain molarity

molecular_mass = 58.44 # NaCl
volume_ml = 250
conc_molar = 0.5

# Convert the volume to litres
volume_l = volume_ml/1000

# Do the calculation
mass = conc_molar * volume_l * molecular_mass

# Write the output

print("To create",volume_ml,"ml of a",
conc_molar, "M solution of a compound with molecular mass",
molecular_mass,"you need",mass,"g of material")