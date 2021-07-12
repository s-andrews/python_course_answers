#!python
import sys
from tf_search import parse_options, read_tfs, search_tfs, write_hits
import gzip


def main():
    options = parse_options()

    tf_list = read_tfs(options.tfs)

    if not options.quiet:
        if options.tfs:
            print(f"Found conensus sequences for {' '.join([x['name'] for x in tf_list])}", file=sys.stderr)

        else:
            print(f"Searching with all {len(tf_list)} transcription factors",file=sys.stderr)


    tf_hits = []

    with gzip.open(options.infile, "rt", encoding="UTF-8") as infh:
        for sequence in read_sequence(infh):
            these_tf_hits = search_tfs(sequence,tf_list)

            if not options.quiet:
                print(f"Found {len(these_tf_hits)} hits in {sequence[0]}",file=sys.stderr)

            tf_hits.extend(these_tf_hits)

    if not options.quiet:
        print(f"Found {len(tf_hits)} hits in the search", file=sys.stderr)

    if tf_hits:
        write_hits(tf_hits,options.outfile)

    else:
        print(f"No hits to report", file=sys.stderr)

    if not options.quiet:
        print(f"Wrote hits to {options.outfile}")


def read_sequence(fh):
    seq_id = ""
    sequence = ""

    for line in fh:
        line = line.strip()
        if seq_id == "":
            seq_id = line.split(" ")[0][1:]
            continue

        if line.startswith(">"):
            yield((seq_id,sequence))
            seq_id = line.split(" ")[0][1:]
            sequence = ""
        else:
            sequence += line

    return((seq_id,sequence))

if __name__ == "__main__":
    main()