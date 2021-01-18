import yaml
from Task import *

def addTask():
    name = input("What is this task named?\n")
    description = input("Give a description of this task\n")
    time = int(input("How many days do you have to do this task?\n"))
    task = Task(name, description, time)
    taskDict = task.returnAsDict()
    with open("tasks.yml", "a") as f:
        tasks = yaml.dump(taskDict, f)

def addNote():
    print("add note")

def seeTask():
    allOrOne = input('do you want to see all the tasks or just one \n')

    with open('tasks.yml') as taskFile:
        tasks = yaml.load(taskFile, Loader = yaml.FullLoader)
        tasksSorted = yaml.dump(tasks, sort_keys=True)
        if 'one' in allOrOne:
            toSee = input('which task do you want to see \n')
            task = tasks[toSee]
            print(yaml.dump(task, sort_keys=True))
        else:
            print(tasksSorted)

def seeNote():
    print("see notes")

def reviseTask():
    print("revise task")

def reviseNote():
    print("revise note")
