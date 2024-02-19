import argparse
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
                    print(f"{files[i]:<{num_chars_per_col}}", end="")
                else: break # no more files to process
                col_idx += 1
            print()
            row_idx += 1
    else:
        idx = 0
        while idx < file_cnt:
            col_idx = 0
            while idx < file_cnt and col_idx < max_cols:
                print(f"{files[idx]:<{num_chars_per_col}}", end="")
                idx += 1
                col_idx += 1
            print()

def create_random_files(num_files):
    for _ in range(num_files):
        fn_len = random.randrange(5, 40)
        fn = []
        for _ in range(fn_len):
            i = random.randrange(len(string.ascii_letters))
            fn.append(string.ascii_letters[i])
        # filename ends with .t so that we can easily delete by extension
        fn.append(".t")
        with open("".join(fn), "w") as f:
            f.write("")

def main(dir, across=False):
    create_random_files(400)
    size = os.get_terminal_size()
    print_files(os.listdir(dir), size.lines, size.columns, sort_across=across)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="pyDir.py",
        description="Lists contents of directory"
    )
    parser.add_argument("-d", "--dir", required=True, help="target directory")
    parser.add_argument("-a", "--across", action="store_true", help="sort across instead of vertically")
    args = parser.parse_args()
    main(args.dir, args.across)