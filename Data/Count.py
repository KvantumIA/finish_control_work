from pathlib import Path


class Count:
    def __init__(self):
        self.count = 0
        self.file_path = Path("../Documents") / "count.txt"

    def read_count(self, path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
                text = content.split("=")
                self.count = int(text[1])
            return self.count
        except Exception as e:
            print("Произошла ошибка: ", e)

    def add_count(self):
        self.read_count(self.file_path)
        self.count += 1
        self.save_count(self.file_path)

    def save_count(self, path):
        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(f"Значение Count = {self.count}")
        except Exception as e:
            print("Произошла ошибка: ", e)


# c = Count()
# file_path = Path("../Documents") / "count.txt"
# print(c.read_count(file_path))
