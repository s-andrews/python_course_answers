#!python
import random

# This script generates a random genomic position
# from the human genome.

# For consistency I'm going to make all of these strings
chr_names = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","X","Y"]

# I'm also going to need a dictionary of chromosome sizes

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

# Finally we'll make up a small tuple of strands
strands = ("+","-")

# We'll start by selecting a random chromsome
random_chr = random.choice(chr_names)

# Now we can select a random position from within
# the size of that chromsome
random_position = random.randint(1,chr_sizes[random_chr])

# Finally we can pick a random strand
random_strand = strands[random.randint(0,1)]

# Now we can print out the location
print(random_chr,random_strand,random_position,sep=":")


