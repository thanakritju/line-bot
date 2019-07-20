class Task():
    def __init__(self):
        self.tasks = []

    @staticmethod
    def help():
        message = """
Here is how to use 'todo' or 'Todo'

Adding TODO
    Todo add <your task>

Showing TODOs
    Todo show

Mark as done
    Todo done <your task number>

Deleting unwanted TODO
    Todo del <your task number>

Delete all TODOS
    Todo delall
        """
        return message

    @staticmethod
    def validate_task_number(task_number):
        try:
            task_number = int(task_number)
            if task_number <= 0:
                raise ValueError("Please provide positive value")
            return True
        except (ValueError, TypeError):
            return "Please provide a valid task number"
        except IndexError:
            return f"There is no task number: {task_number}" 

    def add_task(self, task):
        if task is not None:
            self.tasks.append(task)
            return f"Finished adding TODO: {task}"
        else:
            return "Please provide a task"
            
    def done_task(self, task_number):
        condition = self.validate_task_number(task_number)
        task_number = int(task_number)
        if condition == True:
            task = self.tasks[task_number-1]
            self.tasks[task_number-1] = f"(Done) {task}"
            return f"Marked {task} as done"
        return condition

    def delete_task(self,task_number):
        condition = self.validate_task_number(task_number)
        task_number = int(task_number)
        if condition == True:
            task = self.tasks[task_number-1]
            del self.tasks[task_number-1]
            return f"Deleted task: {task}"
        return condition

    def delete_all_tasks(self):
        self.tasks = []
        return f"Deleted all tasks"

    def show_task(self):
        if len(self.tasks) != 0:
            message = "Here is your current TODOs\n\n"
            for task_number,task in enumerate(self.tasks):
                message = message + f"{task_number+1}. {task}\n"
        else:
            message = "There is no current TODOs"
        return message
