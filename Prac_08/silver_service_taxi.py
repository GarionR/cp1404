from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Txi that scales price_per_km by fanciness."""
    flagfall = 4.50

    def __init__(self, name="", fuel=0, fanciness=1):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Return a string like a Taxi but with flag_fall."""
        return "{} plus flagfall of ${}".format(super().__str__(), self.flagfall)
