from PPlay.sprite import Sprite


class Spaceship(Sprite):
    def __init__(self, window, imageUrl):
        super().__init__(imageUrl)
        self.set_position(window.width/2 - self.width/2, window.height * 0.8)
        self.window = window
        self.keyboard = window.get_keyboard()
        self.speed = 100 * window.delta_time()

    def render(self):
        self.updateLogic()
        self.draw()

    def updateLogic(self):
        self.checkMovement()
        self.mustBeInDisplay()

    def checkMovement(self):
        if self.keyboard.key_pressed("RIGHT"):
            self.move_x(self.speed)
        elif self.keyboard.key_pressed("LEFT"):
            self.move_x(-self.speed)

    def mustBeInDisplay(self):
        if self.x < 0:
            self.set_position(0, self.y)
        elif self.x+self.width > self.window.width:
            self.set_position(self.window.width-self.width, self.y)