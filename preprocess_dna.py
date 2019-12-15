import sys
import argparse

CHAR_THRESHOLD = 100000


def read_and_write_data(in_file, out_file):
    char_counter = 0
    with open(out_file, 'w', encoding='utf8') as out:
        with open(in_file, 'r', encoding='utf8') as f:
            for line in f:
                if '>' in line:
                    continue
                char_counter += len(line)
                out.write(line)
                if char_counter > CHAR_THRESHOLD:
                    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-infile', help='input data file')
    parser.add_argument('-outfile', help='output file')
    args = parser.parse_args()

    read_and_write_data(args.infile, args.outfile)

    sys.exit(0)
