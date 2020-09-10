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
        """Determine if language is dynamic"""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Default string return"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)
