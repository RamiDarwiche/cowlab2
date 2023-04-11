from dragon import Dragon

class IceDragon(Dragon):

    def __init__(self, name, image):
        self.name = name
        self.image = image

    def can_breate_fire(self):
        return False
