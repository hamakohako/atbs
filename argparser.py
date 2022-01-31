#!/usr/bin/env python
# Sample python argument parser for command line options

# Import the argparse module
import argparse

# create argument parser object
parser = argparse.ArgumentParser(description='Reads a file in reverse')

# add positional arguments, this will be required when running the program
parser.add_argument('filename', help='The file to read')
# add optional arguments
parser.add_argument('--limit', '-l', type=int, help='Number of lines to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.1')

# Parse arguments - call parse_args() to initialize the object / attributes added
args = parser.parse_args()

# now that the parser has been created, lets create teh sample program
# open the file, read all lines and store contents in reverse
with open(args.filename) as fil:
    lines = fil.readlines()
    lines.reverse()

# if the limit argument is supplied, show only lines up to the limit specified
if args.limit:
    lines = lines[:args.limit]

# iterate through the lines, strip out leading/trailing spaces
for line in lines:
    print(line.strip())
    # print(line.strip()[::-1])