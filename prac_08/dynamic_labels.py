from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # This is your data or model
        self.names = ["Alice", "Bob", "Charlie", "David", "Eve"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            # Create a label for each name
            temp_label = Label(text=name)
            # Add the label to the "main" layout
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()