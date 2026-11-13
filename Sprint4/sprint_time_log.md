# CSE 310 - Sprint Time Log

Name: Luce DeWitt

Sprint #: 4

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
| 11/2/26  | 10:15    |MTG & IM| Planning meeting                           | 63 (31?)    |
| 11/3/26  | 5:25     |   IM   | Planning, brainstorming, research          | 60          |
| 11/4/26  | 10:17    |   TP   | Dashboard, fixing bugs, updating expo      | 64          |
| 11/5/26  | 3:37     |   IM   | Plan & brainstorm, download, color codes   | 120         |
| 11/6/26  | 10:17    |MTG & TP| Stand up meeting & team project work day   | 60 (5)      |
| 11/6/26  | 3:37     |   IM   | Tutorial                                   | 61          |
| 11/9/26  | 10:15    |   TP   | Updating, fixed problems, budget page      | 66          |
| 11/9/26  | 8:57     |   IM   | Created project, designed sprite           | 133         |
| 11/10/26 | 4:17     |   TP   | Made team presentation slides              | 6           |
| 11/10/26 | 4:30     |   IM   | Made more sprites (I need to stop)         | 65          |
| 11/11/26 | 10:18    |MTG & TP| Team presentations (team review meeting)   | 59 (50)     |
| 11/11/26 | 8:04     |   IM   | Created background                         | 170         |
| 11/12/26 | 8:55     |   IM   | Added music and filled out readme          | 25          |
| 11/13/26 | 10:18    |   MTG  | Individual review meeting                  |             |
|          |          |        |                                            |             |
|          |          |        |                                            |             |

_Note: Add more rows as needed._

## Sprint Totals

|Categroy                       |Total Time (Hours:Minutes)|
|-------------------------------|:------------------------:|
|IM - Individual Module         | 11h 36m                  |
|TP - Team Project              | 4h 15m                   |
|MTG - Class Meetings           | 1h 58m                   |
|**TOTAL**                      |                          |


<br>
<br>
<br>


## Personal Notes (ignore)
<span style="color: #EEDD00">Requirements:</span>
- The game must display a background <span style="color: #62F40C">✓</span>
- The game must have at least 1 un-moveable object <span style="color: #62F40C">✓</span>
- The game must have at least 1 moveable object <span style="color: #62F40C">✓</span>
- The game must include collisions of at least 2 objects <span style="color: #62F40C">✓</span>
- The game must take user input from the keyboard or mouse <span style="color: #62F40C">✓</span>

Stretch: (choose one)
- Allow the user to save and load the game
- <span style="color: #EE70EE">Add music or sound effects to the game</span> <span style="color: #62F40C">✓</span>
- Provide levels in your game that change the difficulty of the game

PLANNING
1. What should I do it in? PyGame or Godot? Preliminary decison: <span style="color: #FF8A00">PyGame</span> (easier to install and learn, probably)
- What's collision? How would I implement that in 2D vs 3D? Leaning towards doing <span style="color: #FF6242">2D</span> (seems easier)
  - Collision is interaction between two things. Like a character and the floor, or a plane and a bullet. It works in both 2D and 3D
- What basic idea do I have? Platformer? Space shooter game? What would the type fit best?
  - I do like platformers. Running around is fun. Could be a puzzle? Or a magic maze? <span style="color: #FF0000">~~Space shooter could also be fun.~~</span> Maybe something like the alien board game I really enjoy. Ooo, or something with teleportation. Or themed. What am I into? One Piece? Avatar? <span style="color: #FF0000">~~Haikyuu? Volleyball could maybe be fun.~~</span> Harry Potter? Star Wars? If it's a personal project, does copyright still apply? I don't think so... <span style="color: #FF0000">~~Ooo, maybe some type of potion making game? Potentially like that one board game?~~</span> Could you turn a board game into a video game? Is that a good idea? <span style="color: #FF0000">~~Could I make a Sagrata game?~~</span>
    - **~~One Piece: Fight marines. Ooo, use devil fruit powers. I really like Law's power. Some sort of surgery? Could do teleportation with this. Potentially a cooking or ship building game. What would the immovable objects be? Ooo, a law related fight. Like his backstory or Dressrosa maybe. <span style="color: #EEDD00">Law stuff could fulfill the requirements. Maybe. If it's teleportation would there be any need to moveable objects? Mmm, it would be hard...</span>~~**
    - <span style="color: #62F40C">Avatar:</span> probably Seven Havens themed, since it's my current fixation. Also, Jae. Love him, he's cool. Maybe him on his skateboard thing? Or a fight but with wind powers. Or like, an obstacle course. <span style="color: #EEDD00">Fight or obstacle course would fulfill the requirements</span>
    - **~~Harry Potter: casting magic? Castle is cool, but what could I do? You could do a fighting game, but I feel like I prefer my other fighting game options. Puzzle or maze? But with magic? Ooo, or train. I like trains. Maybe a like, help the train get to Hogwarts and choose the right path? That wouldn't fulfill all the requirements though.~~**
    - **~~Star Wars: what would be fun... I like the Clone Wars era the most, so probably something Jedi or Clone related. Maybe a force related mini game? Or like, obsticle course? Like the one in the backstory in Jedi Fallen Order? Ooo, or a build your own lightsaber game. Or just a figting game. Is there anything interesting that's Clone related... Kamino Training? Piloting? Or a jedi Clone? That could be fun. <span style="color: #EEDD00">The obsticale course or battle could easily fulfill all the requirements</span>~~**
    - **~~Maze/teleportation: eh (not as exciting)~~**
    - Alien game: 3 types of enemies (no bosses (unless diffiuclty level stretch?)), move at different speeds, different attacks. Go to 5? (change based on difficulty level) places to disarm traps. Move and shoot. Dice? Does disarming take a die roll or just an action? How would timing work in this? If I couldn't do timing, how would I change things? I don't think it works if you can't do timing. <span style="color: #EEDD00">This has a background and collision, and immovable objects, but does it have movable objects? Does the player count? Or could I add boxes or something??</span> It would be very complex though, do I have time?
- How difficult are they compared to each other?
  - PyGame is written in code. You program the game. Godot is a game engine with an editor. You build with nodes and scripts, and it handles the actually program. Installing PyGame would be much easier. (Not a whole application)
2. What am I actually doing? What is the idea? <span style="color: #62F40C">Avatar obstacle course (backup option: alien game (very complex))</span>
3. What stretch challenge am I doing? (music could be easiest or hardest, difficulty levels is fine)
- <span style="color: #62F40C">Music:</span> Sagrata, anything
  - Where would I even get the music? Would I make it myself? That could be fun, but do I have the time?
- Save and load: fighting game? Levels? Eh.. -_-
- Difficulty levels: fighting games (shooter), volleyball, puzzles/mazes 
4. What counts as an unmoveable object? Or a moveable? Like, would moving cards around in Solitare count as moveable? And the board as unmoveable? Or does that not count as an object?
- Would Sagrata have moveable and unmovable objects? Or two collisions? If you dragged and dropped the dice ... maybe?

https://coolors.co/966961-903527-cb743e-963d1b-582b25-77655f-cdb0a0-5a3020-e0a57a-815239 