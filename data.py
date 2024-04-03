import sqlite3
from pathlib import Path
import re
from Pet.Cats import Cats
from Pet.Dogs import Dogs
from Pet.Hamsters import Hamsters
from Pack_animal.Horses import Horses
from Pack_animal.Camels import Camels
from Pack_animal.Neddys import Neddys
from Count import Count


class App:
    def __init__(self):
        self.connect = None
        self.cur = None
        self.name = None
        self.birthday = ''
        self.type = ''
        self.command = ''
        self.file_path_dir = Path() / "Documents" / "animals.db"
        self.animal = ''
        self.create_bd()
        self.count_all = Count()

    def create_animals(self):
        print("Введите кличку животного: ")
        self.name = input("Ввод: ")
        print()
        self.animal_birthday()
        print()
        print("Введите команды которые знает животное: ")
        self.command = input("Ввод: ")
        print()
        print("Выберите из списка класс животного: \n"
              "1. Кошка.\n"
              "2. Собака. \n"
              "3. Хомяк. \n"
              "4. Лошадь. \n"
              "5. Ослик. \n"
              "6. Верблюд.")
        num = int(input("Ввод: "))
        animal = ''
        if num == 1:
            animal = Cats(self.name, self.birthday, 'Cats', self.command)
        elif num == 2:
            animal = Dogs(self.name, self.birthday, 'Dogs', self.command)
        elif num == 3:
            animal = Hamsters(self.name, self.birthday, 'Hamsters', self.command)
        elif num == 4:
            animal = Horses(self.name, self.birthday, 'Horses', self.command)
        elif num == 5:
            animal = Neddys(self.name, self.birthday, 'Neddys', self.command)
        elif num == 6:
            animal = Camels(self.name, self.birthday, 'Camels', self.command)
        else:
            print("Вы ввели не верное значение. Повторите.")

        return animal

    def animal_birthday(self):
        print("Введите дату рождения (например, 2020.12.31): ")
        self.birthday = input("Ввод: ")
        if not self.validate_date(self.birthday):
            print()
            print("Некорректный формат даты. Повторите ввод.")
            print()
            self.animal_birthday()

    def save_animal(self, animal):
        try:
            self.cur.execute(f"""INSERT INTO animals (name, birthday, type, command)
                                    VALUES (?, ?, ?, ?)""",
                             (animal.name, animal.birthday, animal.type, animal.commands))

            self.connect.commit()
            self.count_all.add_count()
        except Exception as e:
            print("Произошла ошибка: ", e)

    def create_bd(self):
        self.connect = sqlite3.connect(self.file_path_dir)
        self.cur = self.connect.cursor()

        self.cur.execute("""CREATE TABLE IF NOT EXISTS animals (id INTEGER PRIMARY KEY, 
                            name TEXT NOT NULL,
                            birthday TEXT NOT NULL,
                            type TEXT NOT NULL,
                            command TEXT NOT NULL)""")

    def print_animals_all(self):
        self.cur.execute("SELECT * FROM animals")
        rows = self.cur.fetchall()
        print("№ | ID |  Name   |  Birthday  |  Type | Commands")
        count = 1
        for row in rows:
            print(count, " ", row)
            count += 1

    def print_animals_sort_birthday(self):
        print("Отсортировано по дате рождения животного:")
        self.cur.execute("SELECT * FROM animals ORDER BY birthday")
        rows = self.cur.fetchall()
        print("№ | ID |  Name   |  Birthday  |  Type | Commands")
        count = 1
        for row in rows:
            print(count, " ", row)
            count += 1

    def print_animals_sort_name(self):
        print("Отсортировано по имени животного:")
        self.cur.execute("SELECT * FROM animals ORDER BY name")
        rows = self.cur.fetchall()
        print("№ | ID |  Name   |  Birthday  |  Type | Commands")
        count = 1
        for row in rows:
            print(count, " ", row)
            count += 1

    def print_animals_sort_type(self):
        print("Отсортировано по типу животного:")
        self.cur.execute("SELECT * FROM animals ORDER BY type")
        rows = self.cur.fetchall()
        print("№ | ID |  Name   |  Birthday  |  Type | Commands")
        count = 1
        for row in rows:
            print(count, " ", row)
            count += 1

    def delete_animal(self):
        self.print_animals_all()
        try:
            index = int(input("Введите ID животного: "))
            if index:
                self.cur.execute("DELETE FROM animals WHERE id=?", (index,))
                self.connect.commit()
                print(f"Животное с ID {index} успешно удалено из базы данных.")
                self.print_animals_all()
        except Exception as e:
            print("Произошла ошибка при удалении животного:", e)

    def __del__(self):
        if self.connect:
            self.connect.close()

    def add_new_commands(self):
        self.print_animals_all()
        index = int(input("Введите ID животного: "))
        print()
        new_command = input("Введите новую команду: ")
        try:
            self.cur.execute("SELECT command FROM animals WHERE id=?", (index,))
            current_commands = self.cur.fetchone()[0]
            all_commands = current_commands + ', ' + new_command
            self.cur.execute("UPDATE animals SET command=? WHERE id=?", (all_commands, index))
            self.connect.commit()
            print(f"Новые команды успешно добавлены к животному с ID {index}.")
        except Exception as e:
            print("Произошла ошибка при добавлении команд:", e)

    @staticmethod
    def validate_date(date):
        pattern = r'^\d{4}\.\d{2}\.\d{2}$'
        if re.match(pattern, date):
            return True
        else:
            return False
