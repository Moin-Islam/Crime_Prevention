from kivy.app import App                                 #importing framework
from kivy.logger import Logger
from database import select_all_tasks                    #importing database
#kivy.require("1.10.1")
from kivy.uix.floatlayout import FloatLayout             #selecting which layout to use
from kivy.uix.screenmanager import ScreenManager,Screen  #for switching screen

from kivy.lang import Builder
from kivy.uix.actionbar import ActionBar                 #action bar on then top of screen
from kivy.base import runTouchApp
from kivy.lang import Builder
class FirstScreen(Screen):                               #first screen - mainmenu
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
