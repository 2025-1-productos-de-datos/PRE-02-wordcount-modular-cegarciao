

from ._internals.write_count_words import write_count_words
from ._internals.read_all_lines import read_all_lines
from ._internals.preprocess_lines import preprocess_lines
from ._internals.split_into_words import split_into_words
from ._internals.count_words import count_words


def main():

    input_folder = "data/input"
    output_folder = "data/output"

    all_lines = read_all_lines(input_folder)
    all_lines = preprocess_lines(all_lines)
    words = split_into_words(all_lines)
    counter = count_words(words, output_folder)
    write_count_words(counter)


if __name__ == "__main__":
    main()
