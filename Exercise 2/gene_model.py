#!python

# We're going to build a multi-level data structure
# to hold the information about a gene.

# The top level structure will be a dictionary

gene = {
    "Name": "Nanog",
    "Description": "Nanog homeobox",
    "Location": {
        "Chromosome": "12",
        "Start": 7_787_794,
        "End": 7_799_146,
        "Strand": "Forward"
    },
    "Transcripts" : []
}

# Now we can add the details of the transcripts
gene["Transcripts"].append({
    "Name": "NANOG-201",
    "ID": "ENST00000229307.9",
    "Length": 5182,
    "Amino Acids": 305
})

gene["Transcripts"].append({
    "Name": "NANOG-202",
    "ID": "ENST00000526286.1",
    "Length": 870,
    "Amino Acids": 289
})

gene["Transcripts"].append({
    "Name": "NANOG-204",
    "ID": "ENST00000541267.5",
    "Length": 836,
    "Amino Acids": 186
})

gene["Transcripts"].append({
    "Name": "NANOG-203",
    "ID": "ENST00000526434.2",
    "Length": 558,
    "Amino Acids": 0
})


# Now we've built the data structure we
# can query it

# Get the length of the last transcript
print("Last transcript length:", gene["Transcripts"][-1]["Length"])

# Reconstruct the location
location = gene["Location"]
print(location["Chromosome"],location["Start"],location["End"],location["Strand"],sep=":")




