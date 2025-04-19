from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget

from functions import *
from btn_check_answer import *
from btn_change_card import *
from app_music import Music



class Info:
    def __init__(self, bl):
        super().__init__()
        # все слова для ЕГЭ
        self.words_tpl =  (
            "аэропОрты", "бАнты", "бОроду", "бухгАлтеров", "вероисповЕдание", "водопровОд",
    "газопровОд", "граждАнство", "дефИс", "дешевИзна", "диспансЕр", "договорЁнность",
    "докумЕнт", "досУг", "еретИк", "жалюзИ", "знАчимость", "Иксы", "каталОг", "квартАл",
    "киломЕтр", "кОнусов", "корЫсть", "крАны", "кремЕнь", "лЕкторов", "лОктя", "лыжнЯ",
    "мЕстностей", "намЕрение", "нарОст", "нЕдруг", "недУг", "некролОг", "нЕнависть",
    "нефтепровОд", "новостЕй", "нОгтя", "Отзыв", "отзЫв", "Отрочество", "партЕр",
    "портфЕль", "пОручни", "придАное", "призЫв", "свЁкла", "сирОты", "созЫв",
    "сосредотОчение", "срЕдства", "стАтуя", "столЯр", "тамОжня", "тОрты", "тУфля",
    "цемЕнт", "цЕнтнер", "цепОчка", "шАрфы", "шофЁр", "экспЕрт", "вернА", "знАчимый",
    "красИвее", "кУхонный", "ловкА", "мозаИчный", "оптОвый", "прозорлИвый", "слИвовый",
    "бралА", "бралАсь", "взялА", "взялАсь", "влилАсь", "ворвалАсь", "воспринЯть",
    "воссоздалА", "вручИт", "вручИть", "гналА", "гналАсь", "добралА", "добралАсь",
    "дождалАсь", "дозвонИтся", "дозИровать", "ждалА", "жилОсь", "закУпорить", "занЯть",
    "заперлА", "запломбировАть", "защемИт", "звал", "звонИ", "кАшлянуть", "клАла",
    "клЕить", "крАлась", "кровоточИть", "лгалА", "лилАс", "навралА", "наделИт",
    "надорвалАсь", "вАться", "назвалАсь", "накренИтся", "налилА", "нарвалА", "начАть",
    "нАчал", "началА", "нАчали", "обзвонИт", "обзвонИть", "облегчИть", "облегчИт",
    "облилАсь", "обнялАсь", "обогналА", "ободралА", "ободрИть", "ободрИт", "ободрИться",
    "ободрИтся", "обострИть", "одолжИть", "одолжИт", "озлОбить", "оклЕить", "окружИт",
    "опОшлить", "освЕдомиться", "освЕдоми", "отбылА", "отдалА", "откУпорить", "отозвалА",
    "отозвалАсь", "перезвонИт", "плодоносИть", "пломбировАть", "повторИ", "позвалА",
    "позвонИт", "позвонИть", "полилА", "положИть", "понЯть", "понялА", "послАла",
    "прибЫть", "прИбыл", "прибылА", "прИбыли", "принЯть", "прИнял", "принялА",
    "прИняли", "рвалА", "сверлИт", "снялА", "совралА", "создалА", "сорвалА",
    "сорИт", "убралА", "углубИть", "укрепИт", "чЕрпать", "щемИт", "щЁлкать",
    "довезЁнный", "зАгнутый", "зАнятый", "зАпертый", "заселЁнный", "аселенА",
    "кормЯщий", "кровоточАщий", "нажИвший", "налИвший", "нанЯвшийся", "начАвший",
    "нАчитый", "низведЁнный", "облегчЁнный", "ободрЁнный", "обострЁнный",
    "отключЁнный", "повторЁнный", "поделЁнный", "понЯвший", "прИнятый", "принятА",
    "приручЁнный", "прожИвший", "снятА", "сОгнутый", "углублЁнный", "Деепричастия",
    "закУпорив", "начАв", "начАвшись", "отдАв", "поднЯв", "понЯв", "прибЫв",
    "создАв", "Наречия", "вОвремя", "дОверху", "донЕльзя", "дОнизу", "дОсуха",
    "зАсветло", "зАтемно", "красИвее", "надОлго", "ненадОлго", "диспансЕр"
        )
        self.bl1 = bl

    def screen(self):
        self.check_boxes = {'check1': CheckBox(size_hint_x=.047, size_hint_y=.047, color=[0, 0, 0]),
                            'check2': CheckBox(size_hint_x=.047, size_hint_y=.047, color=[0, 0, 0]),
                            'check3': CheckBox(size_hint_x=.047, size_hint_y=.047, color=[0, 0, 0]),
                            'check4': CheckBox(size_hint_x=.047, size_hint_y=.047, color=[0, 0, 0]),
                            'check5': CheckBox(size_hint_x=.047, size_hint_y=.047, color=[0, 0, 0])
                            }
        self.array = words_combination(self.words_tpl)
        self.labels = {
            'lbl1': Label(text=f'{random_stress(self.array[0])}', font_size='22sp', size_hint=(1, 1), halign='left', color=(0, 0, 0, 1)),
            'lbl2': Label(text=f'{random_stress(self.array[1])}', font_size='22sp', size_hint=(1, 1), halign='left', color=(0, 0, 0, 1)),
            'lbl3': Label(text=f'{random_stress(self.array[2])}', font_size='22sp', size_hint=(1, 1), halign='left', color=(0, 0, 0, 1)),
            'lbl4': Label(text=f'{random_stress(self.array[3])}', font_size='22sp', size_hint=(1, 1), halign='left', color=(0, 0, 0, 1)),
            'lbl5': Label(text=f'{random_stress(self.array[4])}', font_size='22sp', size_hint=(1, 1), halign='left', color=(0, 0, 0, 1))
            }

        #self.btn_change_theme = ChangeTheme(func=self.next_option)
        #self.bl1.add_widget(self.btn_change_theme)

        self.counter_presses = 0
        self.check_answer = CheckAnswer(text='Проверить примеры', func=self.result)
        text = Label(text='Выберете слова, в которых\nверно расставлены ударения:', font_size='22sp', bold=True, halign='center', color=(0, 0, 0, 1), size_hint=(.7, .9))

        # добавления вводного текста
        a = AnchorLayout(anchor_x='center', anchor_y='top')
        a.add_widget(text)
        self.bl1.add_widget(a)
        self.bl1.add_widget(Widget(size_hint=(.5, .7)))

        # добавление слов
        gr = GridLayout(cols=2, rows=6, spacing=15, size_hint=(3, 1))
        a2 = AnchorLayout(anchor_x='left', anchor_y='top', size_hint=(1, .9))

        for counter in range(1, 6):
            self.labels[f'lbl{counter}'].bind(size=self.labels[f'lbl{counter}'].setter('text_size'))
            gr.add_widget(self.check_boxes[f'check{counter}'])
            gr.add_widget(self.labels[f'lbl{counter}'])

        a2.add_widget(gr)
        self.bl1.add_widget(a2)

        self.bl1.add_widget(Widget())

        self.gr_button = GridLayout(cols=1, rows=3, spacing=-50)
        # добавление кнопки с проверкой ответов
        a1 = AnchorLayout(anchor_x='center', anchor_y='center')
        a1.add_widget(self.check_answer)
        self.bl1.add_widget(a1)

        self.screen_button = ChangeCard(text='Следующие примеры', func=self.next_option)

        self.bl1.add_widget(self.gr_button)

        return self.bl1

    def result(self, instance):
        a2 = AnchorLayout(anchor_x='center', anchor_y='center')
        gr2 = GridLayout(cols=1, rows=2, spacing=15, size_hint=(.7, 1))
        self.counter_presses += 1

        Music.press_button()

        if self.counter_presses == 1:
            res(self.check_boxes, self.labels, self.array)
            gr2.add_widget(self.screen_button)
            a2.add_widget(gr2)
            self.gr_button.add_widget(a2)

    def next_option(self, instance):
        Music.press_button()
        self.bl1.clear_widgets()
        Info.screen(self)
