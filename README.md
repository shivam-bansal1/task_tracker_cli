# 📌 Task Tracker CLI

A simple, lightweight, file-based command-line task manager written in Python.
Manage your tasks directly from the terminal — add, update, delete, mark progress, and list tasks with filters. <br>
URL - <a>https://github.com/shivam-bansal1/task_tracker_cli</a>

## 🚀 Features

- Add tasks with automatic unique IDs 
- Update or delete existing tasks 
- Mark tasks as todo, in-progress, or done 
- List tasks with optional filtering 
- JSON-based storage (no database required)
- Minimal, clean, and extensible architecture 
- Works on macOS, Linux, and Windows

## 📂 Project Structure

```
task-tracker/
│
├── main.py        # Task handling logic
├── tasks.json     # Auto-created storage file
```

## 🛠 Requirements

- Python 3

## 📥 Installation

Clone the repository:
```
git clone https://github.com/yourusername/task-tracker.git
cd task-tracker
```

## 💻 Usage

The CLI supports the following commands:

1. add 
2. update 
3. delete 
4. mark-in-progress 
5. mark-done 
6. list


### ➕ Add a Task
```
python main.py add "Buy groceries"
```
### ✏️ Update an Existing Task
```
python main.py update 1 "Buy groceries and vegetables"
````

### ❌ Delete a Task
```
python main.py delete 1
```
### 🔄 Mark Task as In Progress
```
python main.py mark-in-progress 2
```

### ✅ Mark Task as Done
```
python main.py mark-done 3
```
### 📋 List Tasks
```
python main.py list
```

### 📋 List only todo tasks
```
python main.py list todo
```
### 📋 List only in-progress tasks
```
python main.py list in-progress
```

### 📋 List only done tasks
```
python main.py list done
```
