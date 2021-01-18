from addTask import *

def start():
    print("What do you want to do?")
    print("1: write a task")
    print("2: add a note")
    print("3: see a task")
    print("4: see a note")
    print("5: revise task")
    print("6: revise note")
    print("7: quit")
start()

choice = int(input())

def badNamedFunction(input):
    if (input == 1):
        addTask()
    elif (input == 2):
        addNote()
    elif (input == 3):
        seeTask()
    elif (input == 4):
        seeNote()
    elif (input == 5):
        reviseTask()
    elif (input == 6):
        reviseNote()
    elif (input == 7):
        quit()
badNamedFunction(choice)
