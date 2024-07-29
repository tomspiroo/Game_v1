# Game_v1
Early development game

# To do:
Check out Tiled do make new levels, Im assuming that the Tiled app generates the images needed as well as the csv files for where each level of the floor is (walkable pathing, obstacles, grass, enemies, player)

CSV for objects seems fucked for the object indexing and placement, inconsistent throughout the level, when make own levels make sure everything is alright

Move all asseted to their own folder 'assets' for easy file manipulation and to make the folderspace look clean, WILL NEED TO CHANGE PATHING IN CODE IF YOU ARE TO DO THIS

Attacking while moving was not permitted in the tutorial, will have to fix this later so that you can attack and move at the same time, to do so go to 'player.py' in the function 'keyboard_input' and change the function's global 'if' statement to not hold all the inputs while attacking, instead add that conditional to the attack and magic keys only since there does need to be a cooldown of the weapons and magic attacks

When attack button and a move button is pressed at the saeme time there seems to be a bug where the character doesnt take the 'no movement when attacking' policy properly. This might eventually get changed since the attacking while moving might not be a mechanism I want but at the minute when attacking while moving the animation for the weapon does not move with the character, leaving it in the place of spawn until it is destroyed.

Currently (20/07/2024) the animate function in both the player and enemy are the same even though the bloke said theyre different? can put into Entity if they remain the same 

Attack cooldown in 'enemies.py' for each enemy is a global feature where all enemies share the attack cooldown, this is not what I want, thus the cooldown will be added to the enemy dictionary.

Level and even enemy data might be easier to be implemented via CSV files rather than having dictionaries set up for their data. In the low enemy variety it has been good to use dictionaries to learn them but when having a higher amount of enemies i might need to import all the data from a CSV and probably put them into dictionaries like it is current being used to make the code translatable. As for the levels there is already CSV files used for the map, might be able to keep a rough implementation of that is already going on within the level, however there might need to be some change in the code so that the 'level.py' code is not restricted to the one level.

Enemies overlap, can take this out by adding more collision mechanics later on

Can cast healing spell even if the health bar is maxed out, can change this to be different if wanted but it sounds kinda good to punsih stupid players

Currenlty (27/07/2024) magic stat the player has enhances the speed of magic recovery and will be used for the damage of the flame spell but does not alter the healing amount, might change this 

Energy recovery speed will need to be adjusted/scaled/altered depending on game balance 

In 'magic.py' there is a double up in a line of code in the 'flame()' function, can put this outside of conditional if statement to make more streamline and to potentially check if the status of the player is successfully being read by the flame function

In 'particles.py' when calling the particle effects, currently within the __init__ function there is an initilisation of the sprite_type as a borad 'magic', when including more attacking spells this will need to be changed to suit the multitude of attacking spells by adding another parameter to the init function, this will set the sprite_type for the different spells 

Currently upgrade menu is toggled when the 'm' key is pressed, probably change this later on 

Currently nothing happens on player death, this will need to be introduced

Currently when upgrading the stats of the player, the health and energy bar so not increase in size when the specific stats are increased, only the percentage of the health bar changes. This could be changed to an increasing health bar that grows with the stat or by adding numbers displaying the health out of the total health pool, like: 123/150 which goes up and down depending on healing and damage 

In upgrade menu, when the stat is maxed it still says there is a 'cost' for the stat to be upgraded again, when the stat reaches the max change the text at the bottom to say "Max" or something similar

When adding more levels to the game, make sure to change the main file line 30 so that the fill is of the specific level

For the sounds, will need to once again change the pathing for the sounds when the file system is adjusted to put all the assets into a single folder. Also the sounds for the magic can be taken out of the init method and added to the dictionary in the settings so it can be called upon more easily

In the menu main menu you should be able to let the user alter the sounds by looking up whereever there is some sort of sound implementation, they might need to be categorised so the user can adjust based on: main volume, music, backgound sounds, speech, etc

# Final game ideas - Title: The Garden?:
Gameplay:
- NPCs are randomly encountered within stages  of the run and will occupy a place at the beginning of the level and will stay there in that save, 'unlocking' them and their assistance. 

NPCs:
- Dog NPC, main companion and will be the first NPC the character finds along the runs, might spawn with him. Potentially: Eventually a demon steals the dog and turns him into cerebros (3-headed dog) to fight as a boss, knocking him out and making the dog rememebr you to take back to the launch area. Then you will have to find a way to cure him (defeat the demon who stole him?)
- Eventually the player will encounter an 'builder' who will be able to make room for late game NPCs and upgrading the launch stage
- A priest that offers blessings, he has alzheimers and cant remmeber his name or the charatcer each time you meet him in the launch room and he will roam since he lost his way due to his mental illness, thus giving blessings along the run rather than help at the start (maybe initial blessing). The dialogue box will give you randomised options as to what his name will be for the run since he cant remember. At late stages of the game there will be an option for 'not a priest' or then he turns into a demon saying 'thats right im somthing else completely' or something like that and will spawn devils for a boss fight
- Miner can give access to underground areas via bombs/shovel/pickaxe

Debug:
- impleemnt a report/record bug fucntion while game is in alpha in the pause menu, will probabl consist of adding to a .txt file where logs can be made

Enemies:
- See NPCs for some potential boss ideas
- assassin blinking enemy that blinks behind character, delayed heavy attack, then runs from main character. Could be a boss assassin, maybe from a 'league of assassins' type shit.