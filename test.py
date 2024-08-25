from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from utils import get_all_prisoners, get_prisoner_count_by_status, get_total_prisoners

Builder.load_file("test.kv")


class TestScreen(MDScreen):
    def on_pre_enter(self):
        self.load_dashboard_data()
    def __init__(self):
        super(TestScreen, self).__init__()
        self.load_dashboard_data()

    def load_dashboard_data(self):
        total_prisoners = get_prisoner_count_by_status()
        incarcerated_count = total_prisoners.get("Incarcerated", 0)
        released_count = total_prisoners.get("Released", 0)
        transferred_count = total_prisoners.get("Transferred", 0)
        print(total_prisoners)
        # Update the dashboard with fetched data
        self.ids.total_prisoners.text = str(sum(total_prisoners.values()))
        self.ids.incarcerated_count.text = str(incarcerated_count)
        self.ids.released_count.text = str(released_count)
        self.ids.transferred_count.text = str(transferred_count)


class DashboardApp(MDApp):
    def build(self):
        return TestScreen()


if __name__ == '__main__':
    DashboardApp().run()
