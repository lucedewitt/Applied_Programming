use std::io::{self, Write}; // imports io (self) and Write (a trait inside io)
use rand::Rng;
use std::cmp::Ordering;

fn main() {
    println!("Guess the number! (1-100)");

    //from rand, thread_rng generates a random num on current thread and .gen_range (from Rng) is the range (both ends included)
    let secret_number = rand::thread_rng().gen_range(1..=100); 

    loop {
        // print! leaves out the newline
        print!("Please input your guess: ");
        io::stdout().flush().unwrap(); // from io:stdout calls flush (retrieve buffered text) and unwrap (handle failure)

        // let = variable keyword, mut = mutable, String::new() = new function called on String, creates an empty new string
        let mut guess = String::new();

        // from io do stdin, which represents a handle to the standard input for terminal
        io::stdin()
            // calls read_line method on handle to get the user input and append to a string (&=reference, mut=mutable reference)
            .read_line(&mut guess)
            .expect("Failed to read line");

        // u32 = unsigned 32-bit int, trim = get rid of whitespace, parse = converts to another type (:=annotate variable type)
        // match lets you set conditions for Result (from parse)
        let guess: u32 = match guess.trim().parse() {
            // passes the number out or continue-s to the next loop iteration ((_) -> match all values)
            Ok(num) => num,
            Err(_) => continue,
        };

        println!("You guessed: {guess}");

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }

}