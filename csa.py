## assignment:
## Your program should tell me 5 things about you. Things you would like me to know.
## These could be your favorite things, interesting things about you, what you are
## doing over the summer, an about you page, I believe statements, etc.
## The program must include code and should have input and output.
## (This should not be a static output. This is not a one page slide. )

## imports
import os
import time

## defining functions
def fact():
    pass

def printFact():
    pass

def chooseFact():
    pass

## defining the fun facts
funFacts = {
    "Fun Fact 1": "I play tennis",
    "Fun Fact 2": "I worked at Yellow Door Taqueria over the summer.",
    "Fun Fact 3": "3",
    "Fun Fact 4": "4",
    "Fun Fact 5": "5"
    }
keysList = list(funFacts.keys())
valuesList = list(funFacts.values())

## intro text
def intro():
    print("Welcome to Myles' CSA Summer Work!\n")
    displayFact()

## display the facts
def displayFact():
    print("To view a Fun Fact about me, type the corresponding number of the Fun Fact:")
    print("\n".join(keysList))
    chooseFact()

## choose a fact, and otherwise display error code
def chooseFact():
    while True:
        try:
            num = int(input("\nFun Fact Number: "))
            key = keysList[num-1]
            value = valuesList[num-1]
            printFact(key, value)
        except IndexError:
            print("Please type a number corresponding to a Fun Fact.")
            chooseFact()
        except ValueError:
            print("Please type a number corresponding to a Fun Fact.")
            chooseFact()

## print fact
def printFact(key, value):
    print(key + ": \n" + value)
    choice = input("Press 1 to return to the main page, or anything else to exit. \n")
    if choice == "1":
        os.system("cls")
        displayFact()
    else:
        print("Exiting...")
        time.sleep(1)
        os.system("cls")
        exit()

## start program
intro()
