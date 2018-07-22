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
        filename = input("Anna tiedostonimi joka päättyy '.txt' (jos tiedostoa ei ole se luodaan): ")
        fn_len = len(filename)
        if fn_len <= 4:
            print("Tiedoston nimen ja päätteen '.txt' yhteispituus tulee olla vähintään 5 merkkiä")
        elif fn_len > 100:
            print("Tiedostonimi on liian pitkä")
        else:
            end = len(filename)
            start = len(filename) - 4
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
        print("Tiedostoa ei voitu luoda tai avata")

def read(filename):
    try:
        l = []
        f = open(filename, "rt")
        for line in f:
            l.append(line.strip())
        f.close()
        return l
    except FileNotFoundError:
        print("Tiedostoa ei löydy")

def todo_create():
    name = input("Tehtävän nimi: ")
        description = input("Kuvaus: ")
        deadline = input("Deadline: ")
        priority = input("Prioriteetti: ")
        done = input("Tehtävän status: ")
        todo = Todo(name, description, deadline, priority, done)

        print("Syötit:")
        print("|Nimi:", name, "|Kuvaus:", description, "|Deadline:", deadline, "|Prioriteetti:", priority, "|Status:", done)
        return todo

def main():
    print("Todo-lista")
    while True:
        todo = todo_create()
        save_status = input("Haluatko tallentaa? (y/n): ")
        if save_status == "y":
            filename = file_name_checker()
            save(filename, todo)
            print("Tallennus onnistui!")
        else:
            print("Tallennusta ei suoritettu")

        print("") 
        cont = input("Haluatko jatkaa? (y/n): ")
        if cont == "n":
            print("Ohjelma sulkeutuu!")
            break
            
main()
l = read("todo.txt")
for entry in l:
        print(entry)