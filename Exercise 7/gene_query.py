import requests, sys
from Bio import SeqIO
import io
import argparse
import sys

def main():
    options = get_options()
    gene_names = get_gene_names(options)

    gene_info = []

    for gene_name in gene_names:
        options.quiet or print(f"Getting id for {gene_name}", file=sys.stderr)
        gene_id = get_gene_id(gene_name)
        options.quiet or print(f"Found id {gene_id} for {gene_name}", file=sys.stderr)
        transcript_info = get_transcript_info(gene_id)
        options.quiet or print(f"Found {len(transcript_info)} transcripts for {gene_name}", file=sys.stderr)

        gene_info.append({"gene":gene_name, "id":gene_id, "transcripts":transcript_info})

    options.quiet or print(f"Writing results to {options.outfile}", file=sys.stderr)
    write_output(gene_info,options.outfile)
    options.quiet or print(f"All Finished", file=sys.stderr)

def get_options():
    """
    Get the command line options for the program
    """
    parser = argparse.ArgumentParser(description="Get transcript details from Ensembl")

    parser.add_argument("--genes",help="Genes to query", nargs="+", type=str)
    parser.add_argument("--outfile",help="File to write search results to", type=str, default="results.txt")

    parser.add_argument("--quiet",help="Suppress progress messages", action="store_true")

    return parser.parse_args()

def get_gene_names(options):
    if options.genes:
        return options.genes

    gene_names = []

    while True:
        gene = input("Enter a gene name: ")
        gene = gene.strip()
        if gene:
            gene_names.append(gene)
        else:
            break
    
    if not gene_names:
        raise ValueError("No genes to process")

    return gene_names


def get_gene_id(gene_name):
    # Set up the Ensembl API query
    server = "https://rest.ensembl.org"

    # Build the query, including the gene name they supplied
    ext = "/xrefs/symbol/homo_sapiens/"+gene_name+"?external_db=HGNC"

    # Make the query
    r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})

    # Check it worked
    if not r.ok:
        r.raise_for_status()
        sys.exit()

    # Get the data structure the server returned
    decoded = r.json()
    # Extract the gene id from the first hit we got back
    gene_id = decoded[0]['id']

    return gene_id

def get_transcript_info(gene):
    # Set up the Ensembl API query
    server = "https://rest.ensembl.org"

    # Make up the query to the sequence retrieval system
    ext = "/sequence/id/"+gene+"?type=cdna&multiple_sequences=1"
    
    # Run the query
    r = requests.get(server+ext, headers={ "Content-Type" : "text/x-fasta"})
    
    # Check it worked
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    
    # Turn our result into something that looks like a file
    s = io.StringIO(r.text)

    # Parse the result as a fasta file
    fasta = SeqIO.parse(s,"fasta")

    transcripts = []

    # Iterate though the sequences in the file
    for f in fasta:
        # Collect the name and length of the transcript 
        name = f.id
        length = len(f)
        gc = get_gc(f)

        transcripts.append({
            "name": name,
            "length": length,
            "gc": gc
        })

    return transcripts

def get_gc(seq):
    g_count = seq.seq.upper().count("G")
    c_count = seq.seq.upper().count("C")

    percent_gc = 100*(g_count+c_count) / len(seq)

    return percent_gc


def write_output(genes,outfile):
    with open(outfile,"w") as out:

        line = ["gene_name","gene_id","transcript_name","length","gc"]
        print("\t".join(line),file=out)

        for gene in genes:
            gname = gene["gene"]
            gid = gene["id"]
            for transcript in gene["transcripts"]:
                tname=transcript["name"]
                length=transcript["length"]
                gc=transcript["gc"]

                line = [gname,gid,tname,length,round(gc,1)]
                print("\t".join([str(x) for x in line]),file=out)


if __name__ == "__main__":
    main()


