# Name: Alex Austin - Section 2
# CS 110
# Project 1: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq
# 
# This program is based on Michael Ernt's assignment on DNA Analysis 

###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print ("You must supply a file name as an argument when running this program.")
    sys.exit(2)


# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0

# Number of a and t nucleotides seen so far.
at_count = 0
# Number of individual nucleotides
a_count = 0
t_count = 0
g_count = 0
c_count = 0


# for each base pair in the string,
for bp in seq:
    # increment the total number of bp's we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = float(gc_count + 1)
       # next, if the bp is a G or a C,
    if bp == 'A' or bp == 'T':
        # increment the count of at
        at_count = at_count + 1
    #count individual nucleotides
    if bp == 'A':
        a_count = a_count + 1
    if bp == 'T':
        t_count = t_count + 1
    if bp == 'G':
        g_count = g_count + 1
    if bp == 'C':
        c_count = c_count + 1

#Instantiate sum
sum = float(a_count + t_count + g_count + c_count)

# divide the gc_count by the total_count
gc_content = gc_count / sum

# Print the problem number, such as 1b
print("Problem Number: 1b")

# Print the answer
print ("GC-content:", gc_content)

# divide the at_count by the total_count
at_content = float(at_count) / sum

# Print the problem number, such as 2a
print("Problem Number: 2a")

# Print the answers for
print ("AT-content:", at_content)
# Print the answer for 2b
print("Problem Number: 2b")
print ("A count:", a_count)
print ("T count:", t_count)
print ("G count:", g_count)
print ("C count:", c_count)

#2c - sanity check
print("2c. sum is", sum)
print("Total count is: ", total_count)
print("Length is ", len(seq))

#2d Computing AC/GT ratio
ratio = at_content / gc_content
print("2d. Ratio is", ratio)

#2e Categorize organisms
print("2e.")
if gc_content > .60:
#Test if above .60 for high
    print("high GC content")
elif gc_content < .40:
#Test if below .40 for low
    print("low GC content")
else:
#Test if between .60 and .40 for medium
    print("moderate GC content")
