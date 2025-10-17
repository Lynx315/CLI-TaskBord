---

# CLI-TaskBord

Simple, lightweight command-line tool for fast, efficient task management.

CLI-TaskBord provides a small set of commands to add, list, update, and remove tasks, storing them locally in a JSON file (`tasks.json`). It is intentionally minimal and depends only on the Python standard library.

"This project is the result of Roadmap.sh: https://roadmap.sh/projects/task-tracker"

---

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Quick Start](#quick-start)
* [Commands](#commands)
* [Data Format](#data-format)
* [Examples](#examples)
* [License](#license)
* [Troubleshooting](#troubleshooting)

## Features

* Add tasks quickly from the command line
* List tasks with a simple output
* Update task fields
* Delete tasks
* Stores all tasks locally in `tasks.json`

## Requirements

* Python 3.8+ (only uses standard library)



No external dependencies are required.

## Quick Start

Run the CLI script directly:

```bash
python3 interpreter.py
```

All commands are entered using a slash:

```
/[command] [arguments]
```

## Commands

* `/add [task]` — Add a new task
* `/list` — List existing tasks
* `/update [id] [new info]` — Update an existing task
* `/remove [id]` — Remove a task

## Data Format

Tasks are stored locally in `tasks.json`. The file contains all task data; details of the fields are handled internally by the program.

## Examples

```
/list
/add Buy milk
/remove 1
```

## License

This repository includes a LICENSE file — please refer to it for license details.

## Troubleshooting

* If the CLI cannot find `tasks.json`, it may create a new one in the repository root. Ensure the script has write permissions.
* If you see Python errors, check you are using Python 3.8+ and review the traceback for invalid data.



