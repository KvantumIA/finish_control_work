from datetime import datetime


class Count:
    def __init__(self):
        self.count = 0

    def add_count(self):
        self.count += 1
        self.save_count()

    def save_count(self):
        try:
            with open("count.txt", "w", encoding="utf-8") as file:
                # Запись значения переменной в файл
                file.write(f"Значение Count {datetime.today()} = {self.count}")
        except Exception as e:
            print("Произошла ошибка: ", e)
