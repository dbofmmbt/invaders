from invaders.button import Button
import invaders.settings as settings


class Difficulty:
    def __init__(self, window):
        self.window = window
        self.window.set_title("Invaders Dificuldade")

        self.easy = Button(window, "images/difficultyContainer/easy.png")
        self.medium = Button(window, "images/difficultyContainer/medium.png")
        self.hard = Button(window, "images/difficultyContainer/hard.png")

        self.put_button_on_position(self.easy, 0.1)
        self.put_button_on_position(self.medium, 0.4)
        self.put_button_on_position(self.hard, 0.7)

    def put_button_on_position(self, button, heightPercentage):
        half_width = self.window.width / 2
        button.set_position(half_width - button.width/2, self.window.height * heightPercentage)

    def update(self):
        from invaders.screens.game import Game
        if self.easy.clicked():
            settings.difficulty = 1
        elif self.medium.clicked():
            settings.difficulty = 2
        elif self.hard.clicked():
            settings.difficulty = 3
        else:
            return
        # Se não cair no else, algum dos três botões foi clicado
        settings.current_container = Game(self.window)
        print(settings.difficulty)

    def render(self):
        self.window.set_background_color(settings.backgroundColor)
        self.easy.render()
        self.medium.render()
        self.hard.render()
