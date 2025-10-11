import inspect
import sys
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

# help command
def show_help():
    for command_name in commands.keys():
        print(command_name)

# application control operations
def exit_app():
    print("Exiting application.")
    sys.exit(0)

# task management operations
def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"added {task} to the list")

def remove_task(task):
    tasks = load_tasks()
    if task in tasks:
        tasks.remove(task)
        save_tasks(tasks)
        print(f"removed {task} from the list")

    elif task.isdigit():
        index = int(task) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks(tasks)
            print(f"removed {removed_task} from the list")
        else:
            print(f"index {task} out of range")

    else:
        print(f"task {task} not found")

def list_tasks():
    tasks = load_tasks()
    if tasks:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks found.")

commands = {
    "help": show_help,
    "exit": exit_app,
    "add": add_task,
    "remove": remove_task,
    "list": list_tasks
}