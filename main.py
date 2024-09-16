#Python To DO APP

print("-- To Do APP Manager --")

while True:
    print("What you want to do (add, read, edit, complete, exit) in to do app?:")
    user_input = input()
    match user_input:
        case "add":

            print("Enter the task you want to add:")
            task_item = input()

            with open("files/todo.txt", "r") as file:
                todos = file.readlines()

            todos.append(task_item + "\n")

            with open("files/todo.txt", "w") as file:
                file.writelines(todos)

            print(f"Added {task_item} to the todo list")

        case "read":
            with open("files/todo.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                print(f"{index+1} - {item.strip()}")

        case "edit":
            with open("files/todo.txt", "r") as file:
                todos = file.readlines()

            print("Which item no. you want to edit?")
            item_no = int(input())

            print("What is the new task for this item?")
            item_value = input()+"\n"

            todos[item_no-1] =item_value
            with open("files/todo.txt", "w") as file:
                file.writelines(todos)

            print(f"Updated {item_value.strip("\n")} to the todo list")

        case "complete":
            with open("files/todo.txt", "r") as file:
                todos = file.readlines()

            print("Which item no. you have completed?")
            item_no = int(input())

            to_remove_item = todos[item_no-1]
            todos.pop(item_no-1)

            with open("files/todo.txt", "w") as file:
                file.writelines(todos)

            print(f"Removed {to_remove_item.strip("\n")} from the todo list")

        case "exit":
            print("Bye")
            break

        case _ :
            print("This command is not recognized")