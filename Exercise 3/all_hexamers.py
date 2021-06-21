#!python

# We want to create and print the full set of
# all possible hexamers (6-letter DNA sequences)

# We'll start with a small list containing the 4
# DNA bases.
bases = ['G','A','T','C']


# For our output we're going to start by making a
# copy of the 1-mer data
hexamers = bases.copy()

# We now want to extend our output 5 times using 
# each possible base in each extension.
for _ in range(5):
    # We make up an extended set of data
    extended = []

    # We add each base to the starting sequences
    for start in hexamers:
        for base in bases:
            extended.append(start+base)

    # We replace the list of growing hexamers
    # with the extended list we just made
    hexamers = extended


# Finally we print out the results.
for i,hexamer in enumerate(hexamers):
    print(i,hexamer)

