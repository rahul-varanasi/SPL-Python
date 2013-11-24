'''
Created on Oct 8, 2013

@author:    Rahul Varanasi - 800807351
            Kshitiz Gupta - 800803559
            Manmohan Chaubey - 800832048
'''
'''
This program demonstrates the File IO available in Python.
'''
'''
This program is written in a way which demonstrates File Reading, File Writing, File Appending and File Copying in Python.
This program assumes input.txt and append.txt and available in the same directory in which the source files are present.
If these two files are not present, the program will break!
'''

import shutil

# Function to read file
def readFile():
    try:
        print "Reading input.txt File:\n"
        f = open('input.txt', 'r')
        for line in f:
            print line,
        f.close()
    except Exception, e:
        print "IOError: ", str(e)
    print ""


# Function to write to a file
def writeFile():
    try:
        print "\nWriting data to output.txt File:"
        f = open('output.txt', 'w+')
        userInput = raw_input("\nEnter some data that will be stored in the output file:\n")
        f.write(userInput)
        f.close()
        
        print "\nData written to File:"
        f = open('output.txt', 'r')
        for line in f:
            print line,
        f.close()
    except Exception, e:
        print "IOError: ", str(e)
    print ""

# Function to append data to a file
def appendFile():
    try:
        print "\nAppending data to append.txt File:"
        f = open('append.txt', 'a')
        userInput = raw_input("\nEnter some data that will be appended to the append file:\n")
        f.write(userInput)
        f.close()
        
        print "\nData written to File:"
        f = open('append.txt', 'r')
        for line in f:
            print line,
        f.close()
    except Exception, e:
        print "IOError: ", str(e)
    print ""
        
        
# Function to copy a file        
def copyFile():
    try:
        print "\nCopying input.txt to copiedfile.txt"
        shutil.copyfile('input.txt', 'copiedfile.txt')
        print "File Copied!"
        
        print "Reading data of copiedfile.txt:"
        f = open('copiedfile.txt', 'r')
        for line in f:
            print line,
        f.close()        
    except Exception, e:
        print "IOError: ", str(e)  
    print ""

# Main Function
def main():
    readFile()
    writeFile()
    appendFile()
    copyFile()
    
    print "\nProgram complete. Have a good day!"
    
main()