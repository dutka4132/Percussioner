from kivy.uix.screenmanager import Screen
from kivy.config import Config # для работы с размерами окна

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button

from graphic import *
from btn_settings import Setting
import information
from mistake_words import mistakes

# Работа с окнома
screen = (400, 700)
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', screen[0])
Config.set('graphics', 'height', screen[1])


#class CheckMistakes(AnchorLayout):
#    def __init__(self, pos, func, **kwargs):
#        super(CheckMistakes, self).__init__(**kwargs)
#
#        self.pos = pos
#        self.func = func
#        self.button = Button(font_size=20,
#                             on_press=self.func,
#                             pos=self.pos,
#                             size_hint=(.7, .12),  # указвает размер процентно кнопки по отношению к FloatLayout
#                             background_normal='picture/acetone-2025315-173252-818.png',
#                             )
#        self.lb = Label(text='Ваши ошибки', font_size=23, pos=(28, 660), color=(0, 0, 0, 1), bold=True)
#        self.cross = Image(source='picture/green_cross.png', allow_stretch=True, keep_ratio=True, pos=(153, 680),
#                         size=(58, 58))

#        self.button.add_widget(self.cross)
#        self.button.add_widget(self.lb)
#        self.add_widget(self.button)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.widget_space = FloatLayout()

        self.value = 0
        self.bl = BoxLayout(orientation='vertical', padding=50, spacing=-100)
        self.inst = information.Info(self.bl)
        #self.check_mistakes = CheckMistakes((-150, 270), self.mstk_screen)
        self.painter_widget = PainterWidget()
        self.settings = Setting(self.painter_widget)
        self.settings.pos = (-230, 380)

        self.widget_space.add_widget(self.painter_widget)
        self.widget_space.add_widget(self.inst.screen())
        self.widget_space.add_widget(self.settings)

        self.add_widget(self.widget_space)

    #def mstk_screen(self, *args):
    #    print(mistakes)
    #    self.value = 1
    #    self.manager.current = 'mstk_screen'