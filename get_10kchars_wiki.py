import sys
import argparse
import os


CHAR_THRESHOLD = 100000


def read_and_write_data(in_file, out_file):
    char_counter = 0
    with open(out_file, 'w', encoding='utf8') as out:
        with open(in_file, 'r', encoding='utf8') as f:
            for line in f:
                char_counter += len(line)
                out.write(line.strip() + '\n')
                if char_counter > CHAR_THRESHOLD:
                    break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-indir', help='input data file')
    parser.add_argument('-outdir', help='output file')
    args = parser.parse_args()

    for (dirpath, dirnames, filenames) in os.walk(args.indir):
        for filename in filenames:
            read_and_write_data(dirpath + os.sep + filename, args.outdir + os.sep + filename)

    sys.exit(0)
