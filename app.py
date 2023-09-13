
from player import Player
from api import GPT
import json
import prompts

class AIQuest:
    def __init__(self):
        self.player = Player()
        self.gpt = GPT()
        self.gpt.add_system_message(prompts.STARTING_PROMPTS[0])

    def game_loop(self):
        self.player = Player()
        self.query_gpt()

        # Start the game loop
        while self.player.isAlive():
            # At every step we want to pass in the 
            # query for user input via terminal
            user_input = input("What do you do?\n")
            self.gpt.add_user_message(user_input)
            self.query_gpt()
            # response = self.gpt.query_api()

            # try:
            #     json_response = json.loads(response)
            #     print(json_response)
            #     if json_response["playerHealthLost"] > 0:
            #         self.player.subtractHealth(json_response["playerHealthLost"])
            #         print("You lost health! Your health is now " + str(self.player.player_health))
            # except:
                
            
    def query_gpt(self):
        response = self.gpt.query_api()
        try:
            json_response = json.loads(response)
            print(json_response["message"])
            if json_response["playerHealthLost"] > 0:
                self.player.subtractHealth(json_response["playerHealthLost"])
                print("You lost health! Your health is now " + str(self.player.player_health))
        except:
            self.gpt.add_system_message("Please reformat your response above to be a JSON string in the form {\"message\": ... \"playerHealthLost\": ... \"itemGained\": ...}")
            self.query_gpt()

if __name__ == "__main__":
    game = AIQuest()
    game.game_loop()