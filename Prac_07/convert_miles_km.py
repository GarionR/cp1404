from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """MilesConverterApp is a Kivy App for converting miles to kilometres"""
    output_message = StringProperty()

    def build(self):
        """build the Kivy app from the kv file"""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, input_value):
        try:
            miles = int(input_value)
        except ValueError:
            miles = 0
        km = miles * MILES_TO_KM
        self.output_message = "{:.3f}".format(km)

    def handle_increment(self, input_value, increment):
        try:
            miles = int(input_value)
        except ValueError:
            miles = 0
        self.handle_calculate(miles + increment)
        self.root.ids.text_input.text = str(miles + increment)


MilesConverterApp().run()
