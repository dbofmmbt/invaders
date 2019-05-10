from invaders.screens.menu import Menu
from PPlay.window import Window
import invaders.settings as settings


window = Window(800, 600)
keyboard = window.get_keyboard()

settings.current_container = Menu(window)
settings.difficulty = 1
settings.backgroundColor = (33, 33, 33)
settings.game_speed = 3

while True:
    settings.delta_time = window.delta_time()
    settings.current_container.render()
    window.update()
