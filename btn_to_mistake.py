from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button

'''Созддание кнопки для переключения с главной сцены на сцену с ошибочными словами'''
class CheckMistakes(AnchorLayout):
    def __init__(self, pos, **kwargs):
        super(CheckMistakes, self).__init__(**kwargs)

        self.pos = pos
        self.button = Button(font_size=20,
                             on_press=self.mstk_screen,
                             pos=self.pos,
                             size_hint=(.7, .12),  # указвает размер процентно кнопки по отношению к FloatLayout
                             background_normal='picture/acetone-2025315-173252-818.png',
                             )
        self.lb = Label(text='Ваши ошибки', font_size=23, pos=(28, 660), color=(0, 0, 0, 1), bold=True)
        self.cross = Image(source='picture/green_cross.png', allow_stretch=True, keep_ratio=True, pos=(153, 680),
                         size=(58, 58))

        self.button.add_widget(self.cross)
        self.button.add_widget(self.lb)
        self.add_widget(self.button)

    def mstk_screen(self, instance):
        self.switch_to('mstk_screen')