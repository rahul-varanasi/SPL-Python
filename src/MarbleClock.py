'''
Created on Oct 22, 2013

@author:     Rahul Varanasi - 800807351
             Manmohan Chaubey - 800832048
             Kshitiz Gupta - 800803559             
'''

'''
This program simulates the functioning of a Marble Clock. It accepts an integer input >= 21.
It then calculates the number of cycles after which the marbles are back in the original order
'''


tray1 = []  # tray size = 4
tray2 = []  # tray size = 2
tray3 = []  # tray size = 3
tray4 = []  # tray size = 11
tray5 = []  # tray size >= 21

# Function to generate marbles in Tray 5
def genTray5(numOfMarbles):
    global tray5
    for i in range(1, numOfMarbles+1):
        tray5.append(i)
        

# Function to check if Tray 5 is in correct order        
def isTray5InCorrectOrder():
    num = 1
    for i in tray5:
        if num != i:    # Wrong order
            return False
        num += 1
    
    return True     # Tray is in correct order


# Function to add an element to Tray 1
def addToTray1():
    global tray1
    tray1.append(popTray5())
    

# Function to pop all elements from Tray 1    
def popTray1():
    global tray1
    global tray5
    while len(tray1) != 0:
        tray5.append(tray1.pop())


# Function to add an element to Tray 2
def addToTray2():
    global tray2
    tray2.append(popTray5())
    

# Function to pop all elements from Tray 2
def popTray2():
    global tray2
    global tray5
    while len(tray2) != 0:
        tray5.append(tray2.pop())


# Function to add an element to Tray 3
def addToTray3():
    global tray3
    tray3.append(popTray5())
    

# Function to pop all elements from Tray 3    
def popTray3():
    global tray3
    global tray5
    while len(tray3) != 0:
        tray5.append(tray3.pop())


# Function to add an element to Tray 4
def addToTray4():
    global tray4
    tray4.append(popTray5())
    

# Function to pop all elements from Tray 4    
def popTray4():
    global tray4
    global tray5
    while len(tray4) != 0:
        tray5.append(tray4.pop())


# Function to pop 1 element from Tray 5
def popTray5():
    global tray5
    return tray5.pop(0)


# Function to start the marble clock
def runMarbleClock(numOfMarbles):    
    # Generate the marbles in Tray 5
    genTray5(numOfMarbles)
    
    cycles = 0
    
    while True:
        if len(tray1) < 4:
            addToTray1()
        else:   # Tray 1 is full
            if len(tray2) < 2:
                # add next element to tray 2
                addToTray2()
                # pop tray 1
                popTray1()                
            else:   # Tray 2 is full
                if len(tray3) < 3:
                    # add next element to tray 3                    
                    addToTray3()
                    # pop tray 1
                    popTray1()
                    # pop tray 2
                    popTray2()                    
                else:   # Tray 3 is full
                    if len(tray4) < 11:
                        # add next element to tray 4
                        addToTray4()
                        # pop tray 1
                        popTray1()
                        # pop tray 2
                        popTray2()
                        # pop tray 3
                        popTray3()
                    else:   # Tray 4 is full
                        # pop tray 1
                        popTray1()
                        # pop tray 2
                        popTray2()
                        # pop tray 3
                        popTray3()
                        # pop tray 4
                        popTray4()
                        
                        cycles += 1
                        if isTray5InCorrectOrder():
                            # Tray 5 is in original order, break
                            break
    
    print '>>> Number of cycles -->', cycles
    print '>>> Bye-Bye :)'
    

# Function to validate user input and start the marble clock    
def main():
    numMarbles = 0
    while True:
        try:
            numMarbles = int(raw_input('>>> Enter the number of marbles: '))
            if numMarbles < 21:
                # Number of marbles should be atleast 21
                print '>>> Number of marbles has to be atleast 21!!!'
                print ''
                continue
            break
        except:
            # Invalid input
            print '>>> Invalid input!!!'
            print ''
            continue        
    
    # Input valid. Run marble clock
    runMarbleClock(numMarbles)
    

# Call the main function    
main()