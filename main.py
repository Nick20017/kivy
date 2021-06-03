from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button


class Container(BoxLayout):
    box_1_1 = ObjectProperty()
    box_1_2 = ObjectProperty()
    box_1_3 = ObjectProperty()

    box_2_1 = ObjectProperty()
    box_2_2 = ObjectProperty()
    box_2_3 = ObjectProperty()

    box_3_1 = ObjectProperty()
    box_3_2 = ObjectProperty()
    box_3_3 = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_player1 = True
        self.is_player2 = False

        self.is_finished = False
        self.winner = ""

    def select_box(self, box_index):
        if self.is_finished:
            return

        if box_index == '1_1':
            if self.box_1_1.text != '':
                return
            self.box_1_1.text = 'X' if self.is_player1 else 'O'
        elif box_index == '1_2':
            if self.box_1_2.text != '':
                return
            self.box_1_2.text = 'X' if self.is_player1 else 'O'
        elif box_index == '1_3':
            if self.box_1_3.text != '':
                return
            self.box_1_3.text = 'X' if self.is_player1 else 'O'
        elif box_index == '2_1':
            if self.box_2_1.text != '':
                return
            self.box_2_1.text = 'X' if self.is_player1 else 'O'
        elif box_index == '2_2':
            if self.box_2_2.text != '':
                return
            self.box_2_2.text = 'X' if self.is_player1 else 'O'
        elif box_index == '2_3':
            if self.box_2_3.text != '':
                return
            self.box_2_3.text = 'X' if self.is_player1 else 'O'
        elif box_index == '3_1':
            if self.box_3_1.text != '':
                return
            self.box_3_1.text = 'X' if self.is_player1 else 'O'
        elif box_index == '3_2':
            if self.box_3_2.text != '':
                return
            self.box_3_2.text = 'X' if self.is_player1 else 'O'
        elif box_index == '3_3':
            if self.box_3_3.text != '':
                return
            self.box_3_3.text = 'X' if self.is_player1 else 'O'

        self.is_player1 = not self.is_player1
        self.is_player2 = not self.is_player2

        self.check_win()

    def check_win(self):
        if self.box_1_1.text == 'X' and self.box_1_2.text == 'X' and self.box_1_3.text == 'X':
            self.is_finished = True
            self.winner = 'Player 1'
            print("Winner is " + self.winner)
        elif self.box_1_1.text == 'O' and self.box_1_2.text == 'O' and self.box_1_3.text == 'O':
            self.is_finished = True
            self.winner = 'Player 2'
            print("Winner is " + self.winner)
        elif self.box_2_1.text == 'X' and self.box_2_2.text == 'X' and self.box_2_3.text == 'X':
            self.is_finished = True
            self.winner = 'Player 1'
            print("Winner is " + self.winner)
        elif self.box_2_1.text == 'O' and self.box_2_2.text == 'O' and self.box_2_3.text == 'O':
            self.is_finished = True
            self.winner = 'Player 2'
            print("Winner is " + self.winner)
        elif self.box_3_1.text == 'X' and self.box_3_2.text == 'X' and self.box_3_3.text == 'X':
            self.is_finished = True
            self.winner = 'Player 1'
            print("Winner is " + self.winner)
        elif self.box_3_1.text == 'O' and self.box_3_2.text == 'O' and self.box_3_3.text == 'O':
            self.is_finished = True
            self.winner = 'Player 2'
            print("Winner is " + self.winner)
        elif self.box_1_1.text == 'X' and self.box_2_1.text == 'X' and self.box_3_1.text == 'X':
            self.is_finished = True
            self.winner = 'Player 1'
            print("Winner is " + self.winner)
        elif self.box_1_1.text == 'O' and self.box_2_1.text == 'O' and self.box_3_1.text == 'O':
            self.is_finished = True
            self.winner = 'Player 2'
            print("Winner is " + self.winner)
        elif self.box_1_2.text == 'X' and self.box_2_2.text == 'X' and self.box_3_2.text == 'X':
            self.is_finished = True
            self.winner = 'Player 1'
            print("Winner is " + self.winner)
        elif self.box_1_2.text == 'O' and self.box_2_2.text == 'O' and self.box_3_2.text == 'O':
            self.is_finished = True
            self.winner = 'Player 2'
            print("Winner is " + self.winner)
        elif self.box_1_3.text == 'X' and self.box_2_3.text == 'X' and self.box_3_3.text == 'X':
            self.is_finished = True
            self.winner = 'Player 1'
            print("Winner is " + self.winner)
        elif self.box_1_3.text == 'O' and self.box_2_3.text == 'O' and self.box_3_3.text == 'O':
            self.is_finished = True
            self.winner = 'Player 2'
            print("Winner is " + self.winner)
        elif self.box_1_1.text == 'X' and self.box_2_2.text == 'X' and self.box_3_3.text == 'X':
            self.is_finished = True
            self.winner = 'Player 1'
            print("Winner is " + self.winner)
        elif self.box_1_1.text == 'O' and self.box_2_2.text == 'O' and self.box_3_3.text == 'O':
            self.is_finished = True
            self.winner = 'Player 2'
            print("Winner is " + self.winner)
        elif self.box_1_3.text == 'X' and self.box_2_2.text == 'X' and self.box_3_1.text == 'X':
            self.is_finished = True
            self.winner = 'Player 1'
            print("Winner is " + self.winner)
        elif self.box_1_3.text == 'O' and self.box_2_2.text == 'O' and self.box_3_1.text == 'O':
            self.is_finished = True
            self.winner = 'Player 2'
            print("Winner is " + self.winner)
        elif self.box_1_1.text != '' and self.box_1_2.text != '' and self.box_1_3.text != '' \
                and self.box_2_1.text != '' and self.box_2_2.text != '' and self.box_2_3.text != '' \
                and self.box_3_1.text != '' and self.box_3_2.text != '' and self.box_3_3.text != '':
            self.is_finished = True
            self.winner = ''

        if not self.is_finished:
            return

        box = BoxLayout()
        box.padding = 15
        box.spacing = 10
        box.orientation = 'vertical'

        label = Label(text="Congratulations,\nWinner is " + self.winner if self.winner != '' else 'Draw')
        popup_close_button = Button(text="Start new game")
        popup_close_button.size_hint_y = 0.5
        popup_close_button.bind(on_press=self.close_end_popup)

        box.add_widget(label)
        box.add_widget(popup_close_button)

        self.popup = Popup(title='End of game', content=box, size_hint=(0.5, 0.5))

        self.popup.open()

    def close_end_popup(self, *args, **kwargs):
        self.is_finished = False
        self.winner = ''

        self.box_1_1.text = ''
        self.box_1_2.text = ''
        self.box_1_3.text = ''

        self.box_2_1.text = ''
        self.box_2_2.text = ''
        self.box_2_3.text = ''

        self.box_3_1.text = ''
        self.box_3_2.text = ''
        self.box_3_3.text = ''

        self.is_player1 = True
        self.is_player2 = False

        self.popup.dismiss()


class MainApp(App):
    def build(self):
        self.title = "Tic Tac Toe"

        return Container()


if __name__ == "__main__":
    MainApp().run()