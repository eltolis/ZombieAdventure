# ZombieAdventure

Text-based, oldschool style adventure game that takes place in zombie-ridden town of Welton, Kentucky. You create your own character with stats and try to stay alive as soon as possible. Your true quest will reveal itself soon.


## Features

- character creation
- turn-based battle system
- NPCs to talk to
- multiple deaths
- save & load function
- high score board


## Version 1.0.1

- fixed problem where after installation the launch command `zombieadv` did not work directly from shell


## Installation

1. Using `setup.py` to install from source [tar](https://pypi.python.org/packages/source/Z/ZombieAdventure/ZombieAdventure-1.0.1.tar.gz#md5=29a7092a90fc591096279b9e83fb8408):

	`python setup.py install`

2. Fetching from __pip__:

	`pip install ZombieAdventure`

ZombieAdventure uses standard Python 2.7 libraries and has no external dependencies.

If you do not wish to install ZA on your system and want to run it directly, just navigate to `bin/` folder and launch it from there by typing: `python zombieadv.py`.


## Start the game

New shell binary will be added. Just type `zombieadv` to start the game.
Look where you run the game from! Save files have `.sav` extension and are saved in the current dir.


## Playing the game

You use prompt to put in commands for your character. Unlike other text-based input games, you don't really use verbs (only occasionally) - instead you type name of things.

For more information you can type `help` in the game (except battles) to bring up this help screen:

	LOOK: See where you can go.
	HINT: If you're stuck, you can get little help.
	SAVE: Save your progress.
	INV: Will display contents of your inventory.
	CHAR: Shows character stats.
	HEAL: Will heal your char if you have bandage(s).
	QUIT: Quit game.
