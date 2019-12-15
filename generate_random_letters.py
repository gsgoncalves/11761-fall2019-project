import argparse
import collections, sys
from nltk.corpus import brown
import numpy as np

CHAR_THRESHOLD = 100000


def get_char_counts(openfile):
    word_counts = sorted(collections.Counter(c for l in openfile for c in l).items())
    counts = dict()
    for word_count in word_counts:
        if word_count[0].isalpha() or word_count[0].isspace():
            counts[word_count[0]] = float(word_count[1])
    counts[' '] = brown.raw().count(' ')
    corpus_size = float(len(brown.raw()))
    return corpus_size, counts


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r1outfile', help='letter dstro based generated rand file')
    parser.add_argument('-r2outfile', help='python random seq file')
    args = parser.parse_args()

    # Get frequencies
    corpus_size, counts = get_char_counts(brown.words())

    # Calculate cumulative probs
    sorted_chars = sorted(counts.keys())
    cumulative_prob = [None] * len(sorted_chars)

    cumulative_prob[0] = counts[sorted_chars[0]]/corpus_size

    for i in range(1, len(sorted_chars)):
        cumulative_prob[i] = cumulative_prob[i-1] + counts[sorted_chars[i]]/corpus_size

    # Generate random sequence of characters based on that distro
    rand_sequence = ""
    while len(rand_sequence) < CHAR_THRESHOLD:
        v = np.random.uniform()
        for j in range(len(cumulative_prob)):
            if cumulative_prob[j] >= v:
                rand_sequence += sorted_chars[j]
                break

    with open(args.r1outfile, 'w', encoding='utf8') as f:
        f.write(rand_sequence + '\n')

    rand_sequence = ""

    for i in range(CHAR_THRESHOLD):
        v = np.random.randint(0, len(sorted_chars))
        rand_sequence += sorted_chars[v]

    with open(args.r2outfile, 'w', encoding='utf8') as f:
        f.write(rand_sequence + '\n')

    sys.exit(0)
