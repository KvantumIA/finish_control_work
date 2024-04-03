from Pet.Pets import Pets


class Hamsters(Pets):
    def __init__(self, name, birthday, type, commands):
        super().__init__(name, birthday, type, commands)
