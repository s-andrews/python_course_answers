#!python

# We're going to ask the user for a set
# of 5 animals, and then we're going to 
# see whether the sixth animal they provide
# is one they've mentioned before or not.

animal_set = set()

animal_set.add(input("Animal 1: ").lower())
animal_set.add(input("Animal 2: ").lower())
animal_set.add(input("Animal 3: ").lower())
animal_set.add(input("Animal 4: ").lower())
animal_set.add(input("Animal 5: ").lower())

print("")

query = input("Query Animal: ")

found = query.lower() in animal_set

print("Was",query,"found?",found)