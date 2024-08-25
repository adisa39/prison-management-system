from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivymd.uix.pickers import MDDockedDatePicker
from kivymd.uix.textfield import MDTextField
from create_db import create_database

Builder.load_file("inmate_management.kv")

class FormDateField(MDTextField):
    pass


class InmateManagerScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_date_picker(self, focus):
        if not focus:
            return

        date_dialog = MDDockedDatePicker()
        # You have to control the position of the date picker dialog yourself.
        date_dialog.pos = [
            self.ids.dob.center_x - date_dialog.width / 2,
            self.ids.dob.y - (date_dialog.height + dp(32)),
        ]
        date_dialog.open()


class InmateManagerApp(MDApp):

    def build(self):
        return InmateManagerScreen()

    def on_start(self):
        # Initialize the database
        create_database()


if __name__ == '__main__':
    InmateManagerApp().run()
