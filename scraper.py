# scraper.py
# Author: Vittorio Francescon
#  for: University of Leeds
# Description:
# Simple scraper to convert a log dump from BEAST into a csv format
#

import sys
def main():
    output_filename = ""
    first_line = "Generation, Avg Fitness, Best Fitness\n"

    if(len(sys.argv)) == 3:
        output_filename = sys.argv[2]
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