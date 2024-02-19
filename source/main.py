import arcade

from const import *

from board import Board
from side_panel import SidePanel

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # Create the Board
        self.board = Board(0, 0, BOARD_WIDTH, BOARD_HEIGHT)

        # Create the side panel
        self.side_panel = SidePanel(BOARD_WIDTH, 0, SIDE_PANEL_WIDTH, SIDE_PANEL_HEIGHT)

        # Add sections to the view
        self.section_manager.add_section(self.board)
        self.section_manager.add_section(self.side_panel)

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here

        # Reset the board
        self.board.setup()
        self.side_panel.setup()

    def on_draw(self):

        arcade.start_render()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass


def main():

    # Create the Window
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create the view
    view = GameView()

    # Set up the game
    view.setup()

    window.show_view(view)

    arcade.run()

if __name__ == "__main__":
    main()