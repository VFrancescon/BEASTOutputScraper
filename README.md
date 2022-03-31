# BEAST Output Scraper


Quick and dirty Python script to scrape all the info from a BEAST log into a csv file.


BEAST is a software developed for the University of Leeds for the COMP5400M module.


# File Structure
* scaper.py
Takes all the info out of the txt dump and formats it in a csv so we can plot it.
Might use matplotlib later, or just do the plotting in MATLAB.


* chaseScraper.py
Specifically for the chase demo. Takes the info and splits it into two csv files.


* BeastPlotter.m 
Takes the csv outputted by the scaper script and plots is.


* ChaseBeastPlotter100/2000.m
Takes the pairs of csv outputted by the chaseScraper script and plots them


# Usage
Usage is detailed in each individual script in the top line comments.


# Author
Vittorio Francescon

University of Leeds