import os.path

class Todo:
    def __init__(self, name, description, deadline, priority, done_status):
        self.name = name
        self.description = description
        self.deadline = deadline
        self.priority = priority
        self.done_status = done_status

def file_name_checker():
    filename = ""
    while True:
        filename = input("Anna tallennustiedoston nimi päätteellä: .txt (jos tiedostoa ei ole se luodaan): ")
        fn_len = len(filename)
        if fn_len <= 4:
            print("Tiedoston nimen ja päätteen .txt yhteispituus tulee olla vähintään 5 merkkiä")
        elif fn_len > 100:
            print("Tiedostonimi on liian pitkä")
        else:
            end = fn_len
            start = fn_len - 4
            if filename[start:end] == ".txt":
                break
            else:
                print("Tiedostopääte on väärä")
    return filename

def save(filename, todo):
    try:
        entry = todo.name + " | " + todo.description + " | " + todo.deadline + " | " + todo.priority + " | " + todo.done_status + "\n"
        if os.path.isfile(filename):
            with open(filename, "at") as f:
                f.write(entry)
        else:
            with open(filename, "wt") as f:
                f.write(entry)
    except OSError:
        print("Tiedostoa ei voitu luoda tai avata!")

def read(filename):
    l = []
    try:
        with open(filename, "rt") as f:
            for line in f:
                l.append(line.strip())
    except FileNotFoundError:
        print("Tiedostoa ei löydy!")
    return l

def find():
    filename = input("Anna tiedoston nimi (Tiedoston pitää olla komennon suorituskansion sisällä): ")
    keyword = input("Etsi todon nimen perusteella: ")
    todo_matches = []
    try:
        with open(filename, "rt") as f:
            for line in f:
                todo_string = line.strip()
                name = todo_string.split("|")[0].strip()
                if keyword in name:
                    todo_matches.append(todo_string)

        if len(todo_matches) > 0:
            print("Löydetyt avainsanaa vastaavat todot:")
            print()
            print("Nimi | Kuvaus | Deadline | Prioriteetti | Status")
            for match in todo_matches:
                print(match)
        else:
            print()
            print("Ei löydettyjä vastaavuksia")
    except FileNotFoundError:
        print("Tiedostoa ei löydy!")
    
def update(filename):
    pass

def delete(filename):
    pass

def todo_list():
    filename = input("Anna tiedoston nimi (Tiedoston pitää olla komennon suorituskansion sisällä): ")
    todolist = read(filename)
    if len(todolist) > 0:
        print("Löydetyt todot:")
        print("Nimi | Kuvaus | Deadline | Prioriteetti | Status")
        print()
        for entry in todolist:
            print(entry)
    else:
        print("Ei todoja")

def todo_create():
    name = input("Tehtävän nimi: ")
    description = input("Kuvaus: ")
    deadline = input("Deadline: ")
    priority = input("Prioriteetti: ")
    done = input("Tehtävän status: ")
    print("Syötit:")
    print("|Nimi:", name, "|Kuvaus:", description, "|Deadline:", deadline, "|Prioriteetti:", priority, "|Status:", done)
    print()

    save_status = input("Haluatko tallentaa? (y/n): ")
    if save_status == "y":
        filename = file_name_checker()
        todo = Todo(name, description, deadline, priority, done)
        save(filename, todo)
        print("Tallennus onnistui!")
    else:
        print("Tallennusta ei suoritettu")

def main():
    print("Todo-lista")
    print("Valitse toiminto kirjoittamalla haluttu komento:")
    print("Listaa todot:", "L")
    print("Etsi todoja", "E")
    print("Uusi todo:", "U")
    print("Muokkaa todoa:", "M")
    print("Poista todo:", "P")
    print("Komentoapu:", "help")
    print("Lopeta:", "stop")
    print()

    while True:    
        command = input("Valitse (L, E, U, M, P, help, stop): ")
        if command == "L":
            todo_list()
        elif command == "E":
            find()
        elif command == "U":
            todo_create()
        elif command == "M":
            print("Muokkaa")
        elif command == "P":
            print("Poista")
        elif command == "help":
            print("|Listaa todot: L", "|Etsi todoja: E", "|Uusi todo: U", "|Muokkaa todoa: M", "|Poista todo: P") 
            print("|Lopeta: stop", "|Komentoapu: help")
        elif command == "stop":
            print("Ohjelma sulkeutuu, kiitos ja näkemiin!")
            break
        else:
            print("Tuntematon komento!")
            print("Kirjoita help saadaksesi apua")
        print()

main()