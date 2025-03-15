from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class ChangeCard(AnchorLayout):
    def __init__(self, text, func, **kwargs):
        super(ChangeCard, self).__init__(**kwargs)

        self.func = func
        self.button = Button(font_size=20,
            size_hint=(1.7, .35),  # указвает размер процентно кнопки по отношению к FloatLayout
            pos=(127.5, 175),
            on_press=self.func,
            background_normal='picture/btn2-change-card.png',
        )

        self.label = Label(text=text, color=(0, 0, 0, 1),
                           font_size='22sp',
                           bold=True,
                           halign='center',
                           pos=(200, 75))

        self.button.add_widget(self.label)
        self.add_widget(self.button)