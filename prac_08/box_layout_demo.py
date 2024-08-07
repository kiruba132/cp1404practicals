from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """A Kivy app demonstrating a BoxLayout with greeting functionality."""
    def build(self):
        """Set the app title and load the layout from a .kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Greet the user based on the input name or prompt for a name."""
        print('test')
        user_name = self.root.ids.input_name.text.strip()
        if user_name != "":
            greeting_text = f"Hello, {user_name}!"
            self.root.ids.greeting_label.text = greeting_text
        else:
            self.root.ids.greeting_label.text = "Please enter your name."

    def clear_fields(self):
        """Clear the input field and reset the greeting label."""
        self.root.ids.input_name.text = ''
        self.root.ids.greeting_label.text = 'Enter your name'


if __name__ == "__main__":
    BoxLayoutDemo().run()
