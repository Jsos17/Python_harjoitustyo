import os.path

# A small class to encapsulate the Todo concept
# Todot on päätetty luoda luokaksi helpottamaan ohjelmointia ja mahdollistamaan jatkokehityksen
class Todo:
    def __init__(self, name, description, deadline, priority, done_status):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.done_status = done_status

# This method checks that the file ending is correct i.e. .txt
# Tarkistaa, että tiedostopääte on haluttu .txt
def file_choice():
    filename = ""
    while True:
        print("Anna tallennustiedosto joka sijaitsee ohjelman suorituskansiossa (jos tiedostoa ei ole se luodaan) ja jonka pääte on .txt")
        filename = input("Anna tallennustiedoston nimi päätteellä: .txt TAI lopeta komennolla: cancel :")
        if filename == "cancel":
            break
        fn_len = len(filename)
        if fn_len <= 4:
            print("Tiedoston nimen ja päätteen .txt yhteispituus tulee olla vähintään 5 merkkiä")
        else:
            end = fn_len
            start = fn_len - 4
            if filename[start:end] == ".txt":
                if not os.path.isfile(filename):
                    with open(filename, "wt") as f:
                        f.close()
                break
            else:
                print("Tiedostopääte on väärä")
    return filename

# Writes the todo entry into the specified file
# Tallentaa todon parametrina annettavaan tiedostoon
def save(filename, todo):
    try:
        entry = todo.name + " | " + todo.description + " | " + todo.deadline + " | " + todo.priority + " | " + todo.done_status + "\n"
        if os.path.isfile(filename):
            with open(filename, "at") as f:
                f.write(entry)
        else:
            with open(filename, "wt") as f:
                f.write(entry)

        print("Tallennus onnistui!")
    except OSError:
        print("Tiedostoa ei voitu luoda tai avata!")

# Reads every line of a text file and saves the line to a list and then returns the list
# Lukee tekstitiedoston joka rivin ja tallentaa rivit listalle, ja lopuksi palauttaa listan
def read(filename):
    l = []
    try:
        with open(filename, "rt") as f:
            for line in f:
                l.append(line.strip())
    except FileNotFoundError:
        print("Tiedostoa ei löydy!")
    return l

# Finds all matches based on the name of the todo and returns a tuple of found indexes in a list and all the Todos in another list 
# Etsii todoja nimen perusteella ja palauttaa tuplen jossa on löydettyjen vastaavuuksien indeksit ja toisena kaikki Todot
def find(filename):
    keyword = input("Etsi todon nimen perusteella (tyhjä rivi palauttaa kaikki): ")
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
                
        print()
        if len(indexes) > 0:
            print("Löydetyt avainsanaa vastaavat todot:")
            print("Rivinumero | Nimi | Kuvaus | Deadline | Prioriteetti | Status")
            for index in indexes:
                print(index, all_todos[index])
        else:
            print("Ei löydettyjä vastaavuksia")

    except FileNotFoundError:
        print("Tiedostoa ei löydy!")
    
    return (indexes, all_todos)

# Finds Todos based on their name, and then based on the index of the Todo, the user can modify the particular Todo
# Etsii Todoja nimen perusteella ja sitten käyttäjä voi valita muokattavan Todon indeksin perusteella ja päivittää kyseisen entryn
def update(filename):
    indexes_todos = find(filename)
    todos = indexes_todos[1]
    if len(indexes_todos[0]) > 0:
        index = get_index(len(todos), "update")
        if (index != -1):
            todo = todo_modify(todos[index])
            entry = todo.name + " | " + todo.description + " | " + todo.deadline + " | " + todo. priority + " | " + todo.done_status
            print("Muokattu todo:", entry)
            modify_status = input("Haluatko tallentaa (y/n)?: ")
            if modify_status == "y":
                try:
                    temp_filename = filename + ".tmp"
                    with open(temp_filename, "wt") as tempfile:
                        for i in range(len(todos)):
                            if i == index:
                                tempfile.write(entry + "\n")
                            else:  
                                tempfile.write(todos[i] + "\n")
                    
                    os.replace(temp_filename, filename)
                    print("Päivitys onnistui!")
                except OSError:
                    print("Päivitys epäonnistui!")
            else:
                print("Muutoksia ei tehty")

