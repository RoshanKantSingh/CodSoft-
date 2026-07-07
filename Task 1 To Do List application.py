# To-Do List Application

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks in your to-do list.")
    else:
        print("\n------ TO-DO LIST ------")
        for i, task in enumerate(tasks, start=1):
            status = "✔ Completed" if task["completed"] else "✘ Pending"
            print(f"{i}. {task['name']} [{status}]")
        print("------------------------")


while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Mark Task as Completed")
    print("5. Delete Task")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        show_tasks()

    elif choice == "2":
        task_name = input("Enter task: ")
        tasks.append({"name": task_name, "completed": False})
        print("Task added successfully!")

    elif choice == "3":
        show_tasks()
        if tasks:
            try:
                task_no = int(input("Enter task number to update: "))
                if 1 <= task_no <= len(tasks):
                    new_name = input("Enter new task name: ")
                    tasks[task_no - 1]["name"] = new_name
                    print("Task updated successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        show_tasks()
        if tasks:
            try:
                task_no = int(input("Enter task number to mark as completed: "))
                if 1 <= task_no <= len(tasks):
                    tasks[task_no - 1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "5":
        show_tasks()
        if tasks:
            try:
                task_no = int(input("Enter task number to delete: "))
                if 1 <= task_no <= len(tasks):
                    removed = tasks.pop(task_no - 1)
                    print(f"Deleted task: {removed['name']}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "6":
        print("Thank you for using the To-Do List Application!")
        break

    else:
        print("Invalid choice! Please try again.")