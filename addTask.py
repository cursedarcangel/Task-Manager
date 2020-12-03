import json
from Task import *

def addTask():
    name = input("What is this task named?\n")
    description = input("Give a description of this task\n")
    time = int(input("How many days do you have to do this task?\n"))
    task = Task(name, description, time)
    dict = task.returnAsJson()
    jsonObject = json.dumps(dict, indent = 4)
    with open("tasks.json", "w") as outfile:
        outfile.write(jsonObject)

def addNote():
    print("add note")

def seeTasks():
    print("see tasks")

def seeNotes():
    print("see notes")

def reviseTask():
    print("revise task")

def reviseNote():
    print("revise note")
