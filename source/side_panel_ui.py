import arcade
import arcade.gui

from const import *

class SidePanel(arcade.Section):

    def __init__(self, left, bottom, width, height, **kwargs):
        super().__init__(left, bottom, width, height, **kwargs)

        # The main margin used
        self.margin = 10

        # Offset the X coordinate so that it is in the center of the side panel instead of the window
        self.x_offset = BOARD_WIDTH // 2

        # Different widgets (top to bottom, left to right)

        # Team image
        self.team_image = None
        self.team_image_width = SIDE_PANEL_WIDTH - (self.margin * 2)
        self.team_image_height = 170

        # Team name
        self.team_name = None
        self.team_name_width = self.team_image_width
        self.team_name_height = self.team_image_height / 4

        # Players list
        self.lst_players = None
        self.lst_players_text = None
        self.lst_players_bg = None
        self.lst_players_width = SIDE_PANEL_WIDTH / 3
        self.lst_players_height = TILE_HEIGHT * 4
        
        # Current tile
        self.current_tile = None
        self.current_tile_width = TILE_WIDTH
        self.current_tile_height = TILE_HEIGHT
        self.current_tile_x_offset = ((self.right - (self.left + self.margin + self.lst_players_width)) / 2) - TILE_WIDTH

        # Dice Box
        self.dice_box = None
        self.dice_box_width = SIDE_PANEL_WIDTH - (self.margin * 2)
        self.dice_box_height = (TILE_HEIGHT * 2) + (self.margin * 2)

        # Dice
        self.dice_1 = None
        self.dice_2 = None
        self.dice_width = TILE_WIDTH
        self.dice_height = TILE_HEIGHT
        self.dice_texture = arcade.load_texture("assets/Sprites/SixSidedDie/1side_alt.png")

        # Roll dice button
        self.btn_dice_roll = None
        self.btn_dice_roll_width = SIDE_PANEL_WIDTH - (self.margin * 4)
        self.btn_dice_roll_height = self.btn_dice_roll_width / 6

        # Add Team
        self.btn_add_team = None
        self.btn_add_team_width = (SIDE_PANEL_WIDTH / 2) - (self.margin)
        self.btn_add_team_height = self.btn_add_team_width / 2
        
        # Edit Team
        self.btn_edit_team = None
        self.btn_edit_team_width = self.btn_add_team_width
        self.btn_edit_team_height = self.btn_add_team_height

        # Vertical box to hold other boxes
        self.v_box = arcade.gui.UIBoxLayout()

        # Horizontal box for buttons
        self.h_box_1 = arcade.gui.UIBoxLayout(vertical=False)

        # Horizontal box for Dice
        self.h_box_2 = arcade.gui.UIBoxLayout(vertical=False)

        # Vertical box for dice box
        self.v_box_2 = arcade.gui.UIBoxLayout()

        # Horizontal box for the team players current tile
        self.h_box_3 = arcade.gui.UIBoxLayout(vertical=False)

        # Vertical box for the team display
        self.v_box_3 = arcade.gui.UIBoxLayout()

    def setup(self):

        # UI Manager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        """ TEAM BUTTONS """
        # Create the buttons
        self.btn_add_team = arcade.gui.UIFlatButton(width=self.btn_add_team_width, height=self.btn_add_team_height, text="Add Team")
        self.btn_edit_team = arcade.gui.UIFlatButton(width=self.btn_edit_team_width, height=self.btn_edit_team_height, text="Edit Team")

        # Add the buttons
        self.h_box_1.add(self.btn_add_team.with_space_around(right=10))
        self.h_box_1.add(self.btn_edit_team)

        """ ROLL BUTTON """

        # Create the roll button
        self.btn_dice_roll = arcade.gui.UIFlatButton(width=self.btn_dice_roll_width, height=self.btn_dice_roll_height, text="Roll")

        """ DICE """

        # Create the dice
        self.dice_1 = arcade.gui.UITextureButton(width=self.dice_width, height=self.dice_height, texture=self.dice_texture)
        self.dice_2 = arcade.gui.UITextureButton(width=self.dice_width, height=self.dice_height, texture=self.dice_texture)

        # Add the dice
        self.h_box_2.add(self.dice_1.with_space_around(right=10))
        self.h_box_2.add(self.dice_2)

        """ PLAYER LIST """

        # Create the player list
        self.lst_players_bg = arcade.load_texture(":resources:gui_basic_assets/window/grey_panel.png")
        self.lst_players_text = arcade.gui.UITextArea(width=self.lst_players_width, height=self.lst_players_height, text="Names go here", text_color=(0,0,0,255)) # Update text
        self.lst_players = arcade.gui.UITexturePane(self.lst_players_text, self.lst_players_bg, (self.margin, self.margin, self.margin, self.margin))

        # Add the player list
        self.h_box_3.add(self.lst_players)

        """ CURRENT TILE """

        # Create the current tile box
        self.current_tile = arcade.gui.UISpriteWidget(width=self.current_tile_width, height=self.current_tile_height, sprite=arcade.SpriteSolidColor(TILE_WIDTH, TILE_HEIGHT, arcade.color.WHITE)) # Update sprite

        # Add the current tile
        self.h_box_3.add(self.current_tile.with_space_around(left=self.current_tile_x_offset))

        """ TEAM DISPLAY """

        # Create the team image
        self.team_image = arcade.gui.UISpriteWidget(width=self.team_image_width, height=self.team_image_height, sprite=arcade.SpriteSolidColor(self.team_image_width, self.team_image_height, color=arcade.color.WHITE)) # Update sprite

        # Add the team image
        self.v_box_3.add(self.team_image)

        # Create the team name display
        self.team_name = arcade.gui.UITextArea(width=self.team_name_width, height=self.team_name_height, text="Team name here")

        # Add the team name display
        self.v_box_3.add(self.team_name)

        """ UI BOXES """

        # Create the dice box
        self.v_box_2.add(self.h_box_2.with_space_around(bottom=self.margin))
        self.v_box_2.add(self.btn_dice_roll)

        # Add the boxes to the main vertical box
        self.v_box.add(self.v_box_3.with_space_around(bottom=self.margin))
        self.v_box.add(self.h_box_3.with_space_around(bottom=self.margin * 2))
        self.v_box.add(self.v_box_2.with_space_around(bottom=self.margin * 2))
        self.v_box.add(self.h_box_1)

        """ DICE BOX """
        
        # Create the dice box
        self.dice_box = arcade.SpriteSolidColor(self.dice_box_width, self.dice_box_height, arcade.color.BRASS)
        self.dice_box.center_x = self.left + (SIDE_PANEL_WIDTH // 2)

        # Add v_box to UIManager
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                align_x=self.x_offset,
                anchor_y="center_y",
                child=self.v_box
            )
        )

    def on_draw(self):

        # Background
        arcade.draw_lrtb_rectangle_filled(self.left, self.right, self.top, self.bottom, arcade.color.DARK_JUNGLE_GREEN)
        #arcade.draw_lrtb_rectangle_outline(self.left, self.right, self.top, self.bottom, arcade.color.YELLOW, 10)

        # Recalculate the center_y of the dice box
        self.dice_box.center_y = self.v_box_2.center_y

        # Draw the dice box
        self.dice_box.draw()

        # Draw the UI
        self.manager.draw()