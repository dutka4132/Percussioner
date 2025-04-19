from kivy.uix.screenmanager import Screen
from kivy.config import Config
from kivy.graphics import Color, Rectangle, RoundedRectangle

from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout

from mistake_words import *

# Работа с окнома
screen = (400, 700)
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', screen[0])
Config.set('graphics', 'height', screen[1])

class Background(Widget):
    def __init__(self, **kwargs):
        super(Background, self).__init__(**kwargs)

        self.clr_rect1 = (0.19, .84, .6, 1)
        with self.canvas:
            Color(*self.clr_rect1)
            self.rect1 = Rectangle(pos=(0, 0),  # позиция
                                   size=(1000, 1000)  # указывает высоту и ширину элипса
                               )

class BackToMainScreen(AnchorLayout):
    def __init__(self, pos, func, **kwargs):
        super(BackToMainScreen, self).__init__(**kwargs)

        self.pos = pos
        self.func = func
        self.button = Button(font_size=20,
                             on_press=self.func,
                             pos=self.pos,
                             size_hint=(.7, .12),  # указвает размер процентно кнопки по отношению к FloatLayout
                             background_normal='picture/acetone-2025315-173252-818.png',
                             )
        self.lb = Label(text='<- Вернуться назад', font_size=23, pos=(60, 740), color=(0, 0, 0, 1), bold=True)
        #self.cross = Image(source='picture/green_cross.png', allow_stretch=True, keep_ratio=True, pos=(153, 680),
        #                 size=(58, 58))

        #self.button.add_widget(self.cross)
        self.button.add_widget(self.lb)
        self.add_widget(self.button)

class MistakeScreen(Screen):
    def __init__(self, **kwargs):
        super(MistakeScreen, self).__init__(**kwargs)
        self.widget_space = FloatLayout()

        self.bl_inst = BoxLayout()
        self.inst = MistakeWords(self.bl_inst)
        self.inst.pos = (-100, 200)
        self.back_to_main_screen = BackToMainScreen((-130, 350), self.main_screen)

        self.widget_space.add_widget(Background())
        self.widget_space.add_widget(self.back_to_main_screen)
        self.widget_space.add_widget(self.inst.screen_mistakes())

        self.add_widget(self.widget_space)

    def main_screen(self, *args):
        self.manager.current = 'main_screen'