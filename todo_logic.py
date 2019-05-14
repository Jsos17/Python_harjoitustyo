from todo import Todo

def check_filename(filename):
    return len(filename) <= 4

def name_len(filename):
    fn_len = len(filename)
    return [fn_len, fn_len - 4]
    
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

def get_index(list_length, status):
    instruction = todo_io.update_delete(status)
    index = -1
    if instruction == "":
        return index

    while True:
        try:
            index = int(input(instruction))
            if index >= 0 and index < list_length:
                break
            elif index == -1:
                todo_io.cancel
                break
            else:
                todo_io.index_not_in_list
        except ValueError:
            todo_io.not_in_Z
    return index