import os
import random
import string

def print_files(files, rows, cols, sort_across=False):
    files.sort()

    file_cnt = len(files)
    max_filename_len = max([len(fn) for fn in files])
    # max filename length will determine how many chars can fit in a column
    max_cols = cols // (max_filename_len+1)
    num_chars_per_col = cols // max_cols

    # number of rows used on the terminal
    # increment max rows if the last row is not fully occupied by filenames
    max_rows = file_cnt // max_cols + (1 if file_cnt % max_cols != 0 else 0)

    if not sort_across:
        row_idx = 0
        while row_idx < max_rows:
            col_idx = 0
            while col_idx < max_cols:
                i = row_idx + max_rows * col_idx
                if i < file_cnt:
                    print(files[i].ljust(num_chars_per_col, " "), end="")
                else:
                    # no more filenames to process
                    break
                col_idx += 1
            print()
            row_idx += 1
    else:
        idx = 0
        while idx < file_cnt:
            col_idx = 0
            while idx < file_cnt and col_idx < max_cols:
                print(files[idx].ljust(num_chars_per_col, " "), end="")
                idx += 1
                col_idx += 1
            print()

def generate_random_filenames(num_files):
    random_filenames = []
    for _ in range(num_files):
        fn_len = random.randrange(5, 40)
        s = []
        for _ in range(fn_len):
            i = random.randrange(len(string.ascii_letters))
            s.append(string.ascii_letters[i])
        # filename ends with .t so that we can easily delete by extension
        s.append(".t")
        random_filenames.append("".join(s))
    return random_filenames

def create_random_files(filenames):
    for fn in filenames:
        with open(fn, 'w') as f:
            f.write("")

def main():
    # random_filenames = generate_random_filenames(12)
    # create_random_files(random_filenames)
    size = os.get_terminal_size()
    print_files(os.listdir("./"), size.lines, size.columns, sort_across=False)

if __name__ == "__main__":
    main()