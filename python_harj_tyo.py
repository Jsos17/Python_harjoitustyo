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
        filename = input("Anna tiedostonimi joka päättyy '.txt': ")
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

def file_reader(filename):
    try:
        l = []
        f = open(filename, "rt")
        for line in f:
            l.append(line.strip())
        f.close()
        return l
    except FileNotFoundError:
        print("Tiedostoa ei löydy")

def main():
    print("Todo-lista")
    while True:
        name = input("Tehtävän nimi: ")
        description = input("Kuvaus: ")
        deadline = input("Deadline: ")
        priority = input("Prioriteetti: ")
        done = input("Tehtävän status: ")

        print("Syötit:")
        print("| Nimi:", name, "| Kuvaus:", description, "| Deadline:", deadline, "| Prioriteetti:", priority, "| Status:", done)
        save = input("Haluatko tallentaa? (y/n)")
        if save == "y":
            print("Tallennus onnistui!")
        else:
            print("Tallennusta ei suoritettu")
        
        cont = input("Haluatko jatkaa? (y/n): ")
        if cont == "n":
            print("Ohjelma sulkeutuu")
            break

# file_name_checker()
main()