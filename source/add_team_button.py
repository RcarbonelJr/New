import arcade
import arcade.gui
import customtkinter

from tkinter import messagebox

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class AddTeamButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("Add team clicked")
        pop_up = AddTeamPopUp()
        pop_up.mainloop()

class AddTeamPopUp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Add Team")
        self.geometry("500x500")
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure((0,1,2,3,4), weight=1)

        # Team Name
        self.team_name = customtkinter.CTkEntry(self, placeholder_text="Team Name")
        self.team_name.grid(row=0, column=0, padx=(20,20), pady=(20,20))

        # Team character
        self.character_var = customtkinter.StringVar(value="Character")
        self.character = customtkinter.CTkComboBox(self, values=["Goblin", "Chicken", "Cow"], variable=self.character_var, justify="center", state="readonly")
        self.character.grid(row=1, column=0, padx=(20,20), pady=(20,20))

        # Add player
        self.player = customtkinter.CTkEntry(self, placeholder_text="Player Name")
        self.player.grid(row=2, column=0, padx=(20,20), pady=(20,20))
        self.player.bind("<Return>", self.add_player_to_list)

        # Player list
        self.player_list = customtkinter.CTkTextbox(self, state="disabled", wrap="none")
        self.player_list.grid(row=0, column=1, rowspan=3, columnspan=2, padx=(20,20), pady=(20,20), sticky="snew")
        self.player_list.bind("<Button-1>", self.selected_player)

        # Remove player button
        self.remove_player = customtkinter.CTkButton(self, text="Remove", state="disabled",command=self.on_click_remove_player)
        self.remove_player.grid(row=3, column=1, columnspan=2, padx=(20,20), pady=(20,20), sticky="nsew")

        # Submit button
        self.submit = customtkinter.CTkButton(self, text="Submit", state="normal", command=self.on_click_submit)
        self.submit.grid(row=3, column=0, padx=(20,20), pady=(20,20))

    def add_player_to_list(self, event):
        player_name = self.player.get()
        if player_name:
            self.player_list.configure(state="normal")
            self.player_list.insert("end", f"{player_name}\n")
            self.player_list.configure(state="disabled")
            self.player.delete(0, "end")

    def selected_player(self, event):
        index = self.player_list.index(f"@{event.x},{event.y}")
        
        line_number = index.split(".")[0]
        start = f"{line_number}.0"
        end = self.player_list.index(f"{start} lineend")

        if start != end:
            # Remove current tag
            self.player_list.tag_remove("selected", "1.0", "end")

            # Add tag to clicked name and highlight
            self.player_list.tag_add("selected", start, end)
            self.player_list.tag_config("selected", background="blue")

            # Enable remove button
            self.remove_player.configure(state="normal")
        else:
            # Remove all tags
            self.player_list.tag_remove("selected", "1.0", "end")

            # disable remove button
            self.remove_player.configure(state="disabled")

    def on_click_remove_player(self):
        # Get the range of the selected player
        selected_range = self.player_list.tag_ranges("selected")

        if selected_range:
            start, end = selected_range

            # Remove the new line character to keep the list clean
            if self.player_list.get(end) == "\n":
                end_adjusted = self.player_list.index(f"{end}+1c")
            else:
                end_adjusted = end

            # Enable editing on the player_list
            self.player_list.configure(state="normal")

            # Delete the selected player
            self.player_list.delete(start, end_adjusted)

            # Disable editing on the player_list
            self.player_list.configure(state="disabled")

            # Disable remove button
            self.remove_player.configure(state="disabled")

    def on_click_submit(self):

        team_name = self.team_name.get()
        character = self.character.get()
        player_list = self.player_list.get("1.0", "end-1c")
        
        # Team name check
        if not team_name:
            messagebox.showinfo("Error", "Please enter a team name")

        # Character selection check
        elif character == "Character":
            messagebox.showinfo("Error", "Please select a team character")

        # Player check
        elif not player_list:
            messagebox.showinfo("Error", "Team must have at lease one player")

        else:
            print("Team submitted")
            self.destroy()
            

if __name__ == "__main__":
    print("Add team launched from main")
    pop_up = AddTeamPopUp()
    pop_up.mainloop()