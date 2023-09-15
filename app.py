
from player import Player
from api import GPT
import json
import prompts
import colorama
from utils import type_print

from colorama import Fore,Style,Back

from simple_term_menu import TerminalMenu

# COLORS for terminal
RED = "\x1b[1;31;40m"
BLUE = "\x1b[1;34;40m"
GREEN = "\x1b[1;32;40m"
YELLOW = "\x1b[1;33;40m"
CYAN = "\x1b[1;36;40m"
MAGENTA = "\x1b[1;35;40m"
RESET = "\x1b[0m"

# AIQuest codewords
AVAILABLE_COMAMNDS = ["ITEMS", "HEALTH", "USE ITEM", "QUIT", "HELP"]

MAX_TRIES = 6

class AIQuest:
    def __init__(self):
        self.player = Player()
        self.gpt = GPT()
        self.gpt.add_system_message(prompts.STARTING_PROMPTS[0])

        colorama.init()

    def read_user_input(self):
        user_input = input(f"{Fore.BLUE}What do you do? {RESET}").strip().upper()
        if user_input == "ITEMS":
            print(self.player.available_items)
        elif user_input == "HEALTH":
            health_color = Fore.GREEN if self.player.player_health > 50 else Fore.RED
            print(f"{health_color} {self.player.player_health}")
        elif user_input == "USE ITEM": # This defines when we used the item
            terminal_menu = TerminalMenu(self.player.get_items())
            menu_entry_index = terminal_menu.show()
            self.gpt.add_user_message(f"I used {self.player.available_items[menu_entry_index]}")
            self.player.remove_item(self.player.available_items[menu_entry_index])
            self.query_gpt()
        elif user_input == "QUIT":
            quit()
        elif user_input == "HELP":
            print(f"{Fore.YELLOW} The available commands are: {AVAILABLE_COMAMNDS}")
        else:
            self.gpt.add_user_message(user_input)
            self.query_gpt()

    def game_loop(self):
        self.player = Player()
        self.query_gpt()

        # Start the game loop
        while self.player.isAlive():
            # At every step we want to pass in the 
            # query for user input via terminal
            self.read_user_input()

    # Add a typewriter effect for printing
    
            
    def query_gpt(self):
        response = self.gpt.query_api()
        i = 0
        while i < 5:
            try:
                json_response = json.loads(response)
                break
            except json.decoder.JSONDecodeError:
                response = self.gpt.query_api()
                i += 1
        
        type_print(Fore.GREEN + json_response["message"] + Fore.RESET)
        if "playerHealthLost" in json_response and int(json_response["playerHealthLost"]) > 0:
            self.player.subtractHealth(json_response["playerHealthLost"])
            print(f"{Fore.RED}You lost health! Your health is now " + str(self.player.player_health))
        if "itemGained" in json_response and not (json_response["itemGained"] == "" or str(json_response["itemGained"]) == str(None)):
            self.player.add_item(json_response["itemGained"])
            print(f"{Fore.YELLOW}You gained an item! Your items are now " + str(self.player.available_items))

if __name__ == "__main__":
    game = AIQuest()
    game.game_loop()