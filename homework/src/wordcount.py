
import os


def main():

files_in_input_dir=os.listdir('data/input/')
files_in_input_dir


counter={}
for filename in files_in_input_dir:
    with open('data/input/'+filename) as f:
        for l in f:
            for w in l.split( ):
                w = w.lower().strip(",.!?")
                counter[w] = counter.get(w, 0) + 1


if not os.path.exists('data/output'):
    os.makedirs('data/output')


with open("data/output/results.tsv", "w", encoding="utf-8") as f:
        for key, value in counter.items():
        
            f.write(f"{key}\t{value}\n")


if __name__ == "__main__":
    main()