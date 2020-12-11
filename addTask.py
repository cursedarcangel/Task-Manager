import json
from Task import *

def addTask():
    name = input("What is this task named?\n")
    description = input("Give a description of this task\n")
    time = int(input("How many days do you have to do this task?\n"))
    task = Task(name, description, time)
    taskDict = task.returnAsJson()
    jsonObject = json.dumps(taskDict, indent = 4)
    with open("tasks.json", "a") as outfile:
        outfile.write(jsonObject)

def addNote():
    print("add note")

def seeTask():
    allOrOne = input('do you want to see all the tasks or just one \n')

    with open('tasks.json') as taskFile:
        tasks = json.load(taskFile)
        if 'one' in allOrOne:
            toSee = input('which task do you want to see \n')
            print(tasks[toSee])
        else:
            for k, v in tasks.items():
                print(k, v, '\n')

def seeNote():
    print("see notes")

def reviseTask():
    print("revise task")

def reviseNote():
    print("revise note")
