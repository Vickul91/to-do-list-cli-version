# TO DO LIST CLI VERSION
# Author Przemyslaw Ksiazek Vickul

user_choice = 0
tasks = []

def show_tasks():
    tasks_index = 0
    print('----------------------------------------------------')
    print("Zadania:")
    for task in tasks:
        print(f"{task} [{tasks_index}]")
        tasks_index += 1
    print('----------------------------------------------------')

def add_task():
    new_tasks = str(input("Wpisz treść zadania: "))
    tasks.append(new_tasks)
    print('Zadanie zostało dodane!')

def delete_task():
    task_to_delete = int(input("Wpisz indeks zadania, które chcesz usunąć: "))
    if task_to_delete < 0 or task_to_delete > len(tasks) - 1:
        print("Brak zadania o podanym indeksie.")
        return
    else:
        tasks.pop(task_to_delete)
        print('Zadanie zostało usunięte!')

def modify_task():
    task_to_modify = int(input("wpisz indeks zadania, które chcesz zmodyfikować: "))
    if task_to_modify < 0 or task_to_modify > len(tasks) - 1:
        print("Brak zadania o podanym indeksie.")
        return
    else:
        new_task_content = str(input("Podaj treść zadania: "))
        tasks[task_to_modify] = new_task_content

def save_to_file():
    file = open('tasks.txt', 'w')
    for task in tasks:
        file.write(task + '\n')

    file.close()
    print('Plik został zapisany!')

def load_task_from_file():
    try:
        file = open('tasks.txt')

        for line in file.readlines():
            tasks.append(line.strip())

        file.close()
    except FileNotFoundError:
        return

load_task_from_file()

while user_choice != 6:

    print("""
    1. Pokaż zadania.
    2. Dodaj zadanie.
    3. Usuń zadanie.
    4. Modyfikuj zadanie.
    5. Zapisz zmiany do pliku.
    6. Zakończ aplikację.
    """)

    user_choice = int(input("Podaj liczbę z dostępnych opcji: "))

    if user_choice == 1:
        show_tasks()
        print("\n")
    elif user_choice == 2:
        add_task()
    elif user_choice == 3:
        delete_task()
    elif user_choice == 4:
        modify_task()
    elif user_choice == 5:
        save_to_file()