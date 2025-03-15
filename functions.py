from kivy.animation import Animation
from random import choice, randint

anim = Animation(color=(0, 0, 0, 1), duration=.2) + Animation(color=(1, 0, 0, 1), duration=.2) + Animation(color=(0, 0, 0, 1), duration=.2) + Animation(color=(1, 0, 0, 1), duration=.2) + Animation(color=(0, 0, 0, 1), duration=.2) + Animation(color=(1, 0, 0, 1), duration=.2) + Animation(color=(0, 0, 0, 1), duration=.2) + Animation(color=(1, 0, 0, 1), duration=.2)

# Создаёт рандомную конбинацию слов
def words_combination(tpl):
    combination = []
    for i in range(5):
        word = choice(tpl)
        if word in combination:
            while word in combination:
                word = choice(tpl)
        combination.append(word)

    return combination

# Обработка неправильного ответа
def error(lbl, anim):
    anim.start(lbl)
    return lbl

# Изменение ударение в словах
def random_stress(word):
    vowels = 'аеёиоуыэюя'
    for letter in word:
        if letter in vowels and randint(0, 3) == 2:
            return word[:word.find(letter)].lower() + letter.upper() + word[word.find(letter) + 1:].lower()
    return word

# Логика проверки ответов
def check_answers(var, lbl, arr, ind):
    if (var.active and lbl.text == arr[ind]) or (var.active == False and lbl.text != arr[ind]):
        return 1
    elif var.active == False and lbl.text == arr[ind]:
        return 2
    elif var.active == True and lbl.text != arr[ind]:
        return 3

# Сама проверка всех ответов пользователя
def res(c_b, l, ar):
    for counter in range(1, 6):
        if check_answers(c_b[f'check{counter}'], l[f'lbl{counter}'], ar, counter - 1) == 0:
            error(l[f'lbl{counter}'], anim)
            c_b[f'check{counter}'].active = False
        elif check_answers(c_b[f'check{counter}'], l[f'lbl{counter}'], ar, counter - 1) == 2:
            error(l[f'lbl{counter}'], anim)
            c_b[f'check{counter}'].active = True
        elif check_answers(c_b[f'check{counter}'], l[f'lbl{counter}'], ar, counter - 1) == 3:
            error(l[f'lbl{counter}'], anim)
            c_b[f'check{counter}'].active = False