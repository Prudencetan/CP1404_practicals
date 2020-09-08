from kivy.app import App
from kivy.lang import Builder


class MyKivyApp(App):

    def build(self):
        self.root = Builder.load_file("my_layout.kv")
        self.title = "My first kivy title"
        return self.root


if __name__ == '__main__':
    my_kiv_app = MyKivyApp()
    my_kiv_app.run()
