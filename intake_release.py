from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen

Builder.load_file("intake_release.kv")

class IntakeReleaseScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class IntakeReleaseApp(MDApp):

    def build(self):
        return IntakeReleaseScreen()


if __name__ == '__main__':
    IntakeReleaseApp().run()
