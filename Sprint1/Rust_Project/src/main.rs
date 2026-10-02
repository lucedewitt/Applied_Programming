// from std import io (self) and Write (for .flush)
use std::io::{self, Write};
// from rand and prelude import IndexedRandom
use rand::prelude::IndexedRandom;

// constant number of guesses the user gets (6 strokes to draw a stickman)
const INCORRECT_GUESS_LIMIT: u8 = 6;

// Prints everything in a vector (:char) on the same line, with a space between characters
// uses a reference so ownership doesn't transfer and calls display_man
fn print_display(list: &Vec<char>, guesses: u8, _l_list: &Vec<char>) {
    display_man(guesses);
    for _c in list {
        print!("{_c} ");
    }
    print!("\nIncorrectly guessed letters: ");
    for _c in _l_list {
        print!("{_c} ");
    }
}

// prints the stickman decoration up top based on the number of wrong guesses
fn display_man(guesses: u8) {
    println!("     _____");
    println!("    |     |");
    if guesses >= 1 {
        println!("    ◯     |")
    } else {
        println!("          |");
    }
    if guesses >= 4 {
        println!("   /|\\    |");
        println!("    |     |");
    } else if guesses >= 3 {
        println!("   /|     |");
        println!("    |     |");
    } else if guesses >= 2 {
        println!("    |     |");
        println!("    |     |");
    } else {
        println!("          |");
        println!("          |");
    }
    if guesses >= 6 {
        println!("   / \\    |")
    } else if guesses >= 5 {
        println!("   /      |");
    } else {
        println!("          |");
    }
    println!("        ‾‾‾‾‾");
}

fn main() {
    // initializes play and words
    let mut play = 1;
    let words = vec!["peace", "light", "jazzy", "often", "jewel", "chimp", "lucky", "cakes", "ocean", "linux"];

    // itinitalizes choice enum
    enum Choice {
        Letter,
        Word,
    }

    // while play is 1, do game loop
    while play == 1 {
        // initialize guesses and _s_word (secret word) (chooses random word from word to be _s_word)
        let mut guesses = 0;
        let mut rng = rand::rng(); // creates random number generator
        // .choose uses the rng to generate a random index and select a random word (.expect() to catch errors
        // and continue with an Option, and .to_string to change it into a string)
        let mut _s_word = words.choose(&mut rng).expect("Empty vector").to_string();
        // initializes characters by collecting and storing each character into a vector (aka list)
        let characters: Vec<char> = _s_word.chars().collect(); // .chars() produces characters, while .collect() adds them to vec
        // initializes filled, which keeps track of how many letters in the word are guessed
        let mut filled = 0;
        // initializes _g_characters
        let mut _g_characters: Vec<char> = Vec::new();
        

        // creates a vector (list) of underscores the same length as the word
        let mut _w_display: Vec<char> = Vec::new();
        for _c in 0..characters.len() {
            _w_display.push('_');
        }

        // while guesses is less than the limit, run code
        'menu: while guesses < INCORRECT_GUESS_LIMIT {
            // prints underscores
            print_display(&_w_display, guesses, &_g_characters);
            println!();

            println!("\n1. Guess letter\n2. Guess word");
            print!("What would you like to do? ");
            io::stdout().flush().unwrap(); // flush to retrieve buffered text and unwrap to handle failure (so print! shows up)
            
            let mut _u_input = String::new();
            // reads user input into choice
            io::stdin().read_line(&mut _u_input).expect("Failed to read line");
            // changes choice (trimmed) to a u8 (number) and error handled
            let _u_input: u8 = match _u_input.trim().parse() {
                Ok(num) => num,
                Err(_) => continue,
            };

            // creates choice (an enum value) based off of _u_input, a type: Letter or type: Word
            let choice = match _u_input {
                1 => Choice::Letter,
                2 => Choice::Word,
                // if _u_input is anything else, prompt for a 1 or 2 and continue
                _ => {
                    println!("Please enter 1 or 2");
                    continue;
                }
            };

            // matches Letter or Word
            match choice {
                Choice::Letter => {
                    // Guess Letter
                    print!("\nWhat letter are you guessing? ");
                    io::stdout().flush().unwrap();

                    // reads user input into _c_guess (as a lowercase string)
                    let mut _c_guess = String::new();
                    io::stdin().read_line(&mut _c_guess).expect("Failed to read");
                    _c_guess = _c_guess.to_lowercase();

                    // trims input and saves the first character into chosen_char
                    let user_chars: Vec<char> = _c_guess.trim().chars().collect();
                    let chosen_char = user_chars[0];

                    // initializes matched
                    let mut matched = false;

                    // loops through characters and checked if it's the same as chosen_char. If so, the index is saved to 
                    // indexes and matched is set to true
                    for (index, character) in characters.iter().enumerate() {
                        if *character == chosen_char { // * = value the reference is pointing to
                            matched = true;
                            filled += 1;
                            _w_display[index] = *character; // changes item at index to the character (value not variable)

                            // checks to see if all letters in the word are correctly guesses, quits and displays message if so
                            if filled == characters.len() {
                                println!("You've correctly guessed the word!");
                                break 'menu; // leaves menu's while loop, 'menu = label
                            }
                        }
                    }

                    // if matched is true, says the letter was in the secret word, else says it's not, increases guesses
                    // and adds the letter to _g_characters
                    if matched {
                        println!("{chosen_char} is in the secret word!\n");
                    } else {
                        _g_characters.push(chosen_char);
                        println!("No {chosen_char}'s are in the secret word.\n");
                        guesses += 1;
                    }

                } 
                Choice::Word => {
                    // Guess Word
                    print!("\nWhat's your guess? ");
                    io::stdout().flush().unwrap();

                    // reads user input into _w_guess as a lowercase string
                    let mut _w_guess = String::new();
                    io::stdin().read_line(&mut _w_guess).expect("Failed to read line");
                    _w_guess = _w_guess.to_lowercase();

                    // compares _w_guess and _s_word after trim-ing _w_guess (no whitespace so it actually compares)
                    if _w_guess.trim() == _s_word {
                        println!("Correct!");
                        _w_display = characters;
                        break 'menu; // leaves menu's while loop
                    } else {
                        println!("Incorrect");
                        guesses += 1; // adds 1 to guesses if incorrect
                    }
                }
            }
            // } else {
            //     println!("Please enter a valid option");
            // }
        }

        // print message if game quit because of lack of guesses
        if guesses == 6 {
            println!("You loose");
        }

        // print ending message thanking the player
        println!();
        print_display(&_w_display, guesses, &_g_characters);
        println!("\n\nThanks for playing!");

        // asks if user would like to play again
        print!("\nWould you like to play again? (0=no, 1=yes) ");
        io::stdout().flush().unwrap();

        // reads user input into _s_play
        let mut _s_play = String::new();
        io::stdin().read_line(&mut _s_play).expect("Failed to read line");
        // changes _s_play into a number and saves to play
        let _s_play: u8 = match _s_play.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
        play = _s_play;
    }
}