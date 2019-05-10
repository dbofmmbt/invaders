from PPlay.sprite import Sprite
import invaders.settings as settings


class Shot(Sprite):
    def __init__(self):
        imageUrl = "images/game/shot.png"
        super().__init__(imageUrl)
        self.speed = 150 * settings.game_speed

    def render(self):
        self.updateLogic()
        self.draw()

    def updateLogic(self):
        self.move_y(-self.speed * settings.delta_time)
