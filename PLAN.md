# Personal Task Manager - Plan

## Overview
A command-line task manager written in Python. Users can add, view, complete,
and delete tasks. Tasks are saved to a JSON file so they stay between sessions.

## Core Features (v1)
1. Add a task
2. View all tasks
3. Mark a task as complete
4. Delete a task
5. Save and load tasks from a JSON file

## User Stories and Acceptance Criteria

### 1. Add a task
As a user, I want to add a task so that I can remember what I need to do.
- Task gets a unique id automatically
- Task starts as not completed
- Empty or spaces-only titles are rejected with a clear message

### 2. View all tasks
As a user, I want to see all my tasks so that I know what is pending.
- Each task shows its id, title, and status ([ ] or [x])
- If there are no tasks, show "No tasks yet"

### 3. Mark a task complete
As a user, I want to mark a task as done so that I can track progress.
- The task's status changes to completed
- If the id does not exist, show "Task not found"
- If it is already complete, tell the user instead of failing

### 4. Delete a task
As a user, I want to delete a task so that my list stays clean.
- The task is removed from the list
- If the id does not exist, show "Task not found"

### 5. Save between sessions
As a user, I want my tasks saved so that I do not lose them when I close the app.
- Tasks save to tasks.json after every change
- On start, tasks load from tasks.json
- If the file is missing, start with an empty list
- If the file is corrupted, start empty and warn the user (do not crash)

## Data Model
Each task is a dictionary:
- id (int): unique, increases by 1
- title (str): the task text
- completed (bool): False by default
- created_at (str): date and time created

## Edge Cases to Handle
- Empty task name
- Task name with only spaces
- Very long task name
- Delete or complete an id that does not exist
- User types a letter instead of a number for the id
- Invalid menu choice
- Viewing an empty list
- tasks.json missing or corrupted
- Completing a task that is already complete

## Out of Scope for v1
- Due dates and priorities
- Multiple users
- Editing a task title
- A graphical interface
### 5. Save between sessions
As a user, I want my tasks saved so that I do not lose them when I close the app.
- Tasks save to tasks.json after every change
- Saving is safe: write to tasks.json.tmp first, then replace tasks.json
- On start, tasks load from tasks.json
- If the file is missing, start with an empty list
- If the file is corrupted, copy it to tasks.json.bak, start empty, and warn the user (do not crash)
- If saving fails (for example disk error), show a clear error and keep the original file untouched

## Data Model
Each task is a dictionary:
- id (int): unique, new id = highest existing id + 1 (never reuse deleted ids)
- title (str): the task text
- completed (bool): False by default
- created_at (str): date and time created

## Edge Cases to Handle
- Empty task name
- Task name with only spaces
- Very long task name
- Delete or complete an id that does not exist
- Deleting the same id twice (second time shows "Task not found")
- User types a letter instead of a number for the id
- Invalid menu choice
- Viewing an empty list
- tasks.json missing
- tasks.json corrupted (back it up, start empty, warn)
- Save fails halfway (original file stays intact)
- Completing a task that is already complete
- New task after deleting the last one (id must not repeat)

