from dragon import Dragon

class IceDragon(Dragon):

    def __init__(self, name, image):
        self.name = name
        self.image = image


    # sets IceDragon class as not being able to breathe fire
    @staticmethod
    def can_breathe_fire():
        return False
