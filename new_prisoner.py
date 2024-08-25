from kivy.properties import StringProperty, ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.recycleview import MDRecycleView
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.uix.label import MDLabel

from utils import filter_prisoners_by_status, get_all_prisoners, search_prisoners

Builder.load_file("new_prisoner.kv")

class PrisonersRecycleView(MDRecycleView):
    def __init__(self, **kwargs):
        super(PrisonersRecycleView, self).__init__(**kwargs)

class NewPrisonerScreen(MDScreen):
    search_term = StringProperty("")
    prisoners_rv = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_pre_enter(self):
        self.load_table_data()

    def load_table_data(self, search_term=""):
        if search_term:
            prisoners = search_prisoners(search_term)
        else:
            prisoners = get_all_prisoners()

        table_data = []
        for prisoner in prisoners:
            table_data.extend([
                {"text": str(prisoner[0])},  # ID
                {"text": prisoner[1]},       # First Name
                {"text": prisoner[2]},       # Last Name
                {"text": prisoner[7]},       # Status
                {"text": str(prisoner[10])}  # Sentence
            ])

        self.set_prisoners_data(table_data)

    def set_prisoners_data(self, data):
        self.ids.prisoners_rv.data = data

    def filter_data(self, status):
        prisoners = filter_prisoners_by_status(status)
        table_data = []
        for prisoner in prisoners:
            table_data.extend([
                {"text": str(prisoner[0])},  # ID
                {"text": prisoner[1]},       # First Name
                {"text": prisoner[2]},       # Last Name
                {"text": prisoner[7]},       # Status
                {"text": str(prisoner[10])}  # Sentence
            ])
        self.set_prisoners_data(table_data)

    def on_start(self):
        # Initialize the filter menu
        pass

    def open_filter_menu(self, item):
        menu_items = [
            {"text": "Incarcerated", "on_release": lambda x="Incarcerated": self.filter_data(x)},
            {"text": "Released", "on_release": lambda x="Released": self.filter_data(x)},
            {"text": "Transferred", "on_release": lambda x="Transferred": self.filter_data(x)},
        ]
        MDDropdownMenu(caller=item, items=menu_items).open()

    def menu_callback(self, text_item):
        self.root.ids.drop_text.text = text_item


class NewPrisonerApp(MDApp):

    def build(self):
        return NewPrisonerScreen()


if __name__ == '__main__':
    NewPrisonerApp().run()
