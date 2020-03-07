import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, \
    QGridLayout, QLabel, QWidget,QPushButton, QStatusBar
from PyQt5.QtGui import QIcon
from poker_game import Game
from functools import partial

class PokerGameApp(QWidget):

    style = "border-radius:5px; border-width:2px; border-style:solid;" \
            "text-align:center;" \
            "font-size:24px;" \
            "background-color:#bbbbbb;" \
            "padding-top:10px; padding-bottom:10px;" \
            "qproperty-alignment: AlignCenter; max-height:30px;"

    cardBoxes = []
    buttons = []
    count = 0

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.initiate_game()
        self.set_grid()
        self.set_statusBar()
        self.set_cardBoxes()
        self.set_buttons()
        self.set_restartButton()

        self.setWindowTitle('project 4jangnim')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

    def initiate_game(self):
        self.game = Game()

    def set_grid(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

    def set_statusBar(self):
        self.statusBar = QStatusBar(self)
        # self.statusBar.show()

    def set_cardBoxes(self):
        for i,card in enumerate(self.game.cards):
            cardBox = QLabel(card.get('number'), self)
            cardStyle = self.style+ "border-color:"+card.get("color")+ ";"
            cardStyle += "color:" + card.get("color") + ";"
            cardBox.setStyleSheet(cardStyle)
        #     self.cardBoxes.append(cardBox)
        # for i, cardBox in enumerate(self.cardBoxes):
            self.grid.addWidget(cardBox, 0, i)

    def set_buttons(self):
        for i, card in enumerate(self.game.cards):
            button = QPushButton("교체", self)
            button.setCheckable(False)
            button.clicked.connect(partial(self.change_card, i))
        #     self.buttons.append(button)
        # for i, button in enumerate(self.buttons):
            self.grid.addWidget(button, 1, i)

    def set_restartButton(self):
        button = QPushButton("재시작", self)
        button.clicked.connect(self.restart)
        self.grid.addWidget(button, 2, 0)

    def change_card(self, i):
        result = self.game.change_card(i)
        # self.statusBar.showMessage(result.get('message'))
        # self.statusBar.show()
        self.reload_card(i)

    def reload_card(self, i):
        card = self.game.cards[i]

        cardBox = QLabel(card.get('number'), self)
        cardStyle = self.style + "border-color:" + card.get("color") + ";"
        cardStyle += "color:" + card.get("color") + ";"
        cardBox.setStyleSheet(cardStyle)
        self.grid.addWidget(cardBox, 0, i)

        button = QPushButton("교체", self)
        button.setCheckable(False)
        button.setEnabled(False)
        self.grid.addWidget(button, 1, i)

    def restart(self):
        self.game.init_game()
        self.set_cardBoxes()
        self.set_buttons()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = PokerGameApp()
   sys.exit(app.exec_())
