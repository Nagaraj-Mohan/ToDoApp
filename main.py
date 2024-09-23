#Python To DO APP

print("-- To Do APP Manager --")

while True:
    print("What you want to do (add, read, edit, complete, exit) in to do app?:")
    user_input = input()
    if 'add' in user_input:

        task_item = user_input[4:]

        with open("files/todo.txt", "r") as file:
            todos = file.readlines()

        todos.append(task_item + "\n")

        with open("files/todo.txt", "w") as file:
            file.writelines(todos)

        print(f"Added {task_item} to the todo list")

    elif "read" in user_input:
        with open("files/todo.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            print(f"{index+1} - {item.strip()}")

    elif "edit" in user_input:
        with open("files/todo.txt", "r") as file:
            todos = file.readlines()

        item_no = int(user_input[5:])

        print("What is the new task for this item?")
        item_value = input()+"\n"

        todos[item_no-1] =item_value
        with open("files/todo.txt", "w") as file:
            file.writelines(todos)

        print(f"Updated {item_value.strip("\n")} to the todo list")

    elif "complete" in user_input:
        with open("files/todo.txt", "r") as file:
            todos = file.readlines()

        print("Which item no. you have completed?")
        item_no = int(user_input[9:])

        to_remove_item = todos[item_no-1]
        todos.pop(item_no-1)

        with open("files/todo.txt", "w") as file:
            file.writelines(todos)

        print(f"Removed {to_remove_item.strip("\n")} from the todo list")

    elif "exit" in user_input:
        print("Bye")
        break

    else:
        print("This command is not recognized")