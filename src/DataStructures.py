'''
Created on Oct 8, 2013

@author:    Rahul Varanasi - 800807351
            Kshitiz Gupta - 800803559
            Manmohan Chaubey - 800832048
'''
'''
This program demonstrates the various Data Structures available in Python Language.
This program has been written in a way which involves minimum user interaction yet demonstrates the usage of Data Structures.
Due to this limitation, all functions/features of the Data Structures cannot be shown or implemented.
'''
'''
This program accepts a certain number of values and puts them into various Data Structures and performs operations on them.
'''

import sys
from collections import deque


# Wrapper class for List
class List():
    # Function to initialize the list    
    def __init__(self):
        self.myList = []
    
    # Function to add values to the list    
    def add(self, userInput):
        self.myList.insert(len(self.myList), userInput)        
    
    # Function to print the list    
    def printList(self):
        print self.myList
    
    # Function to sort the list    
    def sortList(self):
        self.myList.sort()
    
    # Function to reverse the list    
    def reverseList(self):
        self.myList.reverse()
    
    # Function to perform various operations on List type    
    def opsOnList(self):
        print "\nOperations on List:"
        
        print "Print List: ",
        self.printList()    
        
        print "Reverse List: ",
        self.reverseList()
        self.printList()
        
        print "Sort List: ",
        self.sortList()
        self.printList()


# Wrapper class for Stack
class Stack():
    # Function to initialize the stack
    def __init__(self):
        self.myStack = []        
    
    # Function to push a value on to the stack
    def pushStack(self, userInput):
        self.myStack.append(userInput)
    
    # Function to print the values in the stack
    def printStack(self):
        print self.myStack
    
    # Function to pop the stack
    def popStack(self):
        while self.myStack:
            print self.myStack.pop(),
        print ""
    
    # Function to perform various operations on the stack    
    def opsOnStack(self):
        print "\nOperations on Stack:"
        
        print "Print Stack: ",
        self.printStack()
        
        print "Pop Stack: ",
        self.popStack()
    

# Wrapper class for Queue    
class Queue():
    # Function to initialize the queue
    def __init__(self):
        self.myQueue = deque([])        
    
    # Function to push a value into the queue
    def pushQueue(self, userInput):
        self.myQueue.append(userInput)        
    
    # Function to print the values in the queue
    def printQueue(self):
        print self.myQueue
    
    # Function to pop all the values from the queue
    def popQueue(self):
        while self.myQueue:
            print self.myQueue.popleft(),
        print ""
        
    # Function to perform various operations on the queue
    def opsOnQueue(self):
        print "\nOperations on Queue:"
        
        print "Print Queue: ",
        self.printQueue()
        
        print "Empty Queue: ",
        self.popQueue()
            
            
# Wrapper class for Set            
class Set():
    # Function to initialize set
    def __init__(self):
        self.mySet = set()
        
    # Function to add a value into the set
    def add(self, userInput):
        self.mySet.add(userInput)
        
    # Function to print all the values in the set
    def printSet(self):
        print self.mySet
        
    # Function to empty the set
    def emptySet(self):
        while self.mySet:
            print self.mySet.pop(),
        print ""
    
    # Function to perform various operations on the set        
    def opsOnSet(self):
        print "\nOperations on Set:"
        
        print "Print Set: ",
        self.printSet()
        
        print "Pop Set: ",
        self.emptySet()


# Wrapper class for the Dictionary
class Dictionary():
    # Function to initialize the dictionary
    def __init__(self):
        self.myDictionary = {}
        
    # Function to add an entry
    def addEntry(self, userInput):
        self.myDictionary[userInput] = str("value_" + userInput)
    
    # Function to print the dictionary        
    def printDictionary(self):
        print self.myDictionary
        
    # Function to clear the dictionary
    def clearDictionary(self):
        self.myDictionary.clear()
        
    # Function to perform various operations on the dictionary
    def opsOnDictionary(self):
        print "\nOperations on Dictionary:"
        
        print "Print Dictionary: ",
        self.printDictionary()
        
        print "Clear Dictionary: ",
        self.clearDictionary()
        self.printDictionary()

# Main Function
def main():
    print "This program simulates the operations that can be performed on the Data Structures available in Python."
    print "\nIt will load some values into 'list', 'stack', 'queue', 'set' and 'dictionary'",
    print "and output the basic operations that can be performed on those Data Structures."
    print "\nValues of any type can be safely added to the above Data Structures because raw input is treated as String."
    print "\nPlease note that all the values are treated as Strings. Hence any sorting operation will be performed",
    print "based on Strings and not based on numbers even if the input is a number."
    
    # Create the Data Structure objects   
    myList = List()
    myStack = Stack()
    myQueue = Queue()
    mySet = Set()
    myDictionary = Dictionary()
    
    while True:
        try:
            userInput = raw_input("\nPlease enter the number of values you want to add to the Data Structures: ")
            valueCount = int(userInput)
            break
        except:
            print "Invalid input. Enter an integer." 
    
    try:
        i = 1
        print "\nPlease enter", valueCount, "values."
        while i <= valueCount:
            print "Input Value", i, ": ",
            userInput = raw_input()
            if userInput.strip() == "":
                print "Input value cannot be empty."
                continue
            
            # Add the user inputs to the Data Structures
            myList.add(userInput)
            myStack.pushStack(userInput)
            myQueue.pushQueue(userInput)
            mySet.add(userInput)
            myDictionary.addEntry(userInput)

            i += 1        
    except Exception, e:
        print "Unknown Error:\n", str(e)
        sys.exit(1)
    
    # Perform operations on the Data Structures    
    myList.opsOnList()
    myStack.opsOnStack()
    myQueue.opsOnQueue()
    mySet.opsOnSet()
    myDictionary.opsOnDictionary()

main()