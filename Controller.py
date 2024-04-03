from data import App


class Start_app:
    def __init__(self):
        self.data = App()

    def start(self):
        print("Выберите пункт меню: \n"
              "1. Добавить животное. \n"
              "2. Вывести список животных в питомнике.\n"
              "3. Удалить животное.\n"
              "4. Добавить новую команду.\n"
              "9. Выход")
        num = int(input("Ввод: "))
        print()

        if num == 1:
            animal = self.data.create_animals()
            self.data.save_animal(animal)
            print("Животное успешно добавлено!")
            self.stop()
        elif num == 2:
            self.data.print_animals_all()
            print()
            self.sort_animal()
        elif num == 3:
            self.data.delete_animal()
            self.stop()
        elif num == 4:
            self.data.add_new_commands()
            self.stop()
        elif num == 9:
            self.stop()
        else:
            print("Вы неверно ввели пункт меню. Повторите ввод.")
            self.start()

    def stop(self):
        print()
        print("1. Назад в меню.\n"
              "2. Выход из программы.")
        num = int(input("Ввод: "))
        if num == 1:
            self.start()
        elif num == 2:
            self.data.__del__()
            SystemExit
        else:
            print("Вы неверно ввели пункт меню. Повторите ввод.")
            self.stop()

    def sort_animal(self):
        print("Желаете отсортировать?\n"
              "1. Да.\n"
              "2. Нет.")
        num = int(input("Ввод: "))
        if num == 1:
            print()
            print("Выберите тип сортировки: \n"
                  "1. По имени.\n"
                  "2. По дате рождения.\n"
                  "3. По типу животного.")
            num2 = int(input("Ввод: "))
            print()
            if num2 == 1:
                self.data.print_animals_sort_name()
                print()
                self.sort_animal()
            elif num2 == 2:
                self.data.print_animals_sort_birthday()
                print()
                self.sort_animal()
            elif num2 == 3:
                self.data.print_animals_sort_type()
                print()
                self.sort_animal()
            else:
                print("Вы неверно ввели пункт меню. Повторите ввод.")
                self.sort_animal()
        else:
            self.stop()
