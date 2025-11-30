import json
from datetime import datetime
from pathlib import Path
import os
from enum import Enum
from typing import List, Optional


class TaskStatus(Enum):
    DONE = "done"
    COMPLETED = "completed"
    INPROGRESS = "in-progress"

    @classmethod
    def from_string(cls, status: str):
        try:
            return cls(status)
        except ValueError:
            raise ValueError(f"Invalid status: {status}. Must be one of {[s.value for s in cls]}")


class TaskManager:
    def __init__(self, file: str = "tasks.json"):
        self.file_path = Path(file)

    def _load_tasks(self) -> List[dict]:
        if not self.file_path.exists():
            return []

        try:
            with open(self.file_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Warning, File is corrupt!")
            return []
        except Exception as e:
            raise IOError(f"Error reading tasks file: {e}")

    def _save_tasks(self, tasks: List[dict]) -> None:
        try:
            with open(self.file_path, "w") as f:
                json.dump(tasks, f)
        except Exception as e:
            raise IOError(f"Error writing tasks file: {e}")

    def _get_next_id(self):
        return max((task["id"] for task in self._load_tasks()), default=0) + 1

    def _find_task_index(self, tasks: List[dict], task_id: int) -> Optional[int]:
        for idx, task in enumerate(tasks):
            if task["task_id"] == task_id:
                return idx
        return None

    def add_task(self, description: str):
        if not description or description.strip():
            return "Error: Task cannot be empty"

        description = description.strip()
        tasks = self._load_tasks()

        for task in tasks:
            if description == task["description"] and task["status"] != TaskStatus.DONE:
                return "Error: Task already present"

        task_id = self._get_next_id()
        task = {
            "id": task_id,
            "description": description,
            "status": "todo",
            "created_at": str(datetime.now()),
            "updated_at": str(datetime.now()),
        }

        tasks.append(task)
        self._save_tasks(tasks)
        return f"Task added successfully (ID: {task_id})"

    def update_task(self, task_id, description: str):
        if not description or description.strip():
            return "Error: Task cannot be empty"

        tasks = self._load_tasks()
        if not tasks:
            return "No existing tasks found"

        description = description.strip()
        task_idx = self._find_task_index(tasks, task_id)
        if not task_idx:
            return f"No task found with ID: {task_id}"

        tasks[task_idx]['description'] = description.strip()
        tasks[task_idx]['updated_at'] = str(datetime.now())
        self._save_tasks(tasks)

        return f"Task updated successfully (ID: {task_id})"

    def delete_task(self, task_id: int) -> str:
        tasks = self._load_tasks()
        if not tasks:
            return "No existing tasks found"

        task_idx = self._find_task_index(tasks, task_id)
        if not task_idx:
            return f"No task found with ID: {task_id}"

        tasks.pop(task_idx)
        self._save_tasks(tasks)
        return f"Task deleted successfully (ID: {task_id})"

    def mark_task(self, task_id: int, status: TaskStatus) -> str:
        tasks = self._load_tasks()
        if not tasks:
            return "No existing tasks found"

        task_idx = self._find_task_index(tasks, task_id)
        if not task_idx:
            return f"No task found with ID: {task_id}"

        tasks[task_idx]['status'] = status
        tasks[task_idx]['updated_at'] = str(datetime.now())
        self._save_tasks(tasks)
        return f"Task updated successfully (ID: {task_id})"

    def list_tasks(self, status_filter: Optional[str] = None) -> str:
        tasks = self._load_tasks()
        if not tasks:
            return "No existing tasks found"

        if status_filter and status_filter != "all":
            filtered_tasks = [t for t in tasks if t['status'] == status_filter]
        else:
            filtered_tasks = tasks

        if not filtered_tasks:
            filter_msg = f" with status '{status_filter}'" if status_filter != "all" else ""
            return f"No tasks found{filter_msg}"

        output = []
        for task in filtered_tasks:
            output.append(
                f"[{task['id']}] {task['description']} "
                f"(Status: {task['status']}, Updated: {task['updated_at']})"
            )

        return "\n".join(output)

