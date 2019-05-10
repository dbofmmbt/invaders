import invaders.settings as settings
from invaders.components.spaceship import Spaceship


class Game:
    def __init__(self, window):
        self.window = window
        self.window.set_title("INVAAAAAADERS!")
        self.keyboard = window.get_keyboard()

        self.ship = Spaceship(window, "images/game/spaceship.png")

    def render(self):
        self.updateLogic()
        self.window.set_background_color(settings.backgroundColor)
        self.ship.render()

    def updateLogic(self):
        if self.keyboard.key_pressed("ESC"):
            from invaders.screens.menu import Menu
            settings.current_container = Menu(self.window)
