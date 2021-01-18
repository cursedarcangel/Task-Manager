class Task:
    def __init__(self, name, description, time):
        self.name = name
        self.description = description
        self.time = time

    def returnAsDict(self):
        values = {
            self.name:{
	    "Task Name": self.name,
	    "Task Description": self.description,
	    "Time to complete": self.time
		}
            }
        return values
