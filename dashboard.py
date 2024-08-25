from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

from utils import get_prisoner_count_by_status

Builder.load_file("dashboard.kv")


class DashboardScreen(MDScreen):
    def __init__(self, **kwargs):
        super(DashboardScreen, self).__init__(**kwargs)
        self.load_dashboard_data()

    def on_pre_enter(self):
        self.load_dashboard_data()

    def load_dashboard_data(self):
        total_prisoners = get_prisoner_count_by_status()
        incarcerated_count = total_prisoners.get("Incarcerated", 0)
        released_count = total_prisoners.get("Released", 0)
        transferred_count = total_prisoners.get("Transferred", 0)
        print(total_prisoners)
        # Update the dashboard with fetched data
        # self.ids.total_prisoners.text = str(sum(total_prisoners.values()))
        # self.ids.incarcerated_count.text = str(incarcerated_count)
        # self.ids.released_count.text = str(released_count)
        # self.ids.transferred_count.text = str(transferred_count)

