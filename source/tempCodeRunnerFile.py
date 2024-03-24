class AddTeamPopUp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.title("Add Team")
        self.geometry("500x500")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=0)

        # Team Name
        self.team_name = customtkinter.CTkEntry(self, placeholder_text="Team Name")
        self.team_name.grid(row=0, column=0, padx=(20,20), pady=(20,20))

        # Team Character
        self.character_var = customtkinter.StringVar(value="Character")
        self.character = customtkinter.CTkComboBox(self, values=["Goblin", "Chicken", "Cow"], variable=self.character_var, justify="center", state="readonly")
        self.character.grid(row=1, column=0, padx=(20,20), pady=(20,20))

        # Add Player
        self.player = customtkinter.CTkEntry(self, placeholder_text="Player Name")
        self.player.grid(row=2, column=0, padx=(20,20), pady=(20,20))

        # Player List
        self.player_list = customtkinter.CTkTextbox(self)
        self.player_list.grid(row=0, column=1, rowspan=3, padx=(20,20), pady=(20,20), sticky="snew")