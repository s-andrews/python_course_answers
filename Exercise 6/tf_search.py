#!python
import argparse
import sys
from pathlib import Path
import re

def main():
    options = parse_options()
    sequence = read_sequence(options.infile)

    if not options.quiet:
        print(f"Found sequence {sequence[0]} with length {len(sequence[1])}",file=sys.stderr)

    tf_list = read_tfs(options.tfs)

    if not options.quiet:
        if options.tfs:
            print(f"Found conensus sequences for {' '.join([x['name'] for x in tf_list])}", file=sys.stderr)

        else:
            print(f"Searching with all {len(tf_list)} transcription factors",file=sys.stderr)

    tf_hits = search_tfs(sequence,tf_list)

    if not options.quiet:
        print(f"Found {len(tf_hits)} hits in the search", file=sys.stderr)

    if tf_hits:
        write_hits(tf_hits,options.outfile)

    else:
        print(f"No hits to report", file=sys.stderr)

    if not options.quiet:
        print(f"Wrote hits to {options.outfile}")


def write_hits(hits,outfile):
    """
    Take a list of TF search hits and write it to a file

    hits: A list of hits coming from search_tfs
    outfile: The file to write to
    """
    with open(outfile,"w") as out:
        print("\t".join(["SeqName","TFName","Start","End","Consensus","ActualSeq"]),file=out)

        for hit in hits:
            print("\t".join([str(x) for x in hit]),file=out)


def search_tfs (sequence, tfs):
    """
    Perform a search through the named sequence for the set of
    listed transcription factor consensus sequences

    sequence: A tuple of (name, bases) for the sequence
    tfs: A list of transcription factors as returned by read_tfs

    returns: A list of hit lists, each containing
                seq name
                tf name
                start
                end
                consensus seq
                actual seq
    """

    hits = []

    for tf in tfs:
        for rematch in re.finditer(tf['regex'],sequence[1]):
            start = rematch.start()
            end = rematch.end()
            seq = sequence[1][start:end]
            hits.append([sequence[0],tf['name'],start,end,tf['consensus'],seq])

    return hits


def read_tfs(tf_string):
    """
    Read a CSV file of hocomoco transcription factor sequences.  The input
    file is hard coded but you can optionally supply a list of transcription
    factors and only the details for those factors will be returned if the
    list is not empty
    """

    tf_file = Path("c:/Users/andrewss/Desktop/Introduction to Python/Python Intro Data/Transcription Factors/human_tf_consensus.tsv")
    
    tfs_to_keep = []

    if tf_string is not None:
        tfs_to_keep = tf_string.split(",")

    tf_list = []

    with open(tf_file) as intf:

        # Discard the header
        intf.readline()

        for line in intf:
            sections = line.split("\t")
            name = sections[1].split(":")[1]
            consensus = sections[2]

            if name in tfs_to_keep or not tf_string:
                tf_list.append({"name":name, "consensus":consensus, "regex":make_regex(consensus)})

    return tf_list


def make_regex(consensus):
    """
    Turn a consensus sequence into a regex.
    """
    iupac_codes = {
        "M":"[AC]",
        "R":"[AG]", 	
        "W":"[AT]",
        "S":"[CG]",
        "Y":"[CT]",
        "K":"[GT]",
        "V":"[ACG]",
        "H":"[ACT]",
        "D":"[AGT]",
        "B":"[CGT]",
        "N":"[GATC]" 	
    }

    built_regex = ""
    for letter in consensus.upper():
        if letter in iupac_codes:
            built_regex += iupac_codes[letter]
        else:
            built_regex += letter

    return built_regex

def read_sequence(file):
    """
    Read a single sequence from a FastA format file
    """
    with open(file) as fh:
        header = fh.readline()
        seq_id = header.strip().split(" ")[0][1:]

        sequence = ""
        for line in fh:
            line = line.strip()
            sequence += line

    return (seq_id,sequence)




def parse_options():
    """
    Get the command line options for the program
    """
    parser = argparse.ArgumentParser(description="Search for Transcription Factor Binding Sites")

    parser.add_argument("infile",help="FastA file of DNA sequence to search")
    parser.add_argument("outfile",help="File to write search results to")

    parser.add_argument("--tfs",help="Comma separated list of transcription factors to search with (default all)")
    parser.add_argument("--quiet",help="Suppress progress messages", action="store_true")

    return parser.parse_args()


if __name__ == "__main__":
    main()