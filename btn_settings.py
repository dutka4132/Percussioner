from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget

from kivy.graphics import Color, RoundedRectangle

from dark_theme import *
from app_music import Music


class Rctngl(Widget):
    def __init__(self, **kwargs):
        super(Rctngl, self).__init__(**kwargs)
        with self.canvas:
            Color(.5529, .5804, .5529, 1)
            self.menu = RoundedRectangle(pos=(0, 0), size=(325, 875), radius=[(0, 0), (40, 40), (40, 40), (0, 0)])


class Setting(AnchorLayout):
    def __init__(self,  inst, **kwargs):
        super(Setting, self).__init__(**kwargs)

        #self.btn_mstk = btn_mstk
        self.inst = inst
        self.button = Button(font_size=20,
            size_hint=(.3, .1),  # указвает размер процентно кнопки по отношению к FloatLayout
            pos=(120, 175),
            on_press=self.settings_screen,
            background_normal='picture/acetone-2025315-173252-818.png',
        )
        self.cogwheel = Image(source='picture/thumbnail.png', allow_stretch=True, keep_ratio=True, pos=(5, 795),
                         size=(45, 45))

        self.button.add_widget(self.cogwheel)
        self.add_widget(self.button)

    def settings_screen(self, instance):
        Music.press_button()
        self.fl = FloatLayout()
        self.btn_exit = Button(opacity=0, pos=(0, 0), size=(400, 875), on_press=self.press)
        self.menu = Rctngl()
        self.theme = ChangeTheme((-150, 350), self.inst)
        #self.mistake = self.btn_mstk

        self.fl.add_widget(self.btn_exit)
        self.fl.add_widget(self.menu)
        self.fl.add_widget(self.theme)
        #self.fl.add_widget(self.mistake)
        self.add_widget(self.fl)


    def press(self, instance):
        Music.press_button()
        self.fl.clear_widgets()



#class ExitSetting(Button):
#    def __init__(self, p, s, **kwargs):
#        super(Button, self).__init__(**kwargs)
#        self.p = p
#        self.s = s
#        self.btn_exit = Button(opacity=1, pos=self.p, size=self.s, on_press=self.press)
#
#    def press(self, instance):
#        inst = Setting()
#        inst.fl.clear_widgets()