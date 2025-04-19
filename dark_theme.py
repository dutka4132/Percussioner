from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button


class ChangeTheme(AnchorLayout):
    def __init__(self, pos, inst,  status=True, **kwargs):
        super(ChangeTheme, self).__init__(**kwargs)

        self.pos = pos
        self.inst = inst
        self.status = status
        self.button = Button(font_size=20,
                             pos=self.pos,
                             size_hint=(.7, .12),  # указвает размер процентно кнопки по отношению к FloatLayout
                             on_press=self.change,
                             background_normal='picture/acetone-2025315-173252-818.png',
                             )
        self.lb = Label(text='Светлая тема', font_size=23, pos=(28, 740), color=(0, 0, 0, 1), bold=True)
        self.sun = Image(source='picture/icons8-солнце-50.png', allow_stretch=True, keep_ratio=True, pos=(155, 762), size=(55, 55))

        self.button.add_widget(self.lb)
        self.button.add_widget(self.sun)
        self.add_widget(self.button)


    def change(self, instance):
        if self.status == True:
            self.status = False
            self.inst.clr_rect1 = (0, 0, 0, 1)
            self.inst.clr_rect2 = (.34, .36, 38)
            print(self.inst.clr_rect1)
            print(self.inst.clr_rect2)
            #self.inst.clr_rect3 = ()

