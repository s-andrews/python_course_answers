#!python
from pathlib import Path

annotation_file = "genome_annotation.txt"
hits_file = "statistical_hits.txt"
out_file = "annotated_statistical_hits.txt"

base_folder = Path("c:/Users/andrewss/Desktop/Introduction to Python/Python Intro Data")


annotation = {}
annot_headers = []

with open(base_folder/annotation_file) as annot:
    for i,line in enumerate(annot):
        line = line.strip()
        if i==0:
            annot_headers = line.split("\t")
            continue

        sections = line.strip().split("\t")
        gene_annot = {}
        for i,value in enumerate(annot_headers):
            gene_annot[annot_headers[i]] = sections[i]

        annotation[sections[0]] = gene_annot

# Now we can read and annotate the hits

with open(base_folder/hits_file) as hits:
    with open(base_folder/out_file, "w") as outfile:
        for i,line in enumerate(hits):
            line = line.strip()

            if i==0:
                headers = line.split("\t")
                headers.extend(annot_headers)
                print("\t".join(headers), file=outfile)

            else:
                line_data = line.split("\t")
                for key in annot_headers:
                    line_data.append(annotation[line_data[0]][key])
                
                print("\t".join(line_data),file=outfile)
