#!python

# We're going to make a 2-level dictionary
# of amino acid properties and then let the
# user ask for the properties of any amino 
# acid.

# I'm going to make an empty dictionary and
# then populate it one amino acid at a time
amino_acids = {}
amino_acids["A"] = {"name":"Alanine",       "weight":89.1}
amino_acids["R"] = {"name":"Arginine",      "weight":174.2}
amino_acids["N"] = {"name":"Asparigine",    "weight":132.1}
amino_acids["D"] = {"name":"Aspartate",     "weight":133.1}
amino_acids["C"] = {"name":"Cysteine",      "weight":121.2}
amino_acids["E"] = {"name":"Glutamate",     "weight":147.1}
amino_acids["Q"] = {"name":"Glutamine",     "weight":146.2}
amino_acids["G"] = {"name":"Glycine",       "weight":75.1}
amino_acids["H"] = {"name":"Histidine",     "weight":155.2}
amino_acids["I"] = {"name":"Isoleucine",    "weight":131.2}
amino_acids["L"] = {"name":"Leucine",       "weight":131.2}
amino_acids["K"] = {"name":"Lysine",        "weight":146.2}
amino_acids["M"] = {"name":"Methionine",    "weight":149.2}
amino_acids["F"] = {"name":"Phenylalanine", "weight":165.2}
amino_acids["P"] = {"name":"Proline",       "weight":115.1}
amino_acids["S"] = {"name":"Serine",        "weight":105.1}
amino_acids["T"] = {"name":"Threonine",     "weight":119.1}
amino_acids["W"] = {"name":"Tryptophan",    "weight":204.2}
amino_acids["Y"] = {"name":"Tyrosine",      "weight":181.2}
amino_acids["V"] = {"name":"Valine",        "weight":117.1}


# Now we can ask the user for an amino acid

chosen_aa = input("Which amino acid? ")

print ("Chosen amino acid=",chosen_aa,sep="")
print ("Full Name=",amino_acids[chosen_aa]["name"],sep="")
print ("Weight=",amino_acids[chosen_aa]["weight"],sep="")



