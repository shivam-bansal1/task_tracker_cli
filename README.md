# 📌 Task Tracker CLI

A simple, lightweight, file-based command-line task manager written in Python.
Manage your tasks directly from the terminal — add, update, delete, mark progress, and list tasks with filters.

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

Run in interactive mode:
```
python main.py
```
The CLI supports the following commands:

1. add 
2. update 
3. delete 
4. mark-in-progress 
5. mark-done 
6. list


### ➕ Add a Task
```
add "Buy groceries"
```
### ✏️ Update an Existing Task
```
update 1 "Buy groceries and vegetables"
````

### ❌ Delete a Task
```
delete 1
```
### 🔄 Mark Task as In Progress
```
mark-in-progress 2
```

### ✅ Mark Task as Done
```
mark-done 3
```
### 📋 List Tasks
```
list
```

### 📋 List only todo tasks
```
list todo
```
### 📋 List only in-progress tasks
```
list in-progress
```

### 📋 List only done tasks
```
list done
```

## Credits
👉 <a>https://roadmap.sh/projects/task-tracker</a>

