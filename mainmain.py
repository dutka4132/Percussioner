import kivy
kivy.require("1.9.1")
from kivy.app import App # для создания окна
from kivy.config import Config # для работы с размерами окна

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

from graphic import *
from dark_theme import *
import information

# Работа с окнома
screen = (400, 700)
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', screen[0])
Config.set('graphics', 'height', screen[1])

widget_space = FloatLayout()
bl = BoxLayout(orientation='vertical', padding=50, spacing=-100)
inst = information.Info(bl)
#btn_change_theme = ChangeTheme(inst)
#btn_change_theme.pos = (-230, 380)


class MyApp(App):
    # создние кнопки
    def build(self):
        widget_space.add_widget(PainterWidget())
        #widget_space.add_widget(btn_change_theme)
        widget_space.add_widget(inst.screen())

        return widget_space


if __name__ == '__main__':
    MyApp().run()