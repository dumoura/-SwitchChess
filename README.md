# ![Beta Version](https://img.shields.io/badge/version-beta-orange) Switch Chess

This is a Python implementation of the game Switch Chess using Pygame library.


## How to play

Switch Chess is a two-player board game, played on a chessboard, that is essentially a combination of chess and reversi.

The goal is to capture all the opponent's pieces or get the opponent to a position where they cannot make any more moves.

Each player takes turns moving one of their pieces according to the rules of chess. However, after every full move (i.e., both players have made a move), a coin is flipped. Depending on the result of the coin flip, the player to move next will switch to the other color.

## Installation

You need Python 3.x installed on your system to run this game.

1. Clone this repository or download the source code as a ZIP file and extract it.
2. Open a terminal or command prompt window in the project directory.
3. Install the required packages by running `pip install -r requirements.txt` command.
4. Run the game by typing `python main.py` command.

## How to play

1. When the game starts, the board will be displayed on the screen with pieces in their starting positions.
2. Click on one of your pieces to select it. If the piece has any valid moves, they will be highlighted in green.
3. Click on one of the green squares to move your piece there.
4. After every full move, a coin will be flipped to determine the player who will move next. 
5. The game ends when one player captures all of the opponent's pieces or when the opponent cannot make any more moves. 

## Controls

* Click on a piece to select it and see valid moves.
* Click on a green square to move the selected piece there.
* Press 'T' to change the board theme.
* Press 'R' to reset the game.
* Press 'Esc' to quit the game.

## Requirements

* Python 3.x
* Pygame library

You can install the required packages by running `pip install -r requirements.txt` command in your terminal or command prompt window.

## Deploying to a Website

To deploy the game on a website, you need to first build the game using the following command:

```
python build.py
```

This will create a `build` folder with the necessary files. Then, compress the `build` folder into a ZIP file named `web.zip`. 

Next, upload the `web.zip` file to your web server or hosting service. Once uploaded, extract the contents of the `web.zip` file to a folder named `web-cache` on your web server. This folder will store the game cache.

Finally, move all the extracted files from the `web-cache` folder to the `web` folder. This will make the game accessible through the website's URL.

Note that the `version.txt` file contains the version number of the game. Make sure to update this file whenever you make changes to the game and deploy a new version.

________

