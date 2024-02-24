tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added.")

def view_tasks():
    print("Tasks in your to-do list:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def delete_task(task_number):
    removed_task = tasks.pop(task_number - 1)
    print("Task deleted.")


def main_loop():
    while True:
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        else:
            print("Error")
            break

main_loop()
