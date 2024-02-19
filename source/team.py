import arcade

class Team(arcade.SpriteCircle):

    def __init__(self, radius, color):
        super().__init__(radius, color)

        self.tile_location = None
        self.team_name = None