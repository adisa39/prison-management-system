# pip install https://github.com/kivymd/KivyMD/archive/master.zip
from kivy.lang import Builder
from kivy.properties import ObjectProperty

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import MDScreenManager

from dashboard import DashboardScreen
from inmate_management import InmateManagerScreen
from intake_release import IntakeReleaseScreen
from new_prisoner import NewPrisonerScreen

class MyScreenManager(MDScreenManager):
    pass

class Home(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class PrisonApp(MDApp):
    sm = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = 'Prison Management System'

    def build(self):
        self.theme_cls.theme_style = "Light"
        Builder.load_file("PrisonApp.kv")
        return Home()

    def on_start(self):
        # Initialize the database
        pass

if __name__ == '__main__':
    PrisonApp().run()
