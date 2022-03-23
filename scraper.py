# scraper.py
# Author: Vittorio Francescon
#  for: University of Leeds
# Description:
# Simple scraper to convert a log dump from BEAST into a csv format
#

import sys

file1 = open(sys.argv[1], 'r')
# file_read = file1.readline()

#split_list = string.split(" ")
#print(split_list)

line_parsed = []
all_lines_parsed = []
while True:
    i = file1.readline()
    if not i:
        break
    for t in i.split():
        try:
            line_parsed.append(float(t))          
        except ValueError:
            pass
    all_lines_parsed.append(line_parsed)
    print(all_lines_parsed)
    line_parsed.clear()

print(all_lines_parsed[2])