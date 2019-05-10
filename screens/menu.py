from invaders.button import Button
import invaders.settings as settings
from time import sleep

class Menu:
    def __init__(self, window):
        self.window = window
        self.window.set_title("Invaders Menu")

        self.play = Button(window, "images/menu/play.png")
        self.difficulty = Button(window, "images/menu/difficulty.png")
        self.rank = Button(window, "images/menu/rank.png")
        self.quit = Button(window, "images/menu/quit.png")

        self.put_button_on_position(self.play, 0.13)
        self.put_button_on_position(self.difficulty, 0.33)
        self.put_button_on_position(self.rank, 0.53)
        self.put_button_on_position(self.quit, 0.73)

    def render(self):
        self.window.set_background_color(settings.backgroundColor)
        self.play.render()
        self.difficulty.render()
        self.rank.render()
        self.quit.render()

    def update(self):
        if self.play.clicked():
            from invaders.screens.game import Game
            settings.current_container = Game(self.window)
        elif self.difficulty.clicked():
            from invaders.screens.difficulty import Difficulty
            self.window.set_background_color(settings.backgroundColor)
            settings.current_container = Difficulty(self.window)
        elif self.rank.clicked():
            pass
        elif self.quit.clicked():
            self.window.close()
        else:
            return
        # Algum botão foi clicado para chegar até aqui.
        sleep(0.2)  # Para evitar que o usuário clique no botão da outra tela sem querer.

    def put_button_on_position(self, button, heightPercentage):
        half_width = self.window.width / 2
        button.set_position(half_width - button.width/2, self.window.height * heightPercentage)

