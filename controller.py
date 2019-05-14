from todo import Todo
import todo_logic
import todo_dao
import todo_io

def main():
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
            command = input("Valitse (list, find, new, update, delete, change file, help, stop): ")
            if command == "list":
                todo_list(filename)
            elif command == "find":
                find(filename)
            elif command == "new":
                todo_create(filename)
            elif command == "update":
                update(filename)
            elif command == "delete":
                delete(filename)
            elif command == "change file":
                f2 = file_choice()
                if f2 != "cancel":
                    filename = f2
            elif command == "help":
                print("| Listaa todot: list", "| Etsi todoja: find", "| Uusi todo: new", "| Muokkaa todoa: update", "| Poista todo: delete") 
                print("| Vaihda tallenustiedosto: change file", "| Komentoapu: help", "| Lopeta: stop")
            elif command == "stop":
                print("Ohjelma sulkeutuu, kiitos ja näkemiin!")
                break
            else:
                print("Tuntematon komento!")
                print("Kirjoita help saadaksesi apua")
        print()

def file_choice():
    filename = ""
    while True:        
        filename = todo_io.get_filename
        if filename == "cancel":
            break

        if todo_logic.check_filename(filename):
            todo_io.print_filename_instruction()
        else:
            startend = todo_logic.name_len(filename)
            if filename[startend[0]:startend[1]] == ".txt":
                todo_dao.open_file(filename)
                break
            else:
                todo_io.file_ending_incorrect()
    return filename

# def command_hashtable(command_list):
