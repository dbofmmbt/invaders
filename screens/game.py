import invaders.settings as settings


class Game:
    def __init__(self, window):
        self.window = window
        self.window.set_title("INVAAAAAADERS!")
        self.keyboard = window.get_keyboard()

    def render(self):
        self.window.set_background_color(settings.backgroundColor)

    def update(self):
        if self.keyboard.key_pressed("ESC"):
            from invaders.screens.menu import Menu
            settings.current_container = Menu(self.window)
