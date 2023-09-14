import yaml
import openai

PATH_TO_CONFIG = "config.yaml"

# GPT is a connector to the API powering ChatGPT
class GPT:
    def __init__(self):
        self._read_api_key(PATH_TO_CONFIG)
        self.messages = []

    def _read_api_key(self,path):
        with open(path, 'r') as f:
            configs = yaml.safe_load(f)
            self._OPEN_AI_API_KEY = configs["OPENAI_API_KEY"]

    def add_system_message(self, message):
        self.messages.append({'role': 'system', 'content': message})
    
    def add_user_message(self, message):
        GPT_FORMATTING = "Please format your response as a JSON string {\"message\": ... \"playerHealthLost\": ... \"itemGained\": ...}"
        self.messages.append({'role': 'user', 'content': message+ " " + GPT_FORMATTING})

    def get_messages(self):
        return self.messages
    
    def clear_messages(self):
        self.messages = []

    def query_api(self):
        openai.api_key = self._OPEN_AI_API_KEY
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=self.messages,
        )
        return response["choices"][0]['message']["content"]
    