import json

def speichere_todos(todos):
    with open("todos.json", "w") as f:
        json.dump(todos, f)

def lade_todos():
    try:
        with open("todos.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return[]

def zeige_todos(todos):
    if not todos:
        print("")
        print("Die Liste ist leer")
    for index, liste in enumerate(todos):
        if liste["Erledigt"] == True:
            print(index, ":", "[x]", liste["Aufgabe"])
        else:
            print(index, ":", "[]", liste["Aufgabe"])


def markiere_todos(todos):
    weiter = True
    while weiter:
        try:
            zeige_todos(todos)
            if not todos:
                break
            nummer = int(input("Welche Todos ist erledigt?"))
            if todos[nummer]["Erledigt"] == True:
                print("")
                print("Dieser Punkt wurde bereits durchgeführt")
            else:
                todos[nummer]["Erledigt"] = True
                speichere_todos(todos)
                print("Die Todo wurde als durchgeführt markiert")
        except (IndexError, ValueError):
            print("")
            print("Diese Nummer gibt es nicht")

        antwort = input("Weiter Aufgabe als durchgeführt auswählen? (Y/N)")
        if antwort != "Y":
            weiter = False

def fuege_todo_hinzu(todos):
    weiter = True
    while weiter:
        aufgabe = input("Neue Aufgabe: ")
        todos.append({"Aufgabe": aufgabe, "Erledigt": False})
        speichere_todos(todos)
        antwort = input("Weitere Aufgabe hinzufügen? (Y/N)")
        if antwort != "Y":
            weiter = False

def loesche_todo(todos):
    weiter = True
    while weiter:
        try:
            zeige_todos(todos)
            if not todos:
                break
            loeschen = int(input("Welche Todo möchtest du löschen?"))
            del todos[loeschen]
            speichere_todos(todos)
            antwort = input("Weitere Aufgabe löschen? (Y/N)")
            if antwort != "Y":
                weiter = False
        except (IndexError, ValueError):
            print("")
            print("Diese Nummer gibt es nicht")
        else:
            print ("Erfolgreich gelöscht")


todos = lade_todos()

while True:
    print("\n1 - Todo hinzufügen")
    print("2 - Todos anzeigen")
    print("3 - Todo erledigt")
    print("4 - Todo löschen")
    print("5 - Beenden")
    auswahl = input("Was möchtest du tun?")

    if auswahl == "1":
        fuege_todo_hinzu(todos)
    elif auswahl == "2":
        zeige_todos(todos)
    elif auswahl == "3":
        markiere_todos(todos)
    elif auswahl == "4":
        loesche_todo(todos)
    elif auswahl == "5":
        break

    else:
        print("Ungültige Auswahl")
