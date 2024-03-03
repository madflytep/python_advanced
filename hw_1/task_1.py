import sys

def number_lines(input_stream):
    line_number = 1
    for line in input_stream:
        print(f"{line_number}\t{line}", end='')
        line_number += 1

if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file, 'r') as f:
            number_lines(f)
    else:
        number_lines(sys.stdin)
