import argparse

def remove_duplicates_and_empty(input_file, remove_duplicates, remove_empty):
    lines_seen = set()  # To keep track of lines we have seen before

    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    with open(input_file, 'w') as outfile:
        for line in lines:
            if remove_duplicates:
                # Remove duplicate lines
                if line not in lines_seen:
                    lines_seen.add(line)
                    outfile.write(line)
            elif remove_empty:
                # Remove empty lines
                if line.strip():  # Check if the line is not empty after stripping whitespace
                    outfile.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove duplicate and/or empty lines from a file.")
    parser.add_argument("input_file", help="Input file name")
    parser.add_argument("--duplicate", type=int, choices=[0, 1], default=0, help="Remove duplicate lines (1 for yes, 0 for no)")
    parser.add_argument("--empty", type=int, choices=[0, 1], default=0, help="Remove empty lines (1 for yes, 0 for no)")

    args = parser.parse_args()
    
    remove_duplicates_and_empty(args.input_file, args.duplicate, args.empty)
