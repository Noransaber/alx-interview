#!/usr/bin/python3
import sys
from collections import defaultdict

def print_statistics(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def main():
    total_size = 0
    status_counts = defaultdict(int)
    lines_processed = 0

    try:
        for line in sys.stdin:
            # Parse the input line
            parts = line.split()
            if len(parts) != 10 or parts[5] != '"GET' or parts[7] != 'HTTP/1.1"':
                continue

            # Extract relevant information
            status_code = parts[8]
            file_size = int(parts[9])

            # Update metrics
            total_size += file_size
            status_counts[status_code] += 1
            lines_processed += 1

            # Print statistics after every 10 lines
            if lines_processed % 10 == 0:
                print_statistics(total_size, status_counts)

    except KeyboardInterrupt:
        # Handle keyboard interruption
        print_statistics(total_size, status_counts)

if __name__ == "__main__":
    main()
