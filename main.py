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

        case _:
            print("Bye")
            break

