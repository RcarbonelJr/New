import arcade
from team import Team

from const import *

class Board(arcade.Section):

    def __init__(self, left, bottom, width, height, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        # Tiled map
        self.tile_map = None

        # Scene for Tiled Map
        self.scene = None

        """ GRID """
        # 1D list of all sprites in the 2D sprite list
        self.grid_sprite_list = arcade.SpriteList()

        # 2D grid of sprites to mirror 2D grid of numbers
        self.grid_sprites = []

        self.tileOutline_black = "assets/Sprites/tileOutline_black.png"
        self.tileoutLine_white = "assets/Sprites/tileOutline_white.png"

        # List of sprites outlineing the grid to match the tiled map
        for row in range(ROW_COUNT):
            self.grid_sprites.append([])
            for column in range(COULMN_COUNT):
                x = column * TILE_WIDTH + (TILE_WIDTH // 2)
                y = row * TILE_HEIGHT + (TILE_HEIGHT // 2)
                sprite = arcade.Sprite(self.tileOutline_black,  TILE_SCALE, center_x = x, center_y = y)
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)

        """ TEAM """
        # Update to a array later so multiple teams can be added
        self.team = None

    def setup(self):
        
        # Tiled map information
        map_name = "assets/Tiled/board.tmx"
        self.tile_map = arcade.load_tilemap(map_name, scaling=TILE_SCALE)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

    def on_draw(self):

        # Draw the Tiled map
        self.scene.draw()

        # Draw the grid sprites
        self.grid_sprite_list.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        
        # Get mouse clicked tile number
        column = x // TILE_WIDTH
        row = y // TILE_HEIGHT

        # Print for debugging
        print(f"Coordiantes: {x, y}. Tile: {column, row}")

        # Make sure we are on the grid
        if row >= ROW_COUNT or column >= COULMN_COUNT:
            return

        # Flip sprites
        sprite = self.grid_sprites[row][column]
        if sprite.texture.name == arcade.load_texture(self.tileOutline_black).name:
            sprite.texture = arcade.load_texture(self.tileoutLine_white)
        else:
           sprite.texture = arcade.load_texture(self.tileOutline_black)            