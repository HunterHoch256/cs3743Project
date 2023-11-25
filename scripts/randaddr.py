# randaddr.py
# A script that appends a random value (from within a given range) to the end of a CSV file - comma assumed to be there
import random
import sys

if ( len(sys.argv) < 5 ):
    print( "randaddr.py syntax: ./randaddr.py <input file> <output file> <start range> <end range>")
    sys.exit(1)

# 1. input file
input_file = sys.argv[1]
# 2. output file
output_file = sys.argv[2]
# 3. start range
start_range = int( sys.argv[3] )
# 4. end range
end_range = int( sys.argv[4] )

# read in file, append a randomly generated number to the end
with open( input_file, 'r', encoding='utf-8' ) as inf:
    with open( output_file, 'w', encoding='utf-8' ) as outf:
        for inline in inf:
            # Strip newline, add random number in range, add newline
            outline = inline.rstrip() + str( random.randrange( start_range, end_range ) ) + '\n'

            outf.write( outline )