import random

class FontColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Game():
    colors = ['red', 'green', 'white']
    numbers = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    cards = []

    def __init__(self):
        cards = []
        i=1
        while i <= 5:
            color = random.choice(self.colors)
            number = random.choice(self.numbers)
            cards.append({
                'key':i, 'color':color, 'number':number, 'mutable':True
            })
            i+=1
        self.cards = cards
        self.see_cards()

    def see_cards(self):
        for card in self.cards:
            if card.get('color') == "red":
                font_color = FontColors.FAIL
            elif card.get('color') == "green":
                font_color = FontColors.OKGREEN
            else:
                font_color = ""
            text = font_color + card.get('number')+FontColors.ENDC

            if card.get('mutable'):
                text += "   (O)"
            else:
                text += "   (X)"
            print(text)

    def change_card(self, key):
        if key not in [1,2,3,4,5]:
            print('1~5 사이의 숫자를 넣어주세요.')
            return
        if not self.cards[key-1].get('mutable'):
            print("이미 바꾼 카드입니다.")
            return
        self.cards[key-1]['color'] = random.choice(self.colors)
        self.cards[key-1]['number'] = random.choice(self.numbers)
        self.cards[key-1]['mutable'] = False
        self.see_cards()





