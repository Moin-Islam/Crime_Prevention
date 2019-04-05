from kivy.app import App
from kivy.logger import Logger
from database import select_all_tasks
#kivy.require("1.10.1")
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen

from kivy.lang import Builder
from kivy.uix.actionbar import ActionBar
from kivy.base import runTouchApp
from kivy.lang import Builder
class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    pass
class MyScreenManager(ScreenManager):
    pass

class mainscreen(App):
    def build(self):
        return MyScreenManager()

if __name__ == "__main__":
    mainscreen().run()