#import modules and libraries
import os, csv, random

# declare important variables
directory = '/projects/canis/twitter_covid/data'
usernames = []
username_string = ''
duplicates_count = 0
set_count = 0
file_count = 0
##### start main code #####

# collect all file names from the first week of 9/2021
files = sorted(filename for filename in os.listdir(directory) if filename >= '2022_01_01' and filename <= '2022_01_08')

# open each file and collect all usernames from the file
for filename in files:
    file_count += 1
    print('Collecting usernames from ' + filename)

    # open each file
    with open(directory + '/' + filename) as csvfile:
        
        # get lines of the file
        lines = csvfile.readlines()
        
        # generate a list of usernames from the files
        duplicate_usernames = [line.split('\t')[6] for line in lines if len(line.split('\t')) > 6]
        duplicates_count += len(duplicate_usernames)
        set_usernames = list(set(duplicate_usernames))
        usernames += set_usernames

usernames = list(set(usernames))
set_count = len(usernames)
one_percent = int(.01*len(usernames))

sample = random.sample(usernames, one_percent)

f = open('sample.txt', 'w')
f.write(str(sample))
f.close()

print('Duplicate Count = ', duplicates_count)
print('Set Count = ', set_count)
print('Sample Count = ', len(sample))
print('File Count = ', file_count)

print('Done!')
