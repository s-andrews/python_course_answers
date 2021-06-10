#!python
import random

# This script takes in a reference DNA sequence
# and simulates a new sequence of a specified
# length which has the same composition

reference_sequence = "GATCXGATTTAGATATXXTAAGATAGTGACTAG"
simulated_length = 20

# Force the data types
reference_sequence = reference_sequence.upper()
simulated_length = int(simulated_length)

# Count the bases
a_count = reference_sequence.count("A")
c_count = reference_sequence.count("C")
t_count = reference_sequence.count("T")
g_count = reference_sequence.count("G")

other_count = len(reference_sequence) - (a_count+c_count+g_count+t_count)

print("Composition is A=",a_count," G=",g_count," C=",c_count," T=",t_count," Other=",other_count, sep="")


weights = [g_count,a_count, t_count, c_count]
bases = ["G","A","T","C"]

simulated_seq = random.choices(bases, weights, k=simulated_length)

print("Simulated seq",simulated_seq)
