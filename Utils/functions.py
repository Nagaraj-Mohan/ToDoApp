

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
