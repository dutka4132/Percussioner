from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout

mistakes = []
'''Добавление слов на экран'''
class MistakeWords(AnchorLayout):
    def __init__(self, bl,  **kwargs):
        super(MistakeWords, self).__init__(**kwargs)
        self.bl = bl

        for word in mistakes:
            self.bl.add_widget(Label(text=f'{word}', color=(1, 1, 1, 1)))

    def screen_mistakes(self):
        return self.bl


