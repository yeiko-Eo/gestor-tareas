import os 
"""
To manage path
"""
class Task_Manager:
    def __init__(self, file_name = "tasks.txt"):
        self.file_name = file_name
        self.tasks = []
    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                for task in file:
                    self.tasks.append(task.strip())
    def save_tasks(self):
        with open(self.file_name, "w") as file:
            for task in self.tasks:
                file.write(task + "\n")
    def add_task(self, task):
        self.tasks.append(task)
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
    def get_tasks(self):
        return self.tasks