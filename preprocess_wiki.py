import sys
import argparse
import re
import time


def preprocess_text(in_text):
    # Remove punctuation
    clean_text = re.sub(r"[^\w\d\s]", "", in_text)
    # Remove multiple spaces
    # clean_text = re.sub("/\s\s+/g", " ", clean_text)
    # clean_text = re.sub("/  +/g", " ", clean_text)
    # clean_text = re.sub("/\s{2,}/g", " ", clean_text)
    clean_text = re.sub(" +", " ", clean_text)
    return clean_text


def read_and_write_data(in_file, out_file):
    doc_counter = 0
    start_checkpoint = time.time()
    with open(out_file, 'w', encoding='utf8') as out:
        with open(in_file, 'r', encoding='utf8') as f:
            doc_text = []
            for line in f:
                line = line.strip()
                if line:
                    if '<p>' in line:
                        doc_text *= 0
                    elif '</p>' in line:
                        clean_text = preprocess_text(' '.join(doc_text))
                        out.write(clean_text + '\n')
                        doc_counter += 1
                        if doc_counter % 100000 == 0:
                            print("Processed " + str(doc_counter) + " in " + str((time.time() - start_checkpoint)) + " sec.")
                            start_checkpoint = time.time()
                    else:
                        doc_text.append(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-infile', help='input data file')
    parser.add_argument('-outfile', help='output file')
    args = parser.parse_args()

    read_and_write_data(args.infile, args.outfile)

    sys.exit(0)
