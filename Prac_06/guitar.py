class Guitar:

    CURRENT_YEAR = 2020
    VINTAGE_THRESHOLD = 50

    def __init__(self, name="", year=0, cost=0):
        """

        name: str
        year: int
        cost: float
        """

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """default string return"""
        return "{} ({}) : ${:,}".format(self.name, self.year, self.cost)

    def get_age(self):
        """returns age of guitar"""
        return Guitar.CURRENT_YEAR - self.year

    def is_vintage(self):
        """determines if guitar is vintage"""
        return self.get_age() > Guitar.VINTAGE_THRESHOLD
