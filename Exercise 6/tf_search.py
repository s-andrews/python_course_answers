#!python
import argparse
import sys
from pathlib import Path

def main():
    options = parse_options()
    sequence = read_sequence(options.infile)

    if not options.quiet:
        print(f"Found sequence {sequence[0]} with length {len(sequence[1])}",file=sys.stderr)

    tf_list = read_tfs(options.tfs)

    if not options.quiet:
        print(f"Found conensus sequences for {' '.join([x['name'] for x in tf_list])}")


def read_tfs(tf_string):

    tf_file = Path("c:/Users/andrewss/Desktop/Introduction to Python/Python Intro Data/Transcription Factors/human_tf_consensus.tsv")
    
    tfs_to_keep = tf_string.split(",")

    tf_list = []

    with open(tf_file) as intf:

        # Discard the header
        intf.readline()

        for line in intf:
            sections = line.split("\t")
            name = sections[1].split(":")[1]
            consensus = sections[2].upper()

            if name in tfs_to_keep:
                tf_list.append({"name":name, "consensus":consensus, "regex":make_regex(consensus)})

    return tf_list


def make_regex(consensus):
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
    for letter in consensus:
        if letter in iupac_codes:
            built_regex += iupac_codes[letter]
        else:
            built_regex += letter

    return built_regex

def read_sequence(file):
    with open(file) as fh:
        header = fh.readline()
        seq_id = header.strip().split(" ")[0][1:]

        sequence = ""
        for line in fh:
            line = line.strip()
            sequence += line

    return (seq_id,sequence)




def parse_options():
    parser = argparse.ArgumentParser(description="Search for Transcription Factor Binding Sites")

    parser.add_argument("infile",help="FastA file of DNA sequence to search")
    parser.add_argument("outfile",help="File to write search results to")

    parser.add_argument("--tfs",help="Comma separated list of transcription factors to search with")
    parser.add_argument("--quiet",help="Suppress progress messages", action="store_true")

    return parser.parse_args()

if __name__ == "__main__":
    main()