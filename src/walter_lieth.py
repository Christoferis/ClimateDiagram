from matplotlib.scale import LinearScale
from matplotlib.transforms import Transform, IdentityTransform

#custom scale: inheriting from LinearScale because its easier

class walter_lieth(LinearScale):

    name = "walter_lieth"

    def __init__(self) -> None:
        super().__init__()

    def set_default_locators_and_formatters():
        super().set_default_locators_and_formatters()


    def get_transform(self):

        IdentityTransform





if __name__ == "__main__":
    pass