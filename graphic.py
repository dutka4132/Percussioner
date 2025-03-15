from kivy.graphics import Color, Rectangle, RoundedRectangle
from kivy.uix.widget import Widget

class PainterWidget(Widget):
    def __init__(self, **kwargs):
        super(PainterWidget, self).__init__(**kwargs)

        self.clr_rect1 = (0.19, .84, .6, 1)
        self.clr_rect2 = (1, .8, 0, 1)
        self.clr_rect3 = (1, 1, 1, 1)
        with self.canvas:
            Color(*self.clr_rect1)
            self.rect1 = Rectangle(pos=(0,0), # позиция
                    size=(1000, 1000) # указывает высоту и ширину элипса
                    )

            Color(*self.clr_rect2)
            self.rect2 = RoundedRectangle(pos=(50, 175), # позиция
                    size=(400, 600), # указывает высоту и ширину элипса
                    radius = [(40, 40), (40, 40), (40, 40), (40, 40)]
                    )

            Color(*self.clr_rect3)
            self.rect2 = RoundedRectangle(pos=(56, 435),  # позиция
                                          size=(387, 215),  # указывает высоту и ширину элипса
                                          radius=[(40, 40), (40, 40), (40, 40), (40, 40)]
                                          )