#!python
import random

# We're going to use the previously constructed
# dataset of chromosome lengths
chr_sizes = {
    "1": 248_956_422,
    "2": 242_193_529,
    "3": 198_295_559,
    "4": 190_214_555,
    "5": 181_538_259,
    "6": 170_805_979,
    "7": 159_345_973,
    "8": 145_138_636,
    "9": 138_394_717,
    "10": 133_797_422,
    "11": 135_086_622,
    "12": 133_275_309,
    "13": 114_364_328,
    "14": 107_043_718,
    "15": 101_991_189,
    "16": 90_338_345,
    "17": 83_257_441,
    "18": 80_373_285,
    "19": 58_617_616,
    "20": 64_444_167,
    "21": 46_709_983,
    "22": 50_818_468,
    "X": 156_040_895,
    "Y": 57_227_415
}

# We need a set of positions to test against,
# and we need to count them, so we'll make a 
# dictionary out of them.  Because they'll be
# keys in a dictionary we need them to be tuples
# rather than lists

positions_to_test = {
    ("1",90435481,90535480): 0,
    ("4",121080701,121180700): 0,
    ("5",58203396,58303395): 0,
    ("6",24011285,24111284): 0,
    ("7",27397324,27497323): 0,
    ("9",63677076,63777075): 0,
    ("12",57831538,57931537): 0,
    ("13",80438618,80538617): 0,
    ("16",86177236,86277235): 0,
    ("18",39459388,39559387): 0
}

# Now we start generating random positions and
# seeing if they fall into any of the ranges.
# We stop when any range has 10 hits, and we
# count the total number of attempts

total_attempts = 0

r = random.Random()

while True:

    # We're going to select a random position by picking
    # a random chromsome and then a random position within
    # it.  THis works but it's not really fair as we'll hit
    # the positions in shorter chromsomes more frequently than
    # we'll hit those in longer chromosomes.

    random_chr = r.choice(list(chr_sizes.keys()))
    random_pos = r.randint(1,chr_sizes[random_chr])

    total_attempts += 1

    can_exit = False

    for test_pos in positions_to_test.keys():
        if test_pos[0] != random_chr:
            continue
        if test_pos[1] > random_pos:
            continue
        if test_pos[2] < random_pos:
            continue

        # It's a hit
        positions_to_test[test_pos] += 1

        if positions_to_test[test_pos] == 10:
            can_exit  = True

    if can_exit:
        break    

print("Total attempts",total_attempts)
for pos,count in positions_to_test.items():
    print(pos,count)







