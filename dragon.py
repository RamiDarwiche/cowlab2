from cow import Cow


class Dragon(Cow):

    def __init__(self, name, image):
        self.name = name
        self.image = image

    # sets Dragon class as being able to breathe fire
    @staticmethod
    def can_breathe_fire():
        return True
