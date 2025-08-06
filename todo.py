

file_name = "tasks.txt"  
tasks = []                

#reading task from file
def load_tasks():
    try:
        f = open(file_name, "r")   
        for line in f:
            line = line.strip()    
            if line.startswith("(DONE)"):
                title = line[6:].strip()
                tasks.append({"title": title, "done": True})
            elif line.startswith("(TODO)"):
                title = line[6:].strip()
                tasks.append({"title": title, "done": False})
        f.close()
    except FileNotFoundError:
        
        pass

#to write and save tasks
def save_tasks():
    f = open(file_name, "w")  
    for task in tasks:
        if task["done"]:
            f.write("(DONE) " + task["title"] + "\n")
        else:
            f.write("(TODO) " + task["title"] + "\n")
    f.close()

#choose one task
def show_menu():
    print("\n===== MY TO-DO LIST =====")
    print("1. Show my tasks")
    print("2. Add a task")
    print("3. Mark a task as done")
    print("4. Delete a task")
    print("5. Exit")

#list of tasks
def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks right now. You are free! 🎉")
    else:
        print("\nYour tasks:")
        num = 1
        for task in tasks:
            if task["done"]:
                status = "(DONE)"
            else:
                status = "(TODO)"
            print(str(num) + ". " + status + " " + task["title"])
            num += 1


def add_task():
    name = input("Type your new task: ").strip()
    if name != "":
        tasks.append({"title": name, "done": False})
        save_tasks()
        print("Task added.")
    else:
        print("You must type something")


def mark_done():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        num = int(input("Which task number is done? "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks()
            print("Marked task as done")
        else:
            print("That number is not here")
    except ValueError:
        print("Please type a number.")


def delete_task():
    view_tasks()
    if len(tasks) == 0:
        return
    try:
        num = int(input("Which task number to delete? "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks()
            print("Deleted: " + removed["title"])
        else:
            print("That number is not in the list.")
    except ValueError:
        print("Please type a number.")

# Main program 
def main():
    load_tasks()
    print("Welcome to My To-Do List!")
    while True:
        show_menu()
        choice = input("Pick 1-5: ").strip()
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Goodbye! Have a nice day.")
            break
        else:
            print("Wrong choice, try again.")

main()
