import src.todo_logic as logic
import src.todo_dao as dao
import src.todo_io as io


class Controller:

    def __init__(self):
        self. filename = "cancel"
        self.commands = {"new": self.new, "update": self.update, "delete": self.delete,
                         "change file": self.file_choice, "help": io.list_commands}

    def file_choice(self):
        while True:
            self.filename = io.set_filename()
            if self.filename == "cancel":
                break

            if logic.check_filename(self.filename):
                io.print_filename_instruction()
            else:
                if logic.file_ending(self.filename) == ".txt":
                    dao.create_file_if_not_exists(self.filename)
                    break
                else:
                    io.file_ending_incorrect()

    def new(self):
        todo = io.todo_create(self.filename)
        if io.save_confirmation() == "y":
            status = dao.save(self.filename, io.create_entry(todo))
            io.save_message(status)

    def update(self):
        keyword = io.find_keyword(self.filename)
        indexes_todos = dao.find(self.filename, keyword)
        todos = indexes_todos[1]
        if len(indexes_todos[0]) > 0:
            io.print_matches(indexes_todos)
        else:
            io.list_todos(todos)

        index = logic.get_index(len(todos), io.update_delete("update"))
        if index == -1:
            io.no_changes()
        elif index == -2:
            io.index_not_in_list()
        elif index == -3:
            io.not_in_Z()
        else:
            inputs = io.todo_modify()
            todo = logic.todo_modify(todos[index], inputs)
            todo_entry = io.create_entry(todo)

            if io.modify_status(todo) == "y":
                io.update_status(dao.update(
                    self.filename, todo_entry, index, todos))
            else:
                io.no_changes()

    def delete(self):
        keyword = io.find_keyword(self.filename)
        indexes_todos = dao.find(self.filename, keyword)
        todos = indexes_todos[1]
        if len(indexes_todos[0]) > 0:
            io.print_matches(indexes_todos)
        else:
            io.list_todos(todos)

        index = logic.get_index(len(todos), io.update_delete("delete"))
        if index != -1 and index != -2 and index != -3:
            if io.delete_confirmation(index, todos[index]) == "y":
                io.delete_status(dao.delete(
                    self.filename, index, todos))
            else:
                io.no_changes()

    def run(self):
        io.welcome()
        file_chosen = False
        while True:
            if file_chosen == False:
                choice = io.choose_location()
                if choice == "stop":
                    io.program_closes()
                    break
                elif choice == "choose file":
                    self.file_choice()
                    if self.filename != "cancel":
                        file_chosen = True
                        io.list_commands()
            else:
                io.current_location(self.filename)
                command = io.choose_command()
                if command == "stop":
                    io.program_closes()
                    break
                elif command == "list":
                    io.list_todos(dao.read(self.filename))
                elif command == "find":
                    keyword = io.find_keyword(self.filename)
                    io.print_matches(
                        dao.find(self.filename, keyword))
                elif command in self.commands:
                    self.commands[command]()
                else:
                    io.unknown_command()
