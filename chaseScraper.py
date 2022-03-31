# chaseScraper.py
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
    output_filename1 = ""
    output_filename2 = ""
    first_line = "Generation, AvgFitness, BestFitness\n"

    if(len(sys.argv)) == 3:
        output_filename1 = "csv_outs/" + sys.argv[2] + "PREDATOR.csv"
        output_filename2 = "csv_outs/" + sys.argv[2] + "PREY.csv"
    else:
        output_filename1 = "outputPREDATOR.csv"
        output_filename2 = "outputPREY.csv"
    fileINPUT = open(sys.argv[1], 'r')
    # file_read = fileINPUT.readline()

    #split_list = string.split(" ")
    #print(split_list)

    line_parsed1 = []
    indeces1 = []
    avg_fit1 = []
    best_fit1 = []
    indeces2 = []
    avg_fit2 = []
    best_fit2 = []
    predatorWrite = True
    while True:
        i = fileINPUT.readline()
        if not i:
            break
        for t in i.split():
            try:
                line_parsed1.append(float(t))          
            except ValueError:
                pass
        if not line_parsed1:
            continue
        # print(line_parsed[0])
        
        if predatorWrite:
            indeces1.append(line_parsed1[0])
            avg_fit1.append(line_parsed1[1])
            best_fit1.append(line_parsed1[2])
            predatorWrite = not predatorWrite
        else:
            indeces2.append(line_parsed1[0])
            avg_fit2.append(line_parsed1[1])
            best_fit2.append(line_parsed1[2])
            predatorWrite = not predatorWrite
        # print(second_list[counter])
        # counter += 1
        # all_lines.append(line_parsed)

        line_parsed1.clear()
    fileINPUT.close()


    fileOUTPUT1 = open(output_filename1, "w")
    fileOUTPUT1.write(first_line)
    fileOUTPUT2 = open(output_filename2, "w")
    fileOUTPUT2.write(first_line)

    for i in range(len(indeces1)):
        fileOUTPUT1.write( str(int(indeces1[i])) + "," + str(avg_fit1[i]) + "," + str(best_fit1[i]) + "\n")
 
    for i in range(len(indeces2)):
        fileOUTPUT2.write( str(int(indeces2[i])) + "," + str(avg_fit2[i]) + "," + str(best_fit2[i]) + "\n")
 

if __name__ == "__main__":
    main()