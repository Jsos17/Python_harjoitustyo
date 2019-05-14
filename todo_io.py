import os.path
from todo import Todo


def welcome():
    print("Todo-lista")
    print("Valitse toiminto kirjoittamalla haluttu komento:")
    print()

def choose_location():
    return input("Valitse tekstitiedosto tallennuspaikaksi antamalla komento: choose file, TAI lopeta komennolla: stop: ")

def program_closes():
    print("Ohjelma sulkeutuu, kiitos ja näkemiin!")

def list_commands():
    print("Listaa todot:", "list")
    print("Etsi todoja", "find")
    print("Uusi todo:", "new")
    print("Muokkaa todoa:", "update")
    print("Poista todo:", "delete")
    print("Muuta tallennuspaikkaa", "change file")
    print("Komentoapu:", "help")
    print("Lopeta:", "stop")

def commands_reminder():
    print("Anna komento:", "choose file", "TAI komento:", "stop")

def current_location(filename):
    print("Tämänhetkinen tallennustiedosto: ", filename)

def get_filename():
    print("Anna tallennustiedosto joka sijaitsee ohjelman suorituskansiossa (jos tiedostoa ei ole se luodaan) ja jonka pääte on .txt")
    return input("Anna tallennustiedoston nimi päätteellä: .txt TAI lopeta komennolla: cancel :")

def print_filename_instruction():
    print("Tiedoston nimen ja päätteen .txt yhteispituus tulee olla vähintään 5 merkkiä")

def file_ending_incorrect():
    print("Tiedostopääte on väärä")

def create_entry(todo):
    return todo.name + " | " + todo.description + " | " + todo.deadline + " | " + todo.priority + " | " + todo.done_status + "\n"

def find(filename):
    return input("Etsi todon nimen perusteella (tyhjä rivi palauttaa kaikki): ")

def print_matches(index_todo_tuple):
    indexes = index_todo_tuple[0]
    all_todos = index_todo_tuple[1]
    print()
    if len(indexes) > 0:
        print("Löydetyt avainsanaa vastaavat todot:")
        print("Rivinumero | Nimi | Kuvaus | Deadline | Prioriteetti | Status")
        for index in indexes:
            print(index, all_todos[index])
    else:
        print("Ei löydettyjä vastaavuksia")

def list_todos(todolist):
    if len(todolist) > 0:
        print("Löydetyt todot:")
        print("Nimi | Kuvaus | Deadline | Prioriteetti | Status")
        print()
        for entry in todolist:
            print(entry)
    else:
        print("Ei todoja")

def todo_create(filename):
    name = input("Tehtävän nimi: ")
    description = input("Kuvaus: ")
    deadline = input("Deadline: ")
    priority = input("Prioriteetti: ")
    done = input("Tehtävän status: ")
    print("Syötit:")
    print("|Nimi:", name, "|Kuvaus:", description, "|Deadline:", deadline, "|Prioriteetti:", priority, "|Status:", done)
    print()

    return input("Haluatko tallentaa (y/n)?: ")
        
def todo_modify(line):
    print("Jätä kenttä tyhjäksi jos et halua muuttaa sitä")
    inputs = []
    inputs.append(input("Tehtävän nimi: "))
    inputs.append(input("Kuvaus: "))
    inputs.append(input("Deadline: "))
    inputs.append(input("Prioriteetti: "))
    inputs.append(input("Tehtävän status: "))

    return inputs

def update_delete(status):
    if status == 0:
        return "Anna rivin numero mikä päivitetään (-1 peruuttaa toiminnon): "
    elif status == 1:
        return "Anna rivin numero mikä poistetaan (-1 peruuttaa toiminnon): "
    else:
        return ""

def cancel():
    print("Tominto peruutetaan")

def index_not_in_list():
    print("Indeksi ei kuulu listalle")

def not_in_Z():
    print("Ei ole kokonaisluku")

def file_error():
    print("Tiedostoa ei löydy!")

def save_message(status):
    if status == 0:
        print("Tallennus onnistui!")
    elif status == 1:
        print("Tiedostoa ei voitu luoda tai avata!")
    else:
        print("Tallennusta ei suoritettu")
        
def modify_status(todo):
    return input("Haluatko tallentaa (y/n)?: ")

def update_status(status):
    if status:
        print("Päivitys onnistui!")
    else:
        print("Päivitys epäonnistui")

def no_changes():
    print("Muutoksia ei tehty")

def delete_confirmation(index, todo):
    print("Poistettava Todo:", index, todo)
    return input("Poistetaanko rivi (y/n)?: ")
    
def delete_status(status):
    if status:
        print("Poistaminen onnistui!")
    else:
        print("Poistaminen epäonnistui!")
