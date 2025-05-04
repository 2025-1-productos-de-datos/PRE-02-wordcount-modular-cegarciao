
import os

from ._internals.write_count_words import write_count_words
from ._internals.read_all_lines import read_all_lines
from ._internals.preprocess_lines import preprocess_lines
from ._internals.split_into_words import split_into_words
from ._internals.count_words import count_words

def main():


    all_lines = read_all_lines()


    all_lines = preprocess_lines(all_lines)


    words = split_into_words(all_lines)


    count_words(words)








# counter={}
# for filename in input_file_list:
#     with open('data/input/'+filename) as f:
#         for l in f:
#             for w in l.split( ):
#                 w = w.lower().strip(",.!?")
#                 counter[w] = counter.get(w, 0) + 1



write_count_words(counter)





if __name__ == "__main__":
    main()