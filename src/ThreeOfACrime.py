'''
Created on Oct 22, 2013

@author:     Rahul Varanasi - 800807351
             Manmohan Chaubey - 800832048
             Kshitiz Gupta - 800803559
'''

'''
This program is to simulate the functioning of Three of a Crime game.
The computer chooses 3 random perpetrators. It then chooses 3 random criminals
and gives us a hint by telling how many of them are actual perpetrators.
The program allows for a maximum of 3 hints after the original hint given when
the actual perpetrators are chosen. No more hints will be given later.
The program allows the player to pass. Maximum 3 passes are allowed after which
player automatically loses the game.
The player can enter his 3 guesses. If they are wrong, player loses.
Player can exit by typing exit anytime during the game.
'''

import random

perpetratorsList = []       # Store actual perpetrators
passCount = 0               # Store actual number of passes done
hintCount = 0               # Store actual number of hints given

# Function to select random perpetrators
def selectRandomPerpetrators():
    global perpetratorsList
    
    # Add 3 random perpetrators to perpetrators list
    while len(perpetratorsList) < 3:
        r = random.randint(1, 7)
        
        # Add only if r doesn't exist in perpetrators list
        if r not in perpetratorsList:
            perpetratorsList.append(r)
    
    print '3 Perpetrators chosen\n'
    

# Function to print perpetratos if player loses    
def showActualPerpetrators():
    print 'Perpetrators are -->', perpetratorsList


# Function to generate random hint for user
def showRandomCriminalsHint():
    global perpetratorsList
    global hintCount
    hintList = []           # Store current random hints
    
    # Check for number of times hint has been given
    # No more hints if 3 hints have been given!
    if hintCount <= 3:
        hintCount += 1
        
        # Add 3 random hints to hint list
        while len(hintList) < 3:
            r = random.randint(1, 7)
            
            # Add only if hint doesn't exist in hint list
            if r not in hintList:
                hintList.append(r)
            
            # Count the number of actual perpetrators in hint list
            count = 0
            for hint in hintList:
                if hint in perpetratorsList:
                    count += 1
        
        print 'Computer hint -->', hintList, '-->', count, 'perpetrators in hint list\n'
    else:
        print 'Only 3 hints allowed!!!\n'
    

# Function to handle user guess and check if it is correct    
def userGuess():
    global perpetratorsList
    guessCount = 0          # Store number of current guess
    correctGuessCount = 0   # Store correct guess
    
    # Max only 3 guess allowed
    while guessCount < 3:
        print 'Guess', guessCount + 1,
        userInput = int(raw_input('--> '))
        
        # If user guess is correct, increment correct guess count
        if userInput in perpetratorsList:
            correctGuessCount += 1
        guessCount += 1
    
    # Player either wins or loses!
    if correctGuessCount == 3:         
        print 'Player wins!!!'
    else:
        print 'Player loses!!!'
        showActualPerpetrators()
        

# Function to handle user pass
def userPass():
    global passCount
    passCount += 1    
    print 'Pass', passCount
    
    # Only 3 passes allowed
    if passCount >= 3:        
        print 'Player loses!!!'
        showActualPerpetrators()
        return False
    
    print ''
    return True
        

# Function to print commands    
def printCommands():
    print 'Enter the following commands:'
    print '"guess" - guess the perpetrators'
    print '"pass" - pass'
    print '"hint" - ask the computer for hint'
    print '"exit" - exit program'
    print '"help" - show these commands again\n'
    

# Run the program console interpreter
def runInterpreter():    
    while True:        
        userInput = raw_input(">>> ")       # Take user input
        
        # User chooses guess
        if userInput == 'guess':
            userGuess()
            break
        # User chooses pass
        elif userInput == 'pass':
            if userPass() != True:      # Check return value of userPass() to see if max passes exceeded
                break
        # User chooses hint
        elif userInput == 'hint':            
            showRandomCriminalsHint()
        # User chooses exit
        elif userInput == 'exit':            
            print 'Bye-Bye :)'
            break
        # User chooses help
        elif userInput == 'help':
            printCommands()
        # User gives wrong input
        else:
            print 'Try again\n'
                

# Main function where program starts
def main():
    printCommands()
    selectRandomPerpetrators()
    showRandomCriminalsHint()
    runInterpreter()


# Call the main function
main()