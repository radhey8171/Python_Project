import json
import os
FILE = "taxks.json"

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE,"r") as f:
            return json.load(f)
    return[]

def save_tasks():
    with open(FILE,"w") as f:
        json.dump(tasks,f,indent=4)
tasks = load_tasks()

def add_task():
    task = input("Enter Task:")
    tasks.append({"task":task,"done":False})
    save_tasks()
    print("Task Added Successfully!")

def view_tasks():
    if not tasks:
        print("No Tasks Available!")
        return

    print("\n-----TO-DO-LIST-----")
    for i, t in enumerate(tasks,1):
        status = "Completed" if t["done"] else "Pending"
        print(f"{i}.{t['task']} [{status}]")

def update_task():
    view_tasks()
    if tasks:
        n = int(input("Enter Task Number:"))
        if 1 <= n <= len(tasks):
            tasks[n-1]["task"] = input("Enter New Task:")
            save_tasks()
            print("Task Updated Successfully!")
        else:
            print("Invalid Task Number!")

def delete_task():
    view_tasks()
    if tasks:
        n = int(input("Enter Task Number:"))
        if 1 <= n <= len(tasks):
            tasks.pop(n-1)
            save_tasks()
            print("Task Deleted Successfully!")
        else:
            print("Invalid Task Number!")

def mark_done():
    view_tasks()
    if tasks:
        n = int(input("Enter Task Number:"))
        if 1 <= n <= len(tasks):
            tasks[n-1]["done"] = True
            save_tasks()
            print("Task Marked as Completed!")
        else:
            print("Invalid Task Number!")

while True:
    print("\n=====TO-DO-LIST=====")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

    choice = input("Enter YOur Choice:")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        mark_done()
    elif choice == "6":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")

        

            
            


