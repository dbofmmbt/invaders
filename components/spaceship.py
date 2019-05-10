from PPlay.sprite import Sprite
import invaders.settings as settings
from invaders.components.shot import Shot


class Spaceship(Sprite):
    def __init__(self, window, imageUrl):
        super().__init__(imageUrl)
        self.set_position(window.width/2 - self.width/2, window.height * 0.8)
        self.window = window
        self.keyboard = window.get_keyboard()
        self.speed = 100 * settings.game_speed
        self.totalReloadTime = 0.2 * settings.difficulty
        self.currentReloadTime = 0
        self.shots = []

    def render(self):
        self.updateLogic()
        for shot in self.shots:
            shot.render()
            if shot.y + shot.height <= 0:
                self.shots.remove(shot)
        self.draw()

    def updateLogic(self):
        self.currentReloadTime -= settings.delta_time
        self.checkMovement()
        self.mustBeInDisplay()
        if self.keyboard.key_pressed("SPACE") and self.currentReloadTime <= 0:
            self.shoot()

    def checkMovement(self):
        if self.keyboard.key_pressed("RIGHT"):
            self.move_x(self.speed * settings.delta_time)
        elif self.keyboard.key_pressed("LEFT"):
            self.move_x(-self.speed * settings.delta_time)

    def mustBeInDisplay(self):
        if self.x < 0:
            self.set_position(0, self.y)
        elif self.x+self.width > self.window.width:
            self.set_position(self.window.width-self.width, self.y)

    def shoot(self):
        shot = Shot()
        shot.set_position(self.x+self.width/2-shot.width/2, self.y-shot.height)
        self.shots.append(shot)
        self.currentReloadTime = self.totalReloadTime