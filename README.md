


# AI Quest 2
![DALL·E 2023-09-14 02 35 02 - a spaceship overlooking an exotic planets in pixel art](https://github.com/plyalyut/ai-quest2/assets/22432684/636d7400-1ea1-4ca9-8f5d-e6c37574747d)

Welcome to the AI Quest 2 repository! This game merges the immersive capabilities of AI storytelling with open-world exploration set in a vast universe. Experience a unique adventure where every conversation you have and decision you make with the GPT narrator will shape your journey!

## Overview

AI Quest 2 positions the player in an expansive space setting. Guided and narrated by GPT, players will take turns conversing with the narrator. The game dynamically tracks player state, health, inventory, and choices, ensuring a unique experience every time.

## Features
  
- **Dynamic Storytelling**: With the GPT narrator, every choice you make has a consequence. Forge your path and see where the story takes you.
  
- **State Tracking**: Your health and items are crucial. Keep an eye on your resources and use them wisely on your journey.

- **Interactive Conversations**: Influence the course of your journey by how you communicate with the AI. Gain allies, gather information, or make enemies—it's up to you!

## How to Play

1. **Start the Game**: Launch AI Quest 2 and select your character.
  
2. **Interact with the GPT Narrator**: As you explore, the GPT narrator will provide you with descriptions, challenges, and choices. Decide your actions and communicate them to the narrator.
  
3. **Inventory Management**: Check your items regularly and decide when to use them. Some items may help you advance in the story, while others might save you in perilous situations.
  
4. **Survive**: Watch your health! Engage in battles, avoid hazards, and make sure you're always ready for what's ahead.

## Example Game

![t-rec](https://github.com/plyalyut/ai-quest2/assets/22432684/07381547-c19f-4deb-a42d-979e32265f99)

```diff
+ Suddenly, a beeping sound rings out in the spaceship; The Stardust Explorer's fuel tank is almost empty. You spot two nearby planets through the window. One is Planet Xenon, which is known for an abundant supply of fuel but frequented by space pirates. The other is safer, the misty Planet Yttrium but you're not sure if there's enough fuel. If you're fortunate, there might be some discarded medkits or tools on either planet. Which planet do you visit? Planet Xenon (known to be dangerous) or Planet Yttrium (safer but uncertain fuel supply)?
# What do you do? Planet Yttrium
+ After hours of navigating through the star-studded darkness of space, you finally reach the Planet Yttrium. It's a beaten up, rocky terrain filled with old remnants of a long-lost civilization. As you explore, you trip over an object embedded in the dirt and you lose some health. Upon closer inspection, you realize it's a 'Polaron Pulse Pistol', an ancient yet trusted weapon.
- You lost health! Your health is now 90
! You gained an item! Your items are now ['Polaron Pulse Pistol']
# What do you do? what does the Polaron Pulse Pistol do 
! The Polaron Pulse Pistol is a powerful energy pistol used for defending against alien threats. It shoots a pulse of polaron particles that can stun or incapacitate most creatures and harm mechanical devices. Use it wisely as it carries a limited amount of charges.
# What do you do? Continue explroing yttrium
+ You continue exploring Yttrium. You tread lightly across the rocky terrain, eyes warily scoping the ever-watchful twilight. As you press on, you trip over a hidden trap. The result is a fall into a shallow canyon, scrapping your elbow in the process. On a bright side, you find a half-buried item next to you.
- You lost health! Your health is now 80
! You gained an item! Your items are now ['Polaron Pulse Pistol', 'Space Compass']
```

## Installation



```bash
git clone https://github.com/plyalyut/ai-quest2.git
cd ai-quest2
pip3 install -r requirements.txt
```

Create a config.yaml file:
```yaml
OPENAI_API_KEY: YOUR_OPENAI_API_KEY_HERE
```
Replace `YOUR_OPENAI_API_KEY_HERE` with your actual API key.

Run 
`python3 app.py`

## Dependencies

- Python 3.8+
- OpenAI GPT (via OpenAI API) (Need 

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you'd like to change. Ensure to update tests as appropriate.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy your journey across the universe with AI Quest 2!
