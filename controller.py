from todo import Todo
import todo_logic
import todo_dao
import todo_io


def file_choice():
    filename = ""
    while True:
        filename = todo_io.get_filename()
        if filename == "cancel":
            break

        if todo_logic.check_filename(filename):
            todo_io.print_filename_instruction()
        else:
            if todo_logic.file_ending(filename) == ".txt":
                todo_dao.open_file(filename)
                break
            else:
                todo_io.file_ending_incorrect()
    return filename


def new(filename):
    todo = todo_io.todo_create(filename)
    if todo_io.save_confirmation() == "y":
        status = todo_dao.save(filename, todo_io.create_entry(todo))
        todo_io.save_message(status)


def update(filename):
    keyword = todo_io.find_keyword(filename)
    indexes_todos = todo_dao.find(filename, keyword)
    todos = indexes_todos[1]
    if len(indexes_todos[0]) > 0:
        todo_io.print_matches(indexes_todos)
    else:
        todo_io.list_todos(todos)

    instruction = todo_io.update_delete("update")
    index = todo_logic.get_index(len(todos), instruction)
    if index == -1:
        todo_io.no_changes()
    elif index == -2:
        todo_io.index_not_in_list()
    elif index == -3:
        todo_io.not_in_Z()
    else:
        inputs = todo_io.todo_modify()
        todo = todo_logic.todo_modify(todos[index], inputs)
        todo_entry = todo_io.create_entry(todo)

        if todo_io.modify_status(todo) == "y":
            todo_io.update_status(todo_dao.update(
                filename, todo_entry, index, todos))
        else:
            todo_io.no_changes()


def delete(filename):
    keyword = todo_io.find_keyword(filename)
    indexes_todos = todo_dao.find(filename, keyword)
    todos = indexes_todos[1]
    if len(indexes_todos[0]) > 0:
        todo_io.print_matches(indexes_todos)
    else:
        todo_io.list_todos(todos)

    instruction = todo_io.update_delete("delete")
    index = todo_logic.get_index(len(todos), instruction)
    if index != -1 and index != -2 and index != -3:
        if todo_io.delete_confirmation(index, todos[index]) == "y":
            todo_io.delete_status(todo_dao.delete(filename, index, todos))
        else:
            todo_io.no_changes()


def control():
    todo_io.welcome()
    file_chosen = False
    filename = "cancel"
    while True:
        if file_chosen == False:
            choice = todo_io.choose_location()
            if choice == "stop":
                todo_io.program_closes()
                break
            elif choice == "choose file":
                filename = file_choice()
                if filename != "cancel":
                    file_chosen = True
                    todo_io.list_commands()
            else:
                todo_io.commands_reminder()
        else:
            todo_io.current_location(filename)
            command = todo_io.choose_command()
            if command == "list":
                todo_io.list_todos(todo_dao.read(filename))
            elif command == "find":
                keyword = todo_io.find_keyword(filename)
                todo_io.print_matches(todo_dao.find(filename, keyword))
            elif command == "new":
                new(filename)
            elif command == "update":
                update(filename)
            elif command == "delete":
                delete(filename)
            elif command == "change file":
                f2 = file_choice()
                if f2 != "cancel":
                    filename = f2
            elif command == "help":
                todo_io.list_commands()
            elif command == "stop":
                todo_io.program_closes()
                break
            else:
                todo_io.unknown_command()
        print()
