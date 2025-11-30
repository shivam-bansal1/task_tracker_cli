import argparse
from utils import TaskManager, TaskStatus

def print_help():

    help_text = """
Available Commands:
  add <description>                 - Add a new task
  update <id> <description>         - Update task description
  delete <id>                       - Delete a task
  mark-done <id>                    - Mark task as done
  mark-in-progress <id>             - Mark task as in progress
  list [all|todo|done|in-progress]  - List tasks (default: all)
  help                              - Show this help message
  exit / quit                       - Exit the program
"""
    print(help_text)


def interactive_mode():
    """Run the task tracker in interactive mode."""
    task_manager = TaskManager()
    print("=" * 50)
    print("Task Tracker - Interactive Mode")
    print("=" * 50)
    print("Type 'help' for available commands or 'exit' to quit\n")

    while True:
        try:
            user_input = input("task-tracker> ").strip()

            if not user_input:
                continue

            # Split input into command and arguments
            parts = user_input.split(maxsplit=1)
            command = parts[0].lower()

            # Handle exit commands
            if command in ["exit", "quit", "q"]:
                print("Goodbye!")
                break

            # Handle help command
            if command == "help":
                print_help()
                continue

            # Handle add command
            if command == "add":
                if len(parts) < 2:
                    print("Error: Please provide a task description")
                    print("Usage: add <description>")
                else:
                    print(task_manager.add_task(parts[1]))
                continue

            # Handle list command
            if command == "list":
                status_filter = parts[1] if len(parts) > 1 else "all"
                if status_filter not in ["all", "todo", "done", "in-progress"]:
                    print(f"Error: Invalid filter '{status_filter}'")
                    print("Valid filters: all, todo, done, in-progress")
                else:
                    print(task_manager.list_tasks(status_filter))
                continue

            # Handle commands that require ID
            if command in ["update", "delete", "mark-done", "mark-in-progress"]:
                if len(parts) < 2:
                    print(f"Error: Please provide a task ID")
                    print(f"Usage: {command} <id>" + (" <description>" if command == "update" else ""))
                    continue

                # Parse ID and remaining arguments
                args = parts[1].split(maxsplit=1)
                try:
                    task_id = int(args[0])
                except ValueError:
                    print("Error: Task ID must be a number")
                    continue

                if command == "update":
                    if len(args) < 2:
                        print("Error: Please provide a new description")
                        print("Usage: update <id> <description>")
                    else:
                        print(task_manager.update_task(task_id, args[1]))

                elif command == "delete":
                    print(task_manager.delete_task(task_id))

                elif command == "mark-done":
                    print(task_manager.mark_task(task_id, TaskStatus.DONE))

                elif command == "mark-in-progress":
                    print(task_manager.mark_task(task_id, TaskStatus.IN_PROGRESS))

                continue

            # Unknown command
            print(f"Unknown command: '{command}'")
            print("Type 'help' for available commands")

        except KeyboardInterrupt:
            print("\n\nUse 'exit' or 'quit' to leave the program")
        except EOFError:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Task Tracker - A simple CLI task management tool",
        epilog="Run without arguments to start interactive mode"
    )

    subparser = parser.add_subparsers(dest="action")

    add_parser = subparser.add_parser("add", help="Add a new task")
    add_parser.add_argument("task", type=str, help="Task to add")

    update_parser = subparser.add_parser("update", help="Update an existing task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("updated_task", type=str, help="Updated Task")

    delete_parser = subparser.add_parser("delete", help="Delete an existing task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    mark_progress_parser = subparser.add_parser("mark-in-progress", help="Update status to in progress")
    mark_progress_parser.add_argument("id", type=int, help="Task ID")

    mark_done_parser = subparser.add_parser("mark-done", help="Update status to in done")
    mark_done_parser.add_argument("id", type=int, help="Task ID")

    list_parser = subparser.add_parser("list", help="list existing tasks")
    list_parser.add_argument(
        "filter",
        nargs="?",
        choices=["all", "done", "todo", "in-progress"],
        default="all",
        help="Filter tasks (default: all)"
    )

    args = parser.parse_args()

    if args.action is None:
        interactive_mode()
        return 0

    task_manager = TaskManager()

    try:
        if args.action == "add":
            print(task_manager.add_task(args.task))
        elif args.action == "update":
            print(task_manager.update_task(args.id, args.updated_task))
        elif args.action == "delete":
            print(task_manager.delete_task(args.id))
        elif args.action == "mark-done":
            print(task_manager.mark_task(args.id, TaskStatus.DONE))
        elif args.action == "mark-in-progress":
            print(task_manager.mark_task(args.id, TaskStatus.INPROGRESS))
        elif args.action == "list":
            print(task_manager.list_tasks(args.filter))
    except Exception as e:
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    main()