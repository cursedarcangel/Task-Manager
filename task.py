class task:
    def __init__(self, name, description, time):
        self.name = name
        self.time = time
        self.description = description

    def printTaskData(self):
        print(self.name)
        print(self.time)
        print(self.description)