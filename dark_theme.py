from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.image import Image
from kivy.uix.button import Button


class ChangeTheme(AnchorLayout):
    def __init__(self, inst, status=True, **kwargs):
        super(ChangeTheme, self).__init__(**kwargs)

        self.status = status
        self.inst = inst
        self.button = Button(font_size=20,
            size_hint=(.3, .1),  # указвает размер процентно кнопки по отношению к FloatLayout
            on_press=self.change,
            background_normal='picture/acetone-2025315-173252-818.png',
        )
        self.sun = Image(source='picture/icons8-солнце-50.png', allow_stretch=True, keep_ratio=True, pos=(5, 792), size=(51, 51))

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

