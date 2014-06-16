#!/usr/bin/python

# This script is used to take a directory of FASTQ files
# and create a csv file with the sample name and FASTQ filename
# It takes as input the name of the direcotry and the output file names
# for the paired end data


import os
import sys

# directory that you want to access to create the csv file from
path=sys.argv[1]
# output file name
outputfile = sys.argv[2]

names_R1 = {}
names_R2 = {}

dirList=os.listdir(path)
for fname in dirList:
    if "fastq" in fname:
        sname = fname.split("_")[0]
        if "_R1_" in fname:
            names_R1[sname] = fname
        elif "_R2_" in fname:
            names_R2[sname] = fname


output = open(outputfile, 'w')

for i in sorted(names_R1.iterkeys()):
    output.write('%s\t%s\t%s\n' % (i, names_R1[i], names_R2[i]))


