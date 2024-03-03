import sys

def tail(filename=None, line_count=10):
    if filename:
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
            print(f"==> {filename} <==")
            for line in lines[-line_count:]:
                print(line, end='')
        except FileNotFoundError:
            print(f"File not found: {filename}")
    else:
        lines = sys.stdin.readlines()
        for line in lines[-line_count:]:
            print(line, end='')

if __name__ == "__main__":
    filenames = sys.argv[1:]
    line_count = 10 if filenames else 17 
    
    if filenames:
        for filename in filenames:
            tail(filename, line_count)
            if filename != filenames[-1]:
                print()
    else:
        tail(line_count=line_count)
