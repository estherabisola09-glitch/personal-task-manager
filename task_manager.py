import json
import os
import shutil
from datetime import datetime

DATA_FILE = "tasks.json"
MAX_TITLE_LENGTH = 100


def load_tasks(filename=DATA_FILE):
    """Load tasks from the JSON file. Returns a list of tasks."""
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            tasks = json.load(f)
        if not isinstance(tasks, list):
            raise ValueError("Tasks file must contain a list.")
        return tasks
    except (json.JSONDecodeError, ValueError):
        # File is broken: keep a backup so nothing is lost, then start empty
        backup = filename + ".bak"
        shutil.copy(filename, backup)
        print(f"Warning: {filename} is corrupted. A backup was saved as {backup}.")
        print("Starting with an empty task list.")
        return []


def save_tasks(tasks, filename=DATA_FILE):
    """Save tasks safely: write to a temp file first, then swap it in."""
    temp_file = filename + ".tmp"
    try:
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2)
        os.replace(temp_file, filename)
        return True
    except OSError as error:
        print(f"Error: could not save tasks ({error}). Your original file is untouched.")
        return False


def get_next_id(tasks):
    """New id = highest id + 1, so deleted ids are never reused."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def find_task(tasks, task_id):
    """Return the task with this id, or None if it does not exist."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def add_task(tasks, title):
    """Add a task. Returns (success, message)."""
    title = title.strip()
    if not title:
        return False, "Task title cannot be empty."
    if len(title) > MAX_TITLE_LENGTH:
        return False, f"Task title is too long (max {MAX_TITLE_LENGTH} characters)."

    task = {
        "id": get_next_id(tasks),
        "title": title,
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    tasks.append(task)
    return True, f"Task {task['id']} added."


def complete_task(tasks, task_id):
    """Mark a task complete. Returns (success, message)."""
    task = find_task(tasks, task_id)
    if task is None:
        return False, "Task not found."
    if task["completed"]:
        return False, "Task is already complete."
    task["completed"] = True
    return True, f"Task {task_id} marked complete."


def delete_task(tasks, task_id):
    """Delete a task. Returns (success, message)."""
    task = find_task(tasks, task_id)
    if task is None:
        return False, "Task not found."
    tasks.remove(task)
    return True, f"Task {task_id} deleted."


def format_tasks(tasks):
    """Return the task list as a printable string."""
    if not tasks:
        return "No tasks yet."
    lines = []
    for task in tasks:
        status = "[x]" if task["completed"] else "[ ]"
        lines.append(f"{task['id']}. {status} {task['title']}  (created {task['created_at']})")
    return "\n".join(lines)