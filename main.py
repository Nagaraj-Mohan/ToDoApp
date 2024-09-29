#Python To DO APP
from Utils import functions

print("-- To Do APP Manager --")

while True:
    file_path = "files/todo.txt"
    print("What you want to do (add, read, edit, complete, exit, export) in to do app?:")
    user_input = input()
    if  user_input.startswith('add'):

        task_item = user_input[4:]

        todos= functions.read_task(file_path)

        task_item_timestamp = functions.timestamp_task(task_item)
        todos.append(task_item_timestamp + "\n")

        functions.write_task(file_path, todos)

        print(f"Added {task_item} to the todo list")

    elif  user_input.startswith("read"):
        todos = functions.read_task(file_path)

        for index, item in enumerate(todos):
            print(f"{index+1} - {item.strip()}")

    elif  user_input.startswith("edit"):
        try:
            todos = functions.read_task(file_path)

            item_no = int(user_input[5:])

            print("What is the new task for this item?")
            item_value = input()
            task_item_timestamp = functions.timestamp_task(item_value)+"\n"

            todos[item_no-1] =task_item_timestamp
            functions.write_task(file_path, todos)

            print(f"Updated {item_value.strip("\n")} to the todo list")
        except ValueError:
            print("Invalid Command is given")
            continue


    elif  user_input.startswith("complete"):
        try:
            todos = functions.read_task(file_path)

            print("Which item no. you have completed?")
            item_no = int(user_input[9:])

            to_remove_item = todos[item_no-1]
            todos.pop(item_no-1)

            functions.write_task(file_path, todos)

            print(f"Removed {to_remove_item.strip("\n")} from the todo list")
        except ValueError:
            print("Invalid input is given")
            continue
        except IndexError:
            print("Invalid Task item is given")
            continue


    elif  user_input.startswith("export"):
        print("Can you give me the filename for export")
        file_name_csv = input()+".csv"
        file_path = "exports/"+file_name_csv
        functions.export_to_csv(file_path)


    elif  user_input.startswith("exit"):
        print("Bye")
        break

    else:
        print("This command is not recognized")