import argparse
import sys
import re

CHAR_THRESHOLD = 100000


def read_and_write_data(in_file, out_file):
    char_counter = 0
    with open(out_file, 'w', encoding='utf8') as out:
        with open(in_file, 'r', encoding='utf8') as f:
            for line in f:
                line = line.strip()
                if line:
                    if "/*" not in line and "*/" not in line and "//" not in line and "*" != line and "*" != line[0]:
                        text_to_write = line + ' '
                        text_to_write = re.sub(" +", " ", text_to_write)
                        char_counter += len(text_to_write)
                        out.write(text_to_write)
                        if char_counter > CHAR_THRESHOLD:
                            return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-infile', help='input data file')
    parser.add_argument('-outfile', help='output file')
    args = parser.parse_args()

    read_and_write_data(args.infile, args.outfile)

    sys.exit(0)
