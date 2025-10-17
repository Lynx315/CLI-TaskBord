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

def print_task(t):
    created = t["created_at"][:16]
    edited = t["edited_at"][:16] if t["edited_at"] else "-"
    print(f"ID: {t['id']} | {t['description']} | created: {created} | edited: {edited} | status: {t['status']}")

commands = {}

# help command
def show_help():
    print(command_descriptions)

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

def list_tasks(id=None):
    tasks = load_tasks()
    if id is None:
        if not tasks:
            print("No tasks found.")
            return

        tasks = sorted(tasks, key=lambda x: x["id"])
        for t in tasks:
            print_task(t)
    elif id.isdigit():
        if isinstance(id, str) and id.isdigit():
            task_id = int(id)
            for t in tasks:
                if t["id"] == task_id:
                    print_task(t)
                    return
            print(f"No task found with id {task_id}.")
    elif id == "done":
        done_tasks = [t for t in tasks if t["status"] == "finished"]
        if not done_tasks:
            print("No finished tasks found.")
            return
        done_tasks = sorted(done_tasks, key=lambda x: x["id"])
        for t in done_tasks:
            print_task(t)
    elif id == "doing":
        doing_tasks = [t for t in tasks if t["status"] == "In Progress"]
        if not doing_tasks:
            print("No tasks in progress found.")
            return
        doing_tasks = sorted(doing_tasks, key=lambda x: x["id"])
        for t in doing_tasks:
            print_task(t)
    elif id == "none":
        none_tasks = [t for t in tasks if t["status"] is None]
        if not none_tasks:
            print("No tasks with undefined status found.")
            return
        none_tasks = sorted(none_tasks, key=lambda x: x["id"])
        for t in none_tasks:
            print_task(t)
    else:
        print(f"No tasks found with filter {id}.")

def update_task(task):
    tasks = load_tasks()
    task_found = False

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
    "doing": doing_task,
    "end": finished_task
})

command_descriptions = """
/help: Show this help message
/exit: Exit the app
/add: Add a new task
/remove: Remove a task by ID
/list: List tasks
    /list            -> all tasks
    /list [id]       -> specific task by ID
    /list done       -> finished tasks
    /list doing      -> tasks in progress
    /list none       -> tasks without status
/update: Update a task by ID
/doing: Mark a task as In Progress
/end: Mark a task as finished
"""