# Finds the desired Todo and then the user can delete said Todo based on its index
# Etsii Todoja nimen perusteella ja sitten käyttäjä voi poistaa Todon indeksin perusteella
def delete(filename):
    indexes_todos = find(filename)
    todos = indexes_todos[1]
    if len(indexes_todos[0]) > 0:
        index = get_index(len(todos), "delete")
        
        if index != -1:
            print("Poistettava Todo:", index, todos[index])
            confirmation = input("Poistetaanko rivi (y/n)?: ")
            if confirmation == "y":
                try:
                    temp_filename = filename + ".tmp"
                    with open(temp_filename, "wt") as tempfile:
                        for i in range(len(todos)):
                            if i != index:  
                                tempfile.write(todos[i] + "\n")
                    
                    os.replace(temp_filename, filename)
                    print("Poistaminen onnistui!")
                except OSError:
                    print("Poistaminen epäonnistui!")
            else:
                print("Muutoksia ei tehty")

# Lists every todo found in a text file
# Listaa todot jotka löytyvät tekstiedostosta
def todo_list(filename):
    todolist = read(filename)
    if len(todolist) > 0:
        print("Löydetyt todot:")
        print("Nimi | Kuvaus | Deadline | Prioriteetti | Status")
        print()
        for entry in todolist:
            print(entry)
    else:
        print("Ei todoja")

# Creates a new todo which the user can then save into a text file
# Luo uuden todon jonka käyttäjä voi halutessaan tallentaa tekstitiedostoon
def todo_create(filename):
    name = input("Tehtävän nimi: ")
    description = input("Kuvaus: ")
    deadline = input("Deadline: ")
    priority = input("Prioriteetti: ")
    done = input("Tehtävän status: ")
    print("Syötit:")
    print("|Nimi:", name, "|Kuvaus:", description, "|Deadline:", deadline, "|Prioriteetti:", priority, "|Status:", done)
    print()

    save_status = input("Haluatko tallentaa (y/n)?: ")
    if save_status == "y":
        save(filename, Todo(name, description, deadline, priority, done))
    else:
        print("Tallennusta ei suoritettu")

# The user can modify existing Todos without having to rewrite the whole Todo by simply leaving the input prompt blank when no modification is desired
# Käyttäjä voi muokata Todoa jättämällä ennalleenjätettävät rivit tyhjäksi, ja kirjoittamalla vain muokattaviin kohtiin
def todo_modify(line):
    fields = line.strip().split("|")
    print("Jätä kenttä tyhjäksi jos et halua muuttaa sitä")
    inputs = []
    inputs.append(input("Tehtävän nimi: "))
    inputs.append(input("Kuvaus: "))
    inputs.append(input("Deadline: "))
    inputs.append(input("Prioriteetti: "))
    inputs.append(input("Tehtävän status: "))

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

# Returns the index of Todo in the list which is to be updated or deleted, checks the appropriate range of the index
# Palauttaa päivitettävän/poistettavan Todon indeksin listalla, ja tarkistaa että indeksi on sallituissa rajoissa
def get_index(list_length, mode):
    instruction = ""
    index = -1
    if mode == "update":
        instruction = "Anna rivin numero mikä päivitetään (-1 peruuttaa toiminnon): "
    elif mode == "delete":
        instruction = "Anna rivin numero mikä poistetaan (-1 peruuttaa toiminnon): "
    else:
        return index

    while True:
        try:
            index = int(input(instruction))
            if index >= 0 and index < list_length:
                break
            elif index == -1:
                print("Tominto peruutetaan")
                break
            else:
                print("Indeksi ei kuulu listalle")
        except ValueError:
            print("Ei ole kokonaisluku")
    return index

# User interface: First, the user chooses the file to be used as the database and second, the user can then manipulate the database 
# Käyttöliittymä: 1) Käyttäjä valitsee tallennustiedoston, 2) Käyttäjä voi manipuloida tiedoston sisältöä
def main():
    print("Todo-lista")
    print("Valitse toiminto kirjoittamalla haluttu komento:")
    print()

    file_chosen = False
    filename = "cancel"
    while True:
        if file_chosen == False:
            choice = input("Valitse tekstitiedosto tallennuspaikaksi antamalla komento: choose file, TAI lopeta komennolla: stop: ")
            if choice == "stop":
                print("Ohjelma sulkeutuu, kiitos ja näkemiin!")
                break
            elif choice == "choose file":
                filename = file_choice()
                if filename != "cancel":
                    file_chosen = True
                    print("Listaa todot:", "list")
                    print("Etsi todoja", "find")
                    print("Uusi todo:", "new")
                    print("Muokkaa todoa:", "update")
                    print("Poista todo:", "delete")
                    print("Muuta tallennuspaikkaa", "change file")
                    print("Komentoapu:", "help")
                    print("Lopeta:", "stop")
            else:
                print("Anna komento:", "choose file", "TAI komento:", "stop")
        else:
            print("Tämänhetkinen tallennustiedosto: ", filename)
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

main()