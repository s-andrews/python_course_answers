#!python

# This script takes in an organism genus and
# species and correctly formats it.  The genus
# should have an initial capital letter, and 
# the genus should be all lowercase.

# Collect the input
genus = input("Enter genus: ")
species = input("Enter species: ")

# Now we need to convert them to the correct 
# capitalisation.
# 
# These are both str variables so we can use
# help(str) to see what we can do with them.
# From there we find:
#
# capitalize(self, /)
#   Return a capitalized version of the string.
#
#   More specifically, make the first character 
#   have upper case and the rest lower case.
#
# ...and also...
# 
# lower(self, /)
#   Return a copy of the string converted to 
#   lowercase.


# These are both class methods (functions) so
# we need to call them from the data rather than
# as standalone functions

genus_fixed = genus.capitalize()
species_fixed = species.lower()

# Now we can print the output

print("The fixed version of",genus,species,"is",genus_fixed,species_fixed)


