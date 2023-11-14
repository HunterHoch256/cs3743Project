# nad.py
# An application that uses the heap queue algorithm (described here https://docs.python.org/3/library/heapq.html) to select a given random number of records from the given filename
# (implemented here: https://stackoverflow.com/questions/22130548/extracting-a-random-line-in-a-file-without-loading-the-file-into-ram-in-python).
import heapq
import random
import sys

if( len(sys.argv) < 4 ):
    print( "nad.py syntax: ./nad.py <path to input file> <number of elements to select> <path to output file>" )
    sys.exit(1)

# 1. Input file path
input_file = sys.argv[1]

# 2. Number of elements
num_lines = int( sys.argv[2] )

# 3. Output file path
output_file = sys.argv[3]

# Read input file
with open( input_file, 'r', encoding='utf-8' ) as input_file_obj:
    # the "key" here is supposed to define a function with one parameter, which is used to extract a comparison key for each element.
    # since the key just outputs a random number, the line selection will be random.
    rand_lines = heapq.nlargest( num_lines, input_file_obj, key=(lambda L: random.random()))

# Export to output file
with open( output_file, 'w', encoding='utf-8' ) as output_file_obj:
    [output_file_obj.write(cur_line) for cur_line in rand_lines]