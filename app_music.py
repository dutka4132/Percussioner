from kivy.core.audio import SoundLoader

class Music:
    def __init__(self, **kwargs):
        super(Music, self).__init__(**kwargs)
        self.bg_music = None

    def background_music(self):
        self.bg_music = SoundLoader.load('music/промежуточный_бит_для_приложения_никитухе_.mp3')
        if self.bg_music:
            self.bg_music.volume = 0.1
            self.bg_music.loop = True
            self.bg_music.play()

    @staticmethod
    def press_button():
        click_sound = SoundLoader.load('music/negromkiy-korotkiy-klik.ogg')
        if click_sound:
            click_sound.volume = 0.1
            click_sound.play()