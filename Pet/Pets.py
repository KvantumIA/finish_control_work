from Animals import Animals


class Pets(Animals):
    def __init__(self, name, birthday, type, commands):
        super().__init__(name, birthday, type, commands)

