#!python
from pathlib import Path
import gzip
import re

bacterial_folder = Path("c:/Users/andrewss/Desktop/Introduction to Python/Python Intro Data/Bacteria")

for annotation_file in bacterial_folder.glob("*gtf.gz"):
    species_name = annotation_file.name.replace(".gtf.gz","")

    gene_count = 0
    largest_gene_size = 0
    largest_gene_name = ""

    with gzip.open(annotation_file,"tr",encoding="UTF-8") as af:
        for line in af:
            if line.startswith("#"):
                continue

            sections = line.split("\t")

            if sections[2] == "gene":
                gene_count += 1

                gene_size = 1+ int(sections[4]) - int(sections[3])

                if gene_size > largest_gene_size:
                    largest_gene_size = gene_size
                    hit = re.search("gene_name (\S+);",sections[8])
                    if hit is not None:
                        largest_gene_name = hit.groups()[0]

                    else:
                        # It's an unnamed gene so we'll get the id instead
                        hit = re.search("gene_id (\S+);",sections[8])
                        if hit is not None:
                            largest_gene_name = hit.groups()[0]
                        else:
                            print("Couldn't find gene name from "+sections[8])


    largest_gene_name = largest_gene_name.replace('"','')

    print(f"Species: {species_name}\nGenes: {gene_count}\nLargest Gene: {largest_gene_size}\nLargest Name: {largest_gene_name}\n")