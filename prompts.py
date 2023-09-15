STARTING_PROMPTS = [
    "The following is a conversational game where the AI assistant takes part in telling a story on a fictional world in space in the style of Zork. " + 
    "The user has a health counter that starts at 100, and upon finding medkits or visitng a hospital, it grants the user health. We also can randomly find items. " + 
    "Upon bad events, the user loses health or an item breaks. " + 
    "Please provide the user with two possible actions that the user can take. " + 
    "Please generate the story, limit it to 100 words per response. Please format 1 response as a JSON in the form {\"message\": ..., \"playerHealthLost\": ... \"itemGained\": ...}. Do not return anything other than a JSON string. Return itemGained as None if no item is gained. " +
    "Example Output: {'message': 'You wake up in your spaceship, the 'Stardust Explorer', cruising through the Milky Way.', 'playerHealthLost': 20, 'itemGained': 'knife'} "
]

# This is a helpful prompt to format our responses in the right way
GPT_REFORMAT = "Please reformat your response above to be a JSON string in the form {\"message\": ... \"playerHealthLost\": ... \"itemGained\": ...}"

prompts = [
]