import sys

def count_stats(input_stream):
    lines, words, bytes = 0, 0, 0
    for line in input_stream:
        lines += 1
        words += len(line.split())
        bytes += len(line.encode('utf-8'))
    return lines, words, bytes

def print_stats(lines, words, bytes, name=None):
    print(f"{lines} {words} {bytes}", name if name else '')

if __name__ == "__main__":
    total_lines, total_words, total_bytes = 0, 0, 0
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, 'r') as f:
                lines, words, bytes = count_stats(f)
                print_stats(lines, words, bytes, filename)
                total_lines += lines
                total_words += words
                total_bytes += bytes
        if len(sys.argv) > 2:
            print_stats(total_lines, total_words, total_bytes, "total")
    else:
        lines, words, bytes = count_stats(sys.stdin)
        print_stats(lines, words, bytes)
