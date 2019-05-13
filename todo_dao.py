import os.path
from todo import Todo
import todo_io
import todo_logic 


def open_file(filename):
    if not os.path.isfile(filename):
        with open(filename, "wt") as f:
            f.close()

def save(filename, todo):
    try:
        entry = todo_io.create_entry(todo)
        if os.path.isfile(filename):
            with open(filename, "at") as f:
                f.write(entry)
        else:
            with open(filename, "wt") as f:
                f.write(entry)

        todo_io.save_message(True)
    except OSError:
        todo_io.save_message(False)
    
def read(filename):
    l = []
    try:
        with open(filename, "rt") as f:
            for line in f:
                l.append(line.strip())
    except FileNotFoundError:
        todo_io.file_error
    return l

def find(filename, keyword):
    indexes = []
    all_todos = []
    try:
        with open(filename, "rt") as f:
            i = 0
            for line in f:
                todo_string = line.strip()
                all_todos.append(todo_string)
                if keyword in todo_string.split("|")[0].strip():
                    indexes.append(i)
                i += 1
                
    except FileNotFoundError:
        todo_io.file_error
    
    return (indexes, all_todos)

def update(filename, keyword):
    indexes_todos = find(filename, keyword)
    todos = indexes_todos[1]
    if len(indexes_todos[0]) > 0:
        index = todo_logic.get_index(len(todos), "update")
        if (index != -1):
            todo = todo_logic.todo_modify(todos[index])
            if todo_io.modify_status(todo) == "y":
                try:
                    temp_filename = filename + ".tmp"
                    with open(temp_filename, "wt") as tempfile:
                        for i in range(len(todos)):
                            if i == index:
                                tempfile.write(todo_io.create_entry(todo) + "\n")
                            else:  
                                tempfile.write(todos[i] + "\n")
                    
                    os.replace(temp_filename, filename)
                    todo_io.update_status(True)
                except OSError:
                    todo_io.update_status(False)
            else:
                todo_io.no_changes

def delete(filename, keyword):
    indexes_todos = find(filename, keyword)
    todos = indexes_todos[1]
    if len(indexes_todos[0]) > 0:
        index = todo_logic.get_index(len(todos), "delete")
        
        if index != -1:
            if todo_io.delete_confirmation(index, todos[index]) == "y":
                try:
                    temp_filename = filename + ".tmp"
                    with open(temp_filename, "wt") as tempfile:
                        for i in range(len(todos)):
                            if i != index:  
                                tempfile.write(todos[i] + "\n")
                    
                    os.replace(temp_filename, filename)
                    todo_io.delete_status(True)
                except OSError:
                    todo_io.delete_status(False)
            else:
                todo_io.no_changes

def todo_list(filename):
    todolist = read(filename)
    todo_io.list_todos(todolist)
