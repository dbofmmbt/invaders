from menu import Menu
from PPlay.window import Window
from PPlay.keyboard import Keyboard
import invaders.settings as settings


window = Window(800, 600)
keyboard = window.get_keyboard()
menu = Menu(window)

settings.current_container = menu
settings.exit_game = False
settings.difficulty = 1
settings.backgroundColor = (33, 33, 33)

while True:
    if settings.exit_game:
        break

    settings.current_container.update()
    settings.current_container.render()
    window.update()
