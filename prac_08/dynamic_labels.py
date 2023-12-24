import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "David", "Emily"]  # List of names

    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        for name in self.names:
            label = Label(text=name)
            main_layout.add_widget(label)
        return main_layout

if __name__ == "__main__":
    DynamicLabelsApp().run()
