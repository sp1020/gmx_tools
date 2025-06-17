
#!/usr/bin/env python3
from collections import defaultdict
import argparse

def reindex_pdb(input_path, output_path):
    """
    Reindexing resi and atom number. 
    """
    atom_serial = 1
    # For each chain, map old (resseq, icode) → new resseq
    resi = 1
    cur_resi = ''

    with open(input_path) as inp, open(output_path, "w") as out:
        for line in inp:
            rec = line[:6]
            if rec in ("ATOM  ", "HETATM"):
                # parse old residue identity
                # chain_id    = line[21]                # column 22
                chain_id = 'A'
                old_resseq  = int(line[22:26])        # columns 23-26
                i_code      = line[26]                # column 27
                key = (old_resseq, i_code)

                # assign new residue number if unseen
                if old_resseq != cur_resi: 
                    cur_resi = old_resseq
                    new_resseq = resi 
                    resi += 1

                # build new line
                prefix    = line[:6]                   # record name
                new_serial = f"{atom_serial:5d}"       # cols 7-11
                mid       = line[11:21]                # cols 12-21
                new_res    = f"{new_resseq:4d}"        # cols 23-26
                i_code_chr = line[26]                  # col 27
                suffix    = line[27:]                  # rest of line

                new_line = (
                    prefix
                    + new_serial
                    + mid
                    + chain_id
                    + new_res
                    + i_code_chr
                    + suffix
                )
                out.write(new_line)
                atom_serial += 1
            else:
                # leave everything else untouched
                out.write(line)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Reindex PDB."
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Input PDB file"
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Output PDB file"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    print("Input PDB:", args.input)
    print("Output PDB:", args.output)
    
    reindex_pdb(args.input, args.output)
