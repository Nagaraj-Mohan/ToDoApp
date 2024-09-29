import csv
from datetime import datetime


def read_task(file_path):
    """ Read Task functions accepts the file path where to-do list is present
        and then it reads the lists from txt file and sends  the list to the calling function
        as output
    """

    todos_ = []
    with open(file_path, "r") as file:
        todos_ = file.readlines()
    return  todos_

def write_task(file_path, todos):
    """ Write Task functions accepts the file path as well as the todo list and
     then it writes the lists to txt file """

    with open(file_path, "w") as file:
        file.writelines(todos)

def export_to_csv(file_path_csv):
    file_path_txt = "files/todo.txt"
    todos = read_task(file_path_txt)
    with open(file_path_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Task List"]) # Add Heading
        for item in todos:
            writer.writerow([item.strip()]) # Add each task as a row to CSV
    print(f"Exported tasks to csv file:{file_path_csv}")

def timestamp_task(task):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{task} (Added on:{timestamp})"