from pygame import mixer

class Music:
    def __init__(self, **kwargs):
        super(Music, self).__init__(**kwargs)
        mixer.init()

    def background_music(self):
        mixer.music.load('music/промежуточный_бит_для_приложения_никитухе_.mp3')
        mixer.music.set_volume(0.1)
        mixer.music.play(-1)

    @staticmethod
    def press_button():
        sound = mixer.Sound('music/negromkiy-korotkiy-klik.ogg')
        sound.set_volume(0.1)
        sound.play()
