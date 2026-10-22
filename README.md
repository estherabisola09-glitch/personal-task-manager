# Personal Task Manager

A command-line task manager written in Python. Add, view, complete, and delete
tasks. Your tasks are saved to a JSON file, so they are still there the next
time you open the app.

Built as an AI-assisted development project: I planned the app first, used AI
(Copilot/Claude) to help build and review it, then tested and fixed what the
AI got wrong. See `REFLECTION.md` for what I learned.

## Features

- Add a task (empty, spaces-only, and very long titles are rejected)
- View all tasks with their status: `[ ]` pending, `[x]` complete
- Mark a task complete
- Delete a task
- Tasks are saved automatically after every change
- Safe saving: the app writes to a temporary file first, then swaps it in, so a
  failed save never destroys your existing data
- Corrupted data file: the app makes a timestamped backup, warns you, and
  starts fresh instead of crashing
- Task ids are never reused, even after deleting the newest task

## Requirements

- Python 3.9 or newer
- pytest (only needed to run the tests)

## Setup

```bash
git clone <your-repo-url>
cd Personal-Task-Manager
python -m venv venv
source venv/Scripts/activate      # Git Bash on Windows
# source venv/bin/activate        # Mac / Linux
pip install pytest
```

## Run the app

```bash
python main.py
```

## Supported commands (menu options)

| Option | What it does |
|--------|--------------|
| 1 | Add a task |
| 2 | View all tasks |
| 3 | Mark a task complete (asks for the task id) |
| 4 | Delete a task (asks for the task id) |
| 5 | Exit |

## Example usage

```
=== Task Manager ===
1. Add a task
2. View all tasks
3. Mark a task complete
4. Delete a task
5. Exit
Choose an option (1-5): 1
Task title: Buy bread
Task 1 added.

Choose an option (1-5): 2
1. [ ] Buy bread  (created 2026-10-22 14:45)

Choose an option (1-5): 3
Task id to complete: 1
Task 1 marked complete.
```

## Run the tests

```bash
pytest -v
```

The tests use temporary folders, so they never touch your real `tasks.json`.

## Project structure

```
Personal-Task-Manager/
├── main.py                 # The menu (what the user sees and types into)
├── task_manager.py         # The logic (add, complete, delete, save, load)
├── test_task_manager.py    # pytest tests
├── PLAN.md                 # Requirements, data model, and edge cases
├── REFLECTION.md           # What I learned using AI to build this
└── README.md
```

## How the data is stored

Tasks are saved in `tasks.json` in this format:

```json
{
  "next_id": 3,
  "tasks": [
    {
      "id": 1,
      "title": "Buy bread",
      "completed": true,
      "created_at": "2026-10-22 14:45"
    }
  ]
}
```

`next_id` is a counter that only goes up. That is how deleted ids are never
reused. Older files that contain a plain list of tasks are converted
automatically.

## Future improvements

- Edit a task's title
- Due dates and priorities
- Store timestamps with timezone and seconds
- Search and filter tasks
- A web or graphical interface
