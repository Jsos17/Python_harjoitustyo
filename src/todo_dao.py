import os.path


def create_file_if_not_exists(filename):
    if not os.path.isfile(filename):
        with open(filename, "wt") as f:
            f.close()


def save(filename, entry):
    try:
        if os.path.isfile(filename):
            with open(filename, "at") as f:
                f.write(entry)
        else:
            with open(filename, "wt") as f:
                f.write(entry)

        return True
    except OSError:
        return False


def read(filename):
    l = []
    try:
        with open(filename, "rt") as f:
            for line in f:
                l.append(line.strip())
    except FileNotFoundError:
        pass

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
        pass

    return (indexes, all_todos)


def update(filename, todo_entry, index, todos):
    try:
        temp_filename = filename + ".tmp"
        with open(temp_filename, "wt") as tempfile:
            for i, todo in enumerate(todos):
                if i == index:
                    tempfile.write(todo_entry)
                else:
                    tempfile.write(todo + "\n")

        os.replace(temp_filename, filename)
        return True
    except OSError:
        return False


def delete(filename, index, todos):
    try:
        temp_filename = filename + ".tmp"
        with open(temp_filename, "wt") as tempfile:
            for i, todo in enumerate(todos):
                if i != index:
                    tempfile.write(todo + "\n")

        os.replace(temp_filename, filename)
        return True
    except OSError:
        return False
