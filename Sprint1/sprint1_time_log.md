# CSE 310 - Sprint Time Log

Name: Luce DeWitt

Sprint #1: Rust

## Instructions

Record all CSE 310 work that you do either inside class or outside of class.  Include time learning, practicing, developing, testing, and documenting.  It is important to update this log every day.

For the Category column, record one of the following:
* IM - You are working on your Individual Module (Don't include Planning Meeting in class)
* TP - You are working on your Team Project (include Team Project Work Days)
* MTG - You are in one of the following class meetings: Planning, Stand-Up, Team Review, or Individual Review

The expected minimum amount of time each Sprint for each category is as follows:

|Categroy                       |Total Time (Hours:Minutes)|
|-------------------------------|:------------------------:|
|IM - Individual Module         |          10:00           |
|TP - Team Project              |           4:00           |
|MTG - Class Meetings           |           4:00           |
|**TOTAL**                      |        **18:00**         |

## Time Log

|Date      |Start Time|Category|Description                                 |Total Minutes|
|----------|----------|:------:|--------------------------------------------|:-----------:|
| 9/21/26  | 10:15    |   IM   | Planned personal project                   | 35          |
| 9/21/26  | 10:50    |MTG & TP| Planning meeting & filling out readme      | 25          |
| 9/21/26  | 5:05     |   IM   | Downloading & researching/learning         | 60          |
| 9/22/26  | 2:45     |   IM   | Learning & practice                        | 20          |
| 9/22/26  | 7:40     |   IM   | Learning & practice                        | 40          |
| 9/23/26  | 10:21    |   TP   | Planning                                   | 16          |
| 9/23/26  | 4:01     |   IM   | Learning & practice                        | 40          |
| 9/23/26  | 6:40     |   IM   | Learning & practice                        | 25          |
| 9/24/26  | 2:08     |   IM   | Learning & practice                        | 40          |
| 9/25/26  | 10:20    |   MTG  | Stand up meeting                           | 5           |
| 9/25/26  | 2:20     |   IM   | Learning & practice                        | 46          |
| 9/25/26  | 5:25     |   TP   | Set up React Native + Expo                 | 62          |
| 9/28/26  | 8:23     |   TP   | Setup, Git, creating Tabs/Screens          | 87          |
| 9/29/26  | 1:50     |   TP   | Team presentation slides                   | 53          |
| 9/29/26  | 9:42     |   IM   | Start coding                               | 55          |
| 9/30/26  | 10:15    |   MTG  | Team presentations (team review meeting)   | 60          |
| 9/30/26  | 4:39     |   IM   | Coding & research                          | 44          |
| 9/30/26  | 10:12    |   IM   | Coding & research                          | 18          |
| 10/1/26  | 3:36     |   IM   | Coding, debugging, learning, testing       | 178         |
| 10/1/16  | 9:20     |   IM   | Testing and finishing readme               | 27          |
| 10/2/26  | 10:35    |MTG & IM| Individual review meeting & project        | 47 (34/13)  |
|          |          |        |                                            |             |

_Note: Add more rows as needed._

## Sprint Totals

|Categroy                       |Total Time (Hours:Minutes)|
|-------------------------------|:------------------------:|
|IM - Individual Module         | 10h 41m                  |
|TP - Team Project              | 4h 5m                    |
|MTG - Class Meetings           | 2h 4m                    |
|**TOTAL**                      |                          |


<br><br><br>
## Personal Project Notes (ignore)
### AI use
- Asked how to add user input immediately after and learned print! .flush() and .unwrap()
- Debugging (comparing strings)
- Learned about io::{self, Write}
- Rust while loop syntax
- Splitting strings (.chars())
- Lists (vec), .collect(), iterators, .contains(), .enumerate(), .len(), loops, & and *
- Seeing if a line of code would work
- Loop labels

### Plan
1. Figure out how to split a word? Or get letters in word to do guess letter option  ? <span style="color: #62F40C">✓</span>
2. <span style="color: #00FFFF">**</span>Figure out how to generate random words ? -nice but technically not needed?  ? <span style="color: #62F40C">✓</spn>
3. Add __ for number of words and update if letter is guessed correct <span style="color: #62F40C">✓</span>
3. If letters are fully filled, end program <span style="color: #62F40C">✓</span>
4. Update __ if word guessed correct (add to Guess word) <span style="color: #62F40C">✓</span>
5. Add decoration (hanging thing) <span style="color: #62F40C">✓</span>
6. Animate a stickman being drawn  ? <span style="color: #62F40C">✓</span>
7. Let user play again <span style="color: #62F40C">✓</span>
8. <span style="color: #00FFFF">**</span>Add difficulty levels (change number of incorrect guesses, vampire?)
9. What is the indexes variable used for?? <span style="color: #62F40C">✓</span> (deleted it)
10. <span style="color: #00FFFF">**</span>Deal with the Err(_) thing (change later), add better error handling
11. Convert to user inputs to lowercase <span style="color: #62F40C">✓</span>
12. Add a guessed letters: section <span style="color: #62F40C">✓</spn>

key: ? = something I don't know how to do, <span style="color: #00FFFF">**</span> = bonus, if I have time/feel like it (optional), <span style="color: #62F40C">✓</span> = finished


Hangman Drawing (? potentially changed)
5 spaces : 5 _
4 spaces: | : 5 spaces: |
4 spaces: ◯ : 5 spaces: |  ?
3 spaces: / : | : \ : 4 spaces : |
4 spaces: | : 5 spaces : |
3 spaces: / : 1 space : \ : 4 spaces: |
8 spaces: 5 ‾
     _____
    |     |
   ◯     |
   /|\    |
    |     |
   / \    |
        ‾‾‾‾‾