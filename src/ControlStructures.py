'''
Created on Oct 8, 2013

@author:    Rahul Varanasi - 800807351
            Kshitiz Gupta - 800803559
            Manmohan Chaubey - 800832048
'''
'''
This program is used for using all the control structures provided by Python language.
This program may be written in a better way. 
However, it is written in the way it is to demonstrate the use of all control structures provided by Python language
'''
'''
This program calculates Prime numbers and Fibonacci numbers using naive method.
'''


import sys


# Function to calculate Fibonacci numbers less than the given input, num
def findFibonacciNumbers(num):
    print "\nCalculating Fibonacci numbers till", num, "..."   

    a, b = 0, 1
    fibNumList = [0]
    
    while b <= num:        
        fibNumList.append(b)
        a, b = b, a + b
    
    print "Fibonacci numbers:", fibNumList


# Function to calculate Prime numbers less than the given input, num
def findPrimes(num):
    print "\nCalculating Prime numbers till", num, "..."
    
    if num < 2:
        print num, "is neither Prime nor Composite"        
        return 1
    
    primeNumList = []
    i = 2        
    
    while True:
        remainder = True
        
        for j in range(2, i):
            if i > 2 and i % j == 0:
                remainder = False        
        
        if i == 2 or remainder == True:
            primeNumList.append(i)
        i += 1
        
        if i <= num:
            continue
        else:
            break
        
    print "Prime numbers:", primeNumList


# Function to get user input and perform exception handling
def getUserInput():
    while True:
        userInput = raw_input("Please enter an integer. Enter 'quit' to terminate the program.\n")
        try:
            if userInput == 'quit':
                print "Terminating..."
                sys.exit(0)
            else:
                num = int(userInput)
            if num < 0:
                print num, "is negative. Please enter a positive integer."
            elif num == 0:
                print num, "is zero. Please enter a positive integer."
            elif num > 0:
                print num, "is positive."
                findPrimes(num)
                findFibonacciNumbers(num)
                break                
            else:
                raise Exception           
        except ValueError:
            print userInput, "is an invalid input.\n"
            continue
        except Exception, e:
            print "Unknown Error:\n", str(e)
            sys.exit(1)
        
        print ""
        
            
# Main starts here
def main():
    getUserInput()
    

main()