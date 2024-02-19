import arcade
import arcade.gui

from const import *

class SidePanel(arcade.Section):

    def __init__(self, left, bottom, width, height, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        # The main margin used
        self.margin = 4
        
        # Team image
        self.team_image = None
        self.team_image_width = SIDE_PANEL_WIDTH - (self.margin * 2)
        self.team_image_height = 250 # Update this once all widgets are added

        # Team name
        self.team_name = None
        self.team_name_width = SIDE_PANEL_WIDTH - (self.margin * 2)
        self.team_name_hight = 75 # Update this once all widgets are added

        # Sprite list for all the SidePanel sprites
        self.side_panel_sprite_list = arcade.SpriteList()
        

    def setup(self):
        
        # Team image Sprite
        self.team_image = arcade.SpriteSolidColor(self.team_image_width, self.team_image_height, arcade.color.WHITE)

        # Team image center x, y
        self.team_image.center_x = self.left + (SIDE_PANEL_WIDTH // 2)
        self.team_image.center_y = self.top - self.margin - (self.team_image_height // 2)

        # Add team image to SpriteList
        self.side_panel_sprite_list.append(self.team_image)

        # Team name Sprite
        self.team_name = arcade.SpriteSolidColor(self.team_name_width, self.team_name_hight, arcade.color.GRAY)

        # Team name center x, y
        self.team_name.center_x = self.left + (SIDE_PANEL_WIDTH // 2)
        self.team_name.center_y = self.top - self.margin - self.team_image_height - (self.team_name_hight // 2)

        # Add team name to SpriteList
        self.side_panel_sprite_list.append(self.team_name)

    def on_draw(self):
        self.side_panel_sprite_list.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
       
        # Print for debugging
        print(f"Coordiantes: {x - self.left, y - self.bottom}.")