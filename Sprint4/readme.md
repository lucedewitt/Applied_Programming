# Seven Havens game

A simple game (more like a base of a game) that's Seven Havens themed. You can push a box around and jump between a couple platforms. All sprites were created by me in Piskel.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Download the latest Python 3.13 release at the offical Python page (https://www.python.org/downloads/release/python-31317/)
2. Install it (if it asks, check Add python.exe to PATH)
3. Restart VS Code (check installation with the command 'py -3.13 --version' in the terminal)
4. Run 'py -3.13 -m pip install pygame' in the terminal
5. Run 'py -3.13 -c "import pygame; print(pygame.version.ver)"' to check that PyGame installed
6. If you have multiple python versions installed: 
- Press Ctrl+Shift+P.
- Choose Python: Select Interpreter.
- Select Python 3.13.
7. In the terminal run 'pip install arcade --user' (if you have multiple Python versions, run '"C:\Users\YOURUSER\AppData\Local\Programs\Python\Python313\python.exe" -m pip install --user arcade' (replace YOURUSER with the user file you want to install it under))
8. Run the game/file

Instructions for using the software:

1. Press the run button
2. If you don't have a run button, type: "python sevenhavens.py"
3. Try pushing the box around and jumping between the platforms!
4. (If you die because you walked off the edge, close the window and rerun it)

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python version 3.13.x (I used 3.13.17)
* PyGame (I used 2.6.1)

## Useful Websites to Learn More

I found these websites useful in developing this software:

* Collision: What is Collision? (https://nerdyteachers.com/PICO-8/Collision/92)
* Pygame vs Godot: Which Should You Learn? (https://coddy.tech/docs/pygame/pygame-vs-godot)
* The Python Arcade Library (https://api.arcade.academy/en/stable/)
* Piskel (https://www.piskelapp.com/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* Add more difficult jumps
* Add a double-jump? Or airbending powers?
* Add multiple levels
* Make it so the game reloads the character if they fall out of the game
* Add more sprite animations and characters
