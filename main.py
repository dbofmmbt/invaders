from invaders.screens.menu import Menu
from PPlay.window import Window
import invaders.settings as settings


window = Window(800, 600)
keyboard = window.get_keyboard()

settings.current_container = Menu(window)
settings.difficulty = 1
settings.backgroundColor = (33, 33, 33)

while True:
    settings.current_container.update()
    settings.current_container.render()
    window.update()
