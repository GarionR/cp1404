class ProgrammingLanguage:
    """Represent a programing language object"""

    def __init__(self, name, typing, reflection, year):
        """

        name: str
        typing: str
        reflection: bool
        year: int
        """

        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"
