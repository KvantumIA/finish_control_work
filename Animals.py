class Animals:
    def __init__(self, name, birthday, type, commands):
        self._name = name
        self._birthday = birthday
        self._type = type
        self._commands = commands

    @property
    def name(self):
        return self._name

    @property
    def birthday(self):
        return self._birthday

    @property
    def type(self):
        return self._type

    @property
    def commands(self):
        return self._commands

    # @property
    # def add_commands(self):
    #     commands = self.commands

