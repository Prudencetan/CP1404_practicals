from kivy.app import App
from kivy.lang import Builder


class ConvertMilesKm(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, value, increment):
        result = value + increment
        self.root.ids.input_number.text = str(result)


ConvertMilesKm().run()
