from src.todo import Todo


def check_filename(filename):
    return len(filename) <= 4


def file_ending(filename):
    return filename[len(filename) - 4:]


def todo_modify(line, inputs):
    fields = line.strip().split("|")
    todo_fields = []
    for i in range(5):
        if inputs[i] == "":
            if i < len(fields):
                todo_fields.append(fields[i].strip())
            else:
                todo_fields.append("")
        else:
            todo_fields.append(inputs[i])

    return Todo(*todo_fields)


def get_index(list_length, instruction):
    index = -1
    try:
        index = int(instruction)
        if index >= -1 and index < list_length:
            return index
        else:
            return -2
    except ValueError:
        return -3
