from todo import Todo


def check_filename(filename):
    return len(filename) <= 4


def file_ending(filename):
    fn_len = len(filename)
    return filename[fn_len - 4:fn_len]


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

    return Todo(todo_fields[0], todo_fields[1], todo_fields[2], todo_fields[3], todo_fields[4])


def get_index(list_length, instruction):
    index = -1
    while True:
        try:
            index = int(instruction)
            if index >= -1 and index < list_length:
                break
            else:
                return -2
        except ValueError:
            return -3
    return index
