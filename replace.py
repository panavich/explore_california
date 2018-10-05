import re
import os
import sys

print('Number of args is:', len(sys.argv))

filelist = sys.argv
del filelist[0]

for arg in filelist:
    print('Running replacement on file:', arg)

    os.rename(arg, arg+'.old') 

    outfile = open(arg, '+w')
    infile = open(arg+'.old', '+r')

    print('Opened file:', arg+'.old')

    for line in infile:
        if (re.search('4315', line)):
            newline = re.sub('4315', '4314', line)
            outfile.write(newline)
        else:
            outfile.write(line)

    infile.close()
    outfile.close()
   


