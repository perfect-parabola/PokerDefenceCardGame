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
        self.init_game()

    def see_cards(self):
        for card in self.cards:
            # if card.get('color') == "red":
            #     font_color = FontColors.FAIL
            # elif card.get('color') == "green":
            #     font_color = FontColors.OKGREEN
            # else:
            #     font_color = ""
            # text = font_color + card.get('number')+FontColors.ENDC

            if card.get('color') == "red":
                font_color = "[R]"
            elif card.get('color') == "green":
                font_color = "[G]"
            else:
                font_color = "[W]"
            text = font_color + card.get('number')

            if card.get('mutable'):
                text += "   (O)"
            else:
                text += "   (X)"
            print(text)

    def init_game(self):
        cards = []
        i = 1
        while i <= 5:
            color = random.choice(self.colors)
            number = random.choice(self.numbers)
            cards.append({
                'key': i, 'color': color, 'number': number, 'mutable': True
            })
            i += 1
        self.cards = cards

    def change_card(self, key):
        if key not in [0,1,2,3,4]:
            message = '잘못된 변수 입력'
            print(message)
            return {
                'status':'failed',
                'message':message
            }
        if not self.cards[key].get('mutable'):
            message = "이미 바꾼 카드입니다."
            print(message)
            return {
                'status':'failed',
                'message':message
            }
        self.cards[key]['color'] = random.choice(self.colors)
        self.cards[key]['number'] = random.choice(self.numbers)
        self.cards[key]['mutable'] = False
        return {'status':'success', 'message':'카드 변경'}





