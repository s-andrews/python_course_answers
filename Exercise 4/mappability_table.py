#!python

mappability_data = [
    {"read_length":30, "fragments":1725, "mapped":697},
    {"read_length":40, "fragments":1713, "mapped":794},
    {"read_length":50, "fragments":1689, "mapped":912},
    {"read_length":70, "fragments":1677, "mapped":1103},
    {"read_length":85, "fragments":1660, "mapped":1187}
]

for map_data in mappability_data:

    # Calculate the mappability
    map_data["mappability"] = 100*(map_data["mapped"]/map_data["fragments"])

    # Print out the results
    print(f"{map_data['read_length']} {map_data['fragments']:<4} {map_data['mapped']:<4} {map_data['mappability']:<4.1f}")