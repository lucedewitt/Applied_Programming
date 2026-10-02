fn main() {
    let mut x = 5;
    println!("The value of x is: {x}");
    x = 6;
    let y = 4;
    println!("The value of x is: {x}");
    
    // When putting in an evaluated expression, use empty {} and write on end
    println!("{x} plus two is {}", x+2);
    println!("{x} is equal to {y}? is {}", x==y);

    // Char variable type
    let c = 'z';
    let u: char = 'Z';
    let heart_eyed_cat = '😻';
    println!("\nChars: {c}, {u}, {heart_eyed_cat} (use single quotation marks, and use double for strings)");


    // Shadowing and Math
    let z = 6 / 4;
    println!("\n6 / 4 = {z}");

    { 
        let z = 8 / 3;
        println!("8 / 3 = {z}");
    }

    println!("z is still {z} because the previous scope ended (no more shadowing)");
    let remainder = 43 % 5;
    println!("The remainder of 43 / 5 is {remainder}");

    // Tuples
    let tup: (i32, f64, u8) = (500, 6.4, 1);
    let (a, b, c) = tup; //destructing tuple
    println!("\nThe value of a is {a}");
    println!("The last value is {}", tup.2); //accessing by . (write outside of {})
}

//Current section: Chapter 3.2, The Array Type