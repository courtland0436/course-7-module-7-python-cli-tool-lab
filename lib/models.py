# lib/models.py

class Task:
    def __init__(self, title):
        # Assign the title
        self.title = title
        # Set completed to False by default
        self.completed = False

    def complete(self):
        # Mark the task as complete
        self.completed = True
        # Print a confirmation message
        print(f"✅ Task '{self.title}' completed.")


class User:
    def __init__(self, name):
        # Store the user's name
        self.name = name
        # Initialize an empty list of tasks
        self.tasks = []

    def add_task(self, task):
        # Add the task to the user's task list
        self.tasks.append(task)
        # Print a confirmation message
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        # Search for a task by its title
        for task in self.tasks:
            if task.title == title:
                return task
        # Return None if not found
        return None
