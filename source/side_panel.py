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

        # Players
        self.player_list = None
        self.player_list_width = (SIDE_PANEL_WIDTH // 3)
        self.player_list_height = 300 # Update this once all widgets are added

        # Current Tile
        self.current_tile = None
        self.current_tile_width = int(TILE_WIDTH * 1.5)
        self.current_tile_height = int(TILE_HEIGHT * 1.5)

        # Dice Box
        self.dice_box = None
        self.dice_box_width = SIDE_PANEL_WIDTH - (self.margin * 2)
        self.dice_box_height = 150 # Update this once all widgets are added

        # Add Team
        self.add_team = None
        self.add_team_width = int(SIDE_PANEL_WIDTH // 2.5)
        self.add_team_height = int(self.add_team_width // 2)

        # Edit Team
        self.edit_team = None
        self.edit_team_width = self.add_team_width
        self.edit_team_height = self.add_team_height
        
        # Sprite list for all the SidePanel sprites
        self.side_panel_sprite_list = arcade.SpriteList()
        
    def setup(self):
        
        # Creat the sprites
        self.team_image = arcade.SpriteSolidColor(self.team_image_width, self.team_image_height, arcade.color.WHITE)
        self.team_name = arcade.SpriteSolidColor(self.team_name_width, self.team_name_hight, arcade.color.GRAY)
        self.player_list = arcade.SpriteSolidColor(self.player_list_width, self.player_list_height, arcade.color.WHITE)
        self.current_tile = arcade.SpriteSolidColor(self.current_tile_width, self.current_tile_height, arcade.color.WHITE)
        self.dice_box = arcade.SpriteSolidColor(self.dice_box_width, self.dice_box_height, arcade.color.WHITE)
        self.add_team = arcade.SpriteSolidColor(self.add_team_width, self.add_team_height, arcade.color.WHITE)
        self.edit_team = arcade.SpriteSolidColor(self.edit_team_width, self.edit_team_height, arcade.color.WHITE)

        # Team image center x, y
        self.team_image.center_x = self.left + (SIDE_PANEL_WIDTH // 2)
        self.team_image.center_y = self.top - self.margin - (self.team_image_height // 2)

        # Add team image to SpriteList
        self.side_panel_sprite_list.append(self.team_image)

        # Team name center x, y
        self.team_name.center_x = self.left + (SIDE_PANEL_WIDTH // 2)
        self.team_name.center_y = self.top - self.margin - self.team_image_height - (self.team_name_hight // 2)

        # Add team name to SpriteList
        self.side_panel_sprite_list.append(self.team_name)

        # Team players center x, y
        self.player_list.center_x = self.left + self.margin + (self.player_list_width // 2)
        self.player_list.center_y = self.top - (self.margin * 2) - (self.team_image_height + self.team_name_hight) - (self.player_list_height // 2)

        # Add team players to sprite list
        self.side_panel_sprite_list.append(self.player_list)

        # Current tile center x, y
        self.current_tile.center_x = (self.player_list.right + self.right) // 2
        self.current_tile.center_y = self.player_list.center_y

        # Add current tile to sprite list
        self.side_panel_sprite_list.append(self.current_tile)

        # Dice box center x, y
        self.dice_box.center_x = self.left + (SIDE_PANEL_WIDTH // 2)
        self.dice_box.center_y = self.player_list.bottom - self.margin - (self.dice_box_height // 2)

        # Add dice box to sprite list
        self.side_panel_sprite_list.append(self.dice_box)

        # Add team center x, y
        self.add_team.center_x = (self.left * (3/4)) + (self.right * (1/4))
        self.add_team.center_y = (self.dice_box.bottom + self.bottom) // 2

        # Add team to sprite list
        self.side_panel_sprite_list.append(self.add_team)

        # Edit team center x, y
        self.edit_team.center_x = (self.left * (1/4)) + (self.right * (3/4))
        self.edit_team.center_y = self.add_team.center_y

        # Add edit team to sprite list
        self.side_panel_sprite_list.append(self.edit_team)

    def on_draw(self):
        self.side_panel_sprite_list.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
       
        # Print for debugging
        print(f"Coordiantes: {x - self.left, y - self.bottom}.")
        print(self.player_list.bottom)
        print(self.add_team.top)
        print(self.dice_box.center_y)
              
