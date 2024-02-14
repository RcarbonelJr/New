# Character class


# Team - What team the character is associated with (The team class houses information for which players are on the team)

import arcade

class Character(arcade.SpriteCircle):

    def __init__(self, radius, color):
        super().__init__(radius, color)

