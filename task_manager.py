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