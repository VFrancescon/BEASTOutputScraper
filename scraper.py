# scraper.py
# Author: Vittorio Francescon
#  for: University of Leeds
# Description:
# Simple scraper to convert a log dump from BEAST into a csv format
#

##
# USAGE:
# run the script giving a txt file as argument
# optionally, give a output file name (fout) as well
# the program will output two CSV files in csv_outs/ with file names foutPREDATOR/PREY.csv
##

##
# NOTE:
# this is not a programming assignment or module and the script is extremely simple
# hence I will not be commenting it.
# only note is that the actual parsing section is taken from stack overflow
# https://stackoverflow.com/questions/4289331/how-to-extract-numbers-from-a-string-in-python
##

import sys
def main():
    output_filename = ""
    first_line = "Generation, AvgFitness, BestFitness\n"

    if(len(sys.argv)) == 3:
        output_filename = "csv_outs/" + sys.argv[2] + ".csv"
    else:
        output_filename = "output.csv"
    fileINPUT = open(sys.argv[1], 'r')
    # file_read = fileINPUT.readline()

    #split_list = string.split(" ")
    #print(split_list)

    line_parsed = []
    indeces = []
    avg_fit = []
    best_fit = []
    while True:
        i = fileINPUT.readline()
        if not i:
            break
        for t in i.split():
            try:
                line_parsed.append(float(t))          
            except ValueError:
                pass
        if not line_parsed:
            continue
        # print(line_parsed[0])
        
        indeces.append(line_parsed[0])
        avg_fit.append(line_parsed[1])
        best_fit.append(line_parsed[2])
        # print(second_list[counter])
        # counter += 1
        # all_lines.append(line_parsed)

        line_parsed.clear()
    fileINPUT.close()


    fileOUTPUT = open(output_filename, "w")
    fileOUTPUT.write(first_line)

    for i in range(len(indeces)):
        fileOUTPUT.write( str(int(indeces[i])) + "," + str(avg_fit[i]) + "," + str(best_fit[i]) + "\n")
 
if __name__ == "__main__":
    main()