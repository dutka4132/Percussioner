import kivy
kivy.require("1.9.1")
from kivy.app import App # для создания окна
from app_music import Music

from kivy.uix.screenmanager import ScreenManager

from main_Screen import *

class MyApp(App):
    # создние кнопки
    def build(self):
        self.msc = Music()
        self.msc.background_music()
        self.sm = ScreenManager()
        scrn1 = MainScreen(name='main_screen')
        self.sm.add_widget(scrn1)

        return self.sm


if __name__ == '__main__':
    MyApp().run()