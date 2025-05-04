import sys

from ._internals.write_count_words import write_count_words
from ._internals.read_all_lines import read_all_lines
from ._internals.preprocess_lines import preprocess_lines
from ._internals.split_into_words import split_into_words
from ._internals.word_counts import word_counts


def main():

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    all_lines = read_all_lines(input_folder)
    all_lines = preprocess_lines(all_lines)
    words = split_into_words(all_lines)
    counter = word_counts(words)
    write_count_words(counter, output_folder)


if __name__ == "__main__":
    main()
