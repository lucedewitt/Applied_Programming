# Rust Hangman Game

A program that runs a game of hangman. It chooses a word from a list (vector) and lets the user guess words or letters. The user gets 6 guesses before they fail. The program loops and quits only when the user says they don't want to play again. The correctly guesses letters are displayed as well as the incorrectly guessed ones. The stickman is drawn with every incorrect guess (word or letter). Every replay of the game generates a new random word (though it could potentially choose the same one twice in a row).

## Instructions for Build and Use

Steps to build and/or run the software:

1. Check to make sure you have cargo with "cargo --version"
2. Make sure you're in the correct folder (the path should end in \\Rust_Project)
3. In the terminal, type "cargo run"

Instructions for using the software:

1. Type 1 to guess a letter or press 2 to guess a word
2. Type your word/letter
3. Repeat until the game finishes
4. Type 0 to quit the program and type 1 to play again

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Install Rust with rustup
* Run the program with an editor/IDE like Visual Studio Code
* (I specifically have rustc version 1.98.1. The project uses the rand crate version 0.9)

## Useful Websites to Learn More

I found these websites useful in developing this software:

* https://doc.rust-lang.org/book/index.html
* https://duck.ai

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* Add a multiple difficulty levels (with different numbers of incorrect guesses for each)
* Potentially add more detailed error handling