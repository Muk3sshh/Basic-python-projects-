import os

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f'Task "{task}" added.')

    def update_task(self, task_number, new_task):
        if 0 <= task_number < len(self.tasks):
            old_task = self.tasks[task_number]['task']
            self.tasks[task_number]['task'] = new_task
            print(f'Task "{old_task}" updated to "{new_task}".')
        else:
            print("Invalid task number.")

    def complete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]['completed'] = True
            print(f'Task "{self.tasks[task_number]["task"]}" marked as completed.')
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            print(f'Task "{removed_task["task"]}" deleted.')
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        for i, task in enumerate(self.tasks):
            status = "Done" if task['completed'] else "Pending"
            print(f"{i + 1}. {task['task']} - {status}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    todo_list = TodoList()

    while True:
        clear_screen()
        print("To-Do List Application")
        print("======================")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            clear_screen()
            todo_list.show_tasks()
            input("\nPress Enter to return to the menu.")
        elif choice == '2':
            task = input("Enter the task: ")
            todo_list.add_task(task)
            input("\nPress Enter to return to the menu.")
        elif choice == '3':
            task_number = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo_list.update_task(task_number, new_task)
            input("\nPress Enter to return to the menu.")
        elif choice == '4':
            task_number = int(input("Enter the task number to complete: ")) - 1
            todo_list.complete_task(task_number)
            input("\nPress Enter to return to the menu.")
        elif choice == '5':
            task_number = int(input("Enter the task number to delete: ")) - 1
            todo_list.delete_task(task_number)
            input("\nPress Enter to return to the menu.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to return to the menu.")

if __name__ == "__main__":
    main()