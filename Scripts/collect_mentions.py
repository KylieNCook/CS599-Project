#import modules and libraries
import os, csv, random

# declare important variables
directory = '/projects/canis/twitter_covid/data'
mentions_all = {}
##### start main code #####

# collect all file names from the first week of 9/2021
files = sorted(filename for filename in os.listdir(directory) if filename >= '2022_01_01' and filename <= '2022_01_08')

# open each file and collect all usernames from the file
for filename in files:
    print('Collecting usernames from ' + filename)

    # open each file
    with open(directory + '/' + filename) as csvfile:
        
        # get lines of the file
        lines = csvfile.readlines()
        
        # generate a list of usernames from the files
        mentions = [[line.split('\t')[6], line.split('\t')[14]] for line in lines if len(line.split('\t')) > 14]
        

f = open('sample.txt', 'w')
f.write(str(mentions_all))
f.close()

