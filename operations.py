import sys
import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

commands = {}

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
    existing_ids = sorted([t["id"] for t in tasks])
    new_id = 1
    for i in existing_ids:
        if i == new_id:
            new_id += 1
        else:
            break

    new_task = {
        "id": new_id,
        "description": task,
        "created_at": datetime.now().isoformat(),
        "edited_at": None,
        "status": None
    }

    tasks.append(new_task)
    save_tasks(tasks)
    print(f"added {task} to the list with id {new_id}")

def remove_task(task):
    tasks = load_tasks()
    task_found = False

#changed this
    # Remove by id if not found by description and task is digit
    if isinstance(task, str) and task.isdigit():
        task_id = int(task)
        for t in tasks:
            if t["id"] == task_id:
                tasks.remove(t)
                save_tasks(tasks)
                print(f"removed task: {t['description']} with id {task_id} from the list")
                task_found = True
                break
        if task_found == False:
            print(f"No task found with id {task_id}.")
    else:
        print(f"{task} needs to be a digit")
    
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    # sortiere Tasks nach ID
    tasks = sorted(tasks, key=lambda x: x["id"])
    for t in tasks:
        created = t["created_at"][:16]
        edited = t["edited_at"][:16] if t["edited_at"] else "-"
        print(f"ID: {t['id']} | {t['description']} | created: {created} | edited: {edited} | status: {t['status']}")

def update_task(task):
    tasks = load_tasks()
    task_found = False

    # Remove by id if task is digit
    if isinstance(task, str) and task.isdigit():
        task_id = int(task)
        for t in tasks:
            if t["id"] == task_id:
                update = input("Update task description: ")
                t["description"] = update
                t["edited_at"] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f"Updated task to: {t['description']} with id {task_id}")
                task_found = True
                break
        if not task_found:
            print(f"No task found with id {task_id}.")
    else:
        print(f"{task} needs to be a digit")

def doing_task(task):
    tasks = load_tasks()
    task_found = False

    # Remove by id if task is digit
    if isinstance(task, str) and task.isdigit():
        task_id = int(task)
        for t in tasks:
            if t["id"] == task_id:
                t["status"] = "In Progress"
                save_tasks(tasks)
                print(f"Set task: {t['description']} with id {task_id} to in progress")
                task_found = True
                break
        if not task_found:
            print(f"No task found with id {task_id}.")
    else:
        print(f"{task} needs to be a digit")

def finished_task(task):
    tasks = load_tasks()
    task_found = False

    # Remove by id if task is digit
    if isinstance(task, str) and task.isdigit():
        task_id = int(task)
        for t in tasks:
            if t["id"] == task_id:
                t["status"] = "finished"
                save_tasks(tasks)
                print(f"Set task: {t['description']} with id {task_id} to in progress")
                task_found = True
                break
        if not task_found:
            print(f"No task found with id {task_id}.")
    else:
        print(f"{task} needs to be a digit")
    


commands.update({
    "help": show_help,
    "exit": exit_app,
    "add": add_task,
    "remove": remove_task,
    "list": list_tasks,
    "update": update_task,
    "do": doing_task,
    "end": finished_task
})