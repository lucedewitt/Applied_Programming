import sqlite3
import time

def print_book_data(books: list[tuple[str, str, str, str, int, int, float]]):
    """Prints the data of each book (title, author, description, genres, year, lengeth, rating) in a list of books (each book is a tuple)"""
    # prints data for each book in books
    for book in books:
        # prints title, author, year published, description, and the start of genres
        print(f"\n{book[0]} by {book[1]}, published in {book[4]}\n{book[2]}")
        print("Genres:", end=" ")
        # calls split_genres
        genres = split_genres(book[3])
        # prints each genre in genres
        for genre in genres:
            print(f"{genre},", end=" ")
        # prints page count and rating
        print(f"\n{book[5]} pages, {book[6]} stars")
        time.sleep(1)
    return;

def split_genres(genres: str):
    """Splits a string at the | and returns them as a list"""
    # splits data and stores in genres_list, which is returned
    genres_list = genres.split("|")
    return genres_list

def main():
    # creates a database and connection
    con = sqlite3.connect("library-catalog.db")
    cur = con.cursor()

    # creates table if it doesn't already exist
    cur.execute("CREATE TABLE IF NOT EXISTS catalog(title, author, description, genres, year, length, rating)")

    # Creates a unique index (rule for the table) that prevents duplicate rows 
    cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS catalog_row_unique ON catalog(title, author, description, genres, year, length, rating)")
    con.commit()


    # list of starting book data
    data = [
        ("Ender's Game", "Orson Scott Card", """In order to develop a secure defense against a hostile alien race's next attack, government agencies breed child geniuses and train them as soldiers. A brilliant young boy, Andrew "Ender" Wiggin lives with his kind but distant parents, his sadistic brother Peter, and the person he loves more than anyone else, his sister Valentine. Peter and Valentine were candidates for the soldier-training program but didn't make the cut―young Ender is the Wiggin drafted to the orbiting Battle School for rigorous military training. Ender's skills make him a leader in school and respected in the Battle Room, where children play at mock battles in zero gravity. Yet growing up in an artificial community of young soldiers Ender suffers greatly from isolation, rivalry from his peers, pressure from the adult teachers, and an unsettling fear of the alien invaders. His psychological battles include loneliness, fear that he is becoming like the cruel brother he remembers, and fanning the flames of devotion to his beloved sister. Is Ender the general Earth needs? But Ender is not the only result of the genetic experiments. The war with the Buggers has been raging for a hundred years, and the quest for the perfect general has been underway for almost as long. Ender's two older siblings are every bit as unusual as he is, but in very different ways. Between the three of them lie the abilities to remake a world. If, that is, the world survives.""", "Science Fiction|Fantasy|Fiction|Young Adult|Dystopia", 1985, 324, 4.31),
        ("Fablehaven", "Brandon Mull", """Follow Kendra and her brother, Seth, who have no idea their grandfather is the current caretaker of Fablehaven, as they face the greatest challenge of their lives to protect the sanctuary and save their family. Race with Seth through dangerous woods, dodging projectiles hurled by dark denizens of the forest. See the Fablehaven yard turn from a monochromatic garden with bees and butterflies to a brilliant, full-color oasis of colorful flowers and fairies. Watch Hugo the golem chuck pumpkins from one side of the page to the other. And witness Kendra fly with warrior fairies in a dramatic battle painting you'll want to have framed on your wall.""", "Fantasy|Young Adult|Middle Grade|Fiction|Magic", 2006, 351, 4.14),
        ("Rise of the Evening Star", "Brandon Mull", """At the end of the school year, Kendra and her brother, Seth, find themselves racing back to Fablehaven, a refuge for mythical and magical creatures. Grandpa Sorenson, the caretaker, invites three specialists - a potion master, a magical relics collector, and a mystical creature trapper - to help protect the property from the Society of the Evening Star, an ancient organization determined to infiltrate the preserve and steal a hidden artifact of great power. Time is running out. The Evening Star is storming the gates. If the artifact falls into the wrong hands, it could mean the downfall of other preserves and possibly the world. Will Kendra learn to use her fairy gifts in time? Will Seth stay out of trouble? Can they overcome paralyzing fear? Find out in book 2 of this bestselling series.""", "Fantasy|Young Adult|Middle Grade|Fiction|Magic", 2007, 456, 4.19),
        ("Grip of the Shadow Plague", "Brandon Mull", """Strange things are afoot at Fablehaven. Someone or something has released a plague that transforms beings of light into creatures of darkness. Seth discovers the problem in its infancy, but as the infectious disease spreads, it becomes clear that the preserve cannot hold out for long. In dire need of help, the Sorensons question where to turn. The Sphinx has always given sound advice-but is he a traitor? Inside the Quiet Box, Vanessa might have information that could lead to a cure-but can she be trust? Meanwhile, Kendra and members of the Knights of the Dawn must journey to a distant preserve and retrieve another hidden artifact. Will the Society of the Evening Star recover it first? Will the plague eclipse all light at Fablehaven? Find out in Fablehaven: Grip of the Shadow Plague.""", "Fantasy|Young Adult|Middle Grade|Fiction|Magic", 2008, 477, 4.31),
        ("Secrets of the Dragon Sanctuary", "Brandon Mull", """Brace yourself for a shocking secret. Two hidden artifacts have been found. Three more remain unrecovered. More preserves face destruction as the Society of the Evening Star relentlessly pursues new talismans. Reading in Patton's Journal of Secrets, Kendra learns the location of the key to a vault housing one of the artifacts. In order to retrieve it, the Knights of the Dawn must enter a death trap — a dragon sanctuary called Wyrmroost. The mission cannot proceed without stealing a sacred object zealously guarded by the centaurs. Anybody seen Seth? The race is on to acquire all five of the artifact keys to the great demon prison. Will the Knights of the Dawn conquer Wyrmroost? Who can stop the Sphinx? Can Vanessa be trusted to help? What artifact will be found next?""", "Fantasy|Young Adult|Middle Grade|Fiction|Dragons|Magic", 2009, 535, 4.39),
        ("Keys to the Demon Prison", "Brandon Mull", """After many centuries of plotting, the Sphinx -- leader of the Society of the Evening Star -- is after the five artifacts needed to open the great demon prison, Zzyxx. Kendra, Seth, and the Knights of the Dawn are in a race to strange and exotic preserves across the globe in an effort to intercept the final artifacts. The stakes have never been higher. The risks have never been more deadly as the forces of light and darkness collide at last.""", "Fantasy|Young Adult|Middle Grade|Fiction|Magic", 2010, 593, 4.46),
        ("Nevermoor: The Trials of Morrigan Crow", "Jessica Townsend", """A cursed girl escapes death and finds herself in a magical world - but is then tested beyond her wildest imagination.\nMorrigan Crow is cursed. Having been born on Eventide, the unluckiest day for any child to be born, she's blamed for all local misfortunes, from hailstorms to heart attacks--and, worst of all, the curse means that Morrigan is doomed to die at midnight on her eleventh birthday.\nBut as Morrigan awaits her fate, a strange and remarkable man named Jupiter North appears. Chased by black-smoke hounds and shadowy hunters on horseback, he whisks her away into the safety of a secret, magical city called Nevermoor.\nIt's then that Morrigan discovers Jupiter has chosen her to contend for a place in the city's most prestigious organization: the Wundrous Society. In order to join, she must compete in four difficult and dangerous trials against hundreds of other children, each boasting an extraordinary talent that sets them apart - an extraordinary talent that Morrigan insists she does not have. To stay in the safety of Nevermoor for good, Morrigan will need to find a way to pass the tests - or she'll have to leave the city to confront her deadly fate.""", "Fantasy|Middle Grade|Fiction|Young Adult|Magic|Mystery", 2017, 465, 4.31),
        ("Wundersmith: The Calling of Morrigan Crow", "Jessica Townsend", """Wunder is gathering in Nevermoor ...\nMorrigan Crow may have defeated her deadly curse, passed the dangerous trials and joined the mystical Wundrous Society, but her journey into Nevermoor and all its secrets has only just begun. And she is fast learning that not all magic is used for good.\nMorrigan Crow has been invited to join the prestigious Wundrous Society, a place that promised her friendship, protection and belonging for life. She's hoping for an education full of wunder, imagination and discovery - but all the Society want to teach her is how evil Wundersmiths are. And someone is blackmailing Morrigan's unit, turning her last few loyal friends against her. Has Morrigan escaped from being the cursed child of Wintersea only to become the most hated figure in Nevermoor?\nWorst of all, people have started to go missing. The fantastical city of Nevermoor, once a place of magic and safety, is now riddled with fear and suspicion...""", "Fantasy|Middle Grade|Fiction|Young Adult|Magic|Mystery", 2018, 467, 4.47),
        ("Hollowpox: The Hunt for Morrigan Crow", "Jessica Townsend", """Morrigan Crow and her friends have survived their first year as proud scholars of the elite Wundrous Society, helped bring down the nefarious Ghastly Market, and proven themselves loyal to Unit 919. Now Morrigan faces a new, exciting challenge: to master the mysterious Wretched Arts, and control the power that threatens to consume her.\nBut a strange and frightening illness has taken hold of Nevermoor, turning infected Wunimals into mindless, vicious Unnimals on the hunt. As victims of the Hollowpox multiply, panic spreads. And with the city she loves in a state of fear, Morrigan quickly realizes it's up to her to find a cure for the Hollowpox, even if it will put her - and everyone in Nevermoor - in more danger than she ever imagined.""", "Fantasy|Middle Grade|Fiction|Young Adult|Magic|Mystery", 2020, 471, 4.47),
        ("Silverborn: The Mystery of Morrigan Crow", "Jessica Townsend", """In the magical city of Nevermoor, long-buried secrets are coming to light, and Morrigan Crow's life is about to turn upside down.\nWhen Morrigan is invited into Nevermoor's wealthy Silver District, she discovers a world of extravagance and a family mystery she's eager to unravel. She could never imagine where it will lead: a white wedding, a golden dragon and a red pool of blood.\nEmbroiled in suspicion and danger, Morrigan leaps head first into a murder investigation, while also grappling with her ever-growing Wundersmith powers. And although her friends are there to help, she fears that could change if they learn she's keeping a terrible secret of her own.\nAs shadowy forces awaken in Nevermoor, can Morrigan find a killer and solve the mystery in her own past … before the clock strikes midnight?""", "Fantasy|Middle Grade|Fiction|Young Adult|Magic|Mystery", 2025, 672, 4.44),
        ("The Hobbit", "J.R.R. Tolkien", """In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.""", "Fantasy|Classics|Fiction|Young Adult|High Fantasy|Dragons", 1937, 366, 4.3),
        ("The Hunger Games", "Suzanne Collins", """Winning means fame and fortune. Losing means certain death. The Hunger Games have begun. . . .\nIn the ruins of a place once known as North America lies the nation of Panem, a shining Capitol surrounded by twelve outlying districts. The Capitol is harsh and cruel and keeps the districts in line by forcing them all to send one boy and one girl between the ages of twelve and eighteen to participate in the annual Hunger Games, a fight to the death on live TV.\nSixteen-year-old Katniss Everdeen regards it as a death sentence when she steps forward to take her sister's place in the Games. But Katniss has been close to dead before-and survival, for her, is second nature. Without really meaning to, she becomes a contender. But if she is to win, she will have to start making choices that weigh survival against humanity and life against love.""", "Young Adult|Dystopia|Fiction|Fantasy|Science Fiction|Romance", 2008, 374, 4.36),
        ("Cinder", "Marissa Meyer", """The prince straightened, forcing her gaze to follow him. “You're not quite what I was expecting.”\nHumans and androids crowd the raucous streets of New Beijing. A deadly plague ravages the population. From space, a ruthless lunar people watch, waiting to make their move. No one knows that Earth's fate hinges on one girl. . . .\nCinder, a gifted mechanic, is a cyborg. She's a second-class citizen with a mysterious past, reviled by her stepmother and blamed for her stepsister's illness. But when her life becomes intertwined with the handsome Prince Kai's, she suddenly finds herself at the center of an intergalactic struggle, and a forbidden attraction. Caught between duty and freedom, loyalty and betrayal, she must uncover secrets about her past in order to protect her world's future.\nWith high-stakes action and a smart, resourceful heroine, Cinder is a Cinderella retelling that is at once classic and strikingly original.""", "Fantasy|Young Adult|Science Fiction|Romance|Dystopia|Retellings|Fiction|Fairy Tales", 2012, 400, 4.12),
        ("Red Rising", "Pierce Brown", """Darrow is a Red, a member of the lowest caste in the color-coded society of the future. Like his fellow Reds, he works all day, believing that he and his people are making the surface of Mars livable for future generations. Yet he toils willingly, trusting that his blood and sweat will one day result in a better world for his children.\nBut Darrow and his kind have been betrayed. Soon he discovers that humanity reached the surface generations ago. Vast cities and lush wilds spread across the planet. Darrow—and Reds like him—are nothing more than slaves to a decadent ruling class.\nInspired by a longing for justice, and driven by the memory of lost love, Darrow sacrifices everything to infiltrate the legendary Institute, a proving ground for the dominant Gold caste, where the next generation of humanity's overlords struggle for power. He will be forced to compete for his life and the very future of civilization against the best and most brutal of Society's ruling class. There, he will stop at nothing to bring down his enemies . . . even if it means he has to become one of them to do so.""", "Science Fiction|Fantasy|Fiction|Dystopia|Young Adult|Adult", 2014, 382, 4.27),
        ("A Discovery of Witches", "Deborah Harkness", """A richly inventive novel about a centuries-old vampire, a spellbound witch, and the mysterious manuscript that draws them together.\nDeep in the stacks of Oxford's Bodleian Library, young scholar Diana Bishop unwittingly calls up a bewitched alchemical manuscript in the course of her research. Descended from an old and distinguished line of witches, Diana wants nothing to do with sorcery; so after a furtive glance and a few notes, she banishes the book to the stacks. But her discovery sets a fantastical underworld stirring, and a horde of daemons, witches, and vampires soon descends upon the library. Diana has stumbled upon a coveted treasure lost for centuries-and she is the only creature who can break its spell.\nDebut novelist Deborah Harkness has crafted a mesmerizing and addictive read, equal parts history and magic, romance and suspense. Diana is a bold heroine who meets her equal in vampire geneticist Matthew Clairmont, and gradually warms up to him as their alliance deepens into an intimacy that violates age-old taboos. This smart, sophisticated story harks back to the novels of Anne Rice, but it is as contemporary and sensual as the Twilight series-with an extra serving of historical realism.""", "Fantasy|Romance|Fiction|Paranormal|Vampires|Witches|Magic|Urban Fantasy|Supernatural", 2011, 592, 4.02),
        ("City of Bones", "Cassandra Clare", """When fifteen-year-old Clary Fray heads out to the Pandemonium Club in New York City, she hardly expects to witness a murder—much less a murder committed by three teenagers covered with strange tattoos and brandishing bizarre weapons. Then the body disappears into thin air. It's hard to call the police when the murderers are invisible to everyone else and when there is nothing—not even a smear of blood—to show that a boy has died. Or was he a boy?\nThis is Clary's first meeting with the Shadowhunters, warriors dedicated to ridding the earth of demons. It's also her first encounter with Jace, a Shadowhunter who looks a little like an angel and acts a lot like a jerk. Within twenty-four hours Clary is pulled into Jace's world with a vengeance, when her mother disappears and Clary herself is attacked by a demon. But why would demons be interested in ordinary mundanes like Clary and her mother? And how did Clary suddenly get the Sight? The Shadowhunters would like to know...""", "Fantasy|Young Adult|Romance|Paranormal|Urban Fantasy|Fiction|Vampires|Supernatural|Magic", 2007, 485, 4.06),
        ("Twilight", "Stephenie Meyer", """About three things I was absolutely positive.\nFirst, Edward was a vampire.\nSecond, there was a part of him - and I didn't know how dominant that part might be - that thirsted for my blood.\nAnd third, I was unconditionally and irrevocably in love with him.""", "Fantasy|Young Adult|Romance|Fiction|Vampires|Paranormal|Supernatural|Urban Fantasy", 2005, 498, 3.68),
        ("Astarion: Baldur's Gate 3", "T. Kingfisher", """You're too pretty to die.\nAstarion Ancunin was supposed to be a magistrate, not a vampire spawn. He was supposed to serve the law, not the vicious vampire lord Cazador Szarr. And he was supposed to drink fine wine, not rat blood. Alas—the city of Baldur's Gate cares little for what's supposed to happen.\nThough he has been powerless to resist his master's bidding, haunting the nighttime streets to fetch warm blood, Astarion has never surrendered his hope. One day, this nightmare must end. He just has to find out how.\nWhen the vampire lord announces a twisted competition for his favor, an opportunity presents itself in the form of a rare prize . . . and an unlikely alliance. The blood of a dead god is buried deep beneath Baldur's Gate, and, to get it, Astarion will need the help of a handsome Aasimar paladin named Hahn den Suriel.\nThere are just a few problems. Astarion is not supposed to trust his fellow spawn. He's not supposed to go out into the city for his own ends rather than the vampire lord's. And he's certainly not supposed to strike a deal with a stranger whose golden eyes can snare even a blackened, undead heart.\nBut the city of Baldur's Gate cares little for what's supposed to happen.""", "Fantasy|Vampires|Horror|Adult|Fiction|Queer|High Fantasy|Romance", 2026, 272, 2.91),
        ("Challenger: A True Story of Heroism and Disaster on the Edge of Space", "Adam Higginbotham", """On January 28, 1986, just seventy-three seconds into flight, the space shuttle Challenger broke apart over the Atlantic Ocean, killing all seven people on board. Millions of Americans witnessed the tragic deaths of a crew including New Hampshire schoolteacher Christa McAuliffe. Like 9/11 or JFK's assassination, the Challenger disaster is a defining moment in 20th-century history—yet the details of what took place that day, and why, have largely been forgotten. Until now.\nBased on extensive archival records and meticulous, original reporting, Challenger follows a handful of central protagonists—including each of the seven members of the doomed crew—through the years leading up to the accident, a detailed account of the tragedy itself, and into the investigation that followed. It's a tale of optimism and promise undermined by political cynicism and cost-cutting in the interests of burnishing national prestige; of hubris and heroism; and of an investigation driven by leakers and whistleblowers determined to bring the truth to light. Throughout, there are the ominous warning signs of a tragedy to come, recognized but then ignored, and ultimately kept from the public.\nHigginbotham reveals the history of the shuttle program, the lives of men and women whose stories have been overshadowed by the disaster as well as the designers, engineers, and test pilots who struggled against the odds to get the first shuttle into space.""", "Nonfiction|History|Science|Space|Politics|Biography", 2024, 563, 4.50),
        ("All the Beauty in the World: The Metropolitan Museum of Art and Me", "Patrick Bringley", """Millions of people climb the grand marble staircase to visit the Metropolitan Museum of Art every year. But only a select few have unrestricted access to every nook and cranny. They're the guards who roam unobtrusively in dark blue suits, keeping a watchful eye on the two million square foot treasure house. Caught up in his glamorous fledgling career at The New Yorker, Patrick Bringley never thought he'd be one of them. Then his older brother was diagnosed with fatal cancer and he found himself needing to escape the mundane clamor of daily life. So he quit The New Yorker and sought solace in the most beautiful place he knew.\nTo his surprise and the reader's delight, this temporary refuge becomes Bringley's home away from home for a decade. We follow him as he guards delicate treasures from Egypt to Rome, strolls the labyrinths beneath the galleries, wears out nine pairs of company shoes, and marvels at the beautiful works in his care. Bringley enters the museum as a ghost, silent and almost invisible, but soon finds his voice and his tribe: the artworks and their creators and the lively subculture of museum guards—a gorgeous mosaic of artists, musicians, blue-collar stalwarts, immigrants, cutups, and dreamers. As his bonds with his colleagues and the art grow, he comes to understand how fortunate he is to be walled off in this little world, and how much it resembles the best aspects of the larger world to which he gradually, gratefully returns.""", "Nonfiction|Memoir|Art|Biography|History", 2023, 240, 4.01),
        ("Project Hail Mary", "Andy Weir", """Ryland Grace is the sole survivor on a desperate, last-chance mission—and if he fails, humanity and the earth itself will perish.\nExcept that right now, he doesn't know that. He can't even remember his own name, let alone the nature of his assignment or how to complete it.\nAll he knows is that he's been asleep for a very, very long time. And he's just been awakened to find himself millions of miles from home, with nothing but two corpses for company.\nHis crewmates dead, his memories fuzzily returning, Ryland realizes that an impossible task now confronts him. Hurtling through space on this tiny ship, it's up to him to puzzle out an impossible scientific mystery—and conquer an extinction-level threat to our species.\nAnd with the clock ticking down and the nearest human being light-years away, he's got to do it all alone.\nOr does he?""", "Science Fiction|Fiction|Fantasy|Space|Thriller|Adult", 2021, 476, 4.51),
        ("Pride and Predjudice", "Jane Austen", """Sisters and Sweethearts!\nJane and Elizabeth Bennet are not only sisters, but best friends. They share all their hopes and dreams. When Jane falls in love, Elizabeth is thrilled for her. But Jane's dream falls apart, and Elizabeth knows just who to blame —proud and handsome Darcy, the very man Elizabeth finds herself both loving and hating at the same time!""", "Classics|Romance|Fiction|Historical Fiction|Enemies To Lovers", 1813, 350, 4.38),
        ("The Pit: A Story of Chicago", "Frank Norris", """In "The Octopus" (1901), one of the earliest muckraking novels of the Progressive Era, Frank Norris exposed the operations of the ruthless, "laissez-faire" capitalism sanctioned by turn-of-the-century Social Darwinists. "The Pit" (1903), the second novel in Norris's projected trilogy, continues the "Epic of the Wheat" with the story of Curtis Jadwin, a speculator bent on cornering the wheat market, and his brutally abused wife, Laura. Mingling realism and romanticism, Norris created in Laura a heroine whose psychological complexity rivals that of Flaubert's Madame Bovary or Edna Pontellier in Kate Chopin's "The Awakening." Edited for the first time as Norris intended it, this masterpiece of American literary naturalism is fully contextualized in the introduction and explanatory notes by Joseph R. McElrath, Jr. and Gwendolyn Jones.""", "Fiction|Classics|Historical Fiction|Finance", 1903, 244, 3.74),
    ]
    

    # checks if there's data in catalog
    res = cur.execute("SELECT * FROM catalog")
    if (res.fetchall() == []):
        # if the table is empty, add starting data
        cur.executemany("""INSERT INTO catalog VALUES(?, ?, ?, ?, ?, ?, ?)
                        ON CONFLICT(title, author, description, genres, year, length, rating) DO NOTHING""", data)
        con.commit()

    # Creates and initializes choice
    choice = -1;

    # Menu
    while (choice != 0):
        print("\nWelcome to the Library Catalog! What would you like to do?\n0. Quit\n1. Find book(s)\n2. Filter books (coming soon)\n3. Modify/update book data\n4. Add book\n5. Delete book\n6. Show stats")
        choice = int(input("Your choice: "))
        if (choice == 0):
            return
        elif (choice == 1):
            # Asks if the user wants to search by the author or title
            print("\nWhat would you like to search?\n1. Author\n2. Title")
            find_option = int(input("Your choice: "))
            if (find_option == 1):
                # gets the author's name and queries catalog with it
                find_author = input("Author: ")
                cur.execute("SELECT * FROM catalog WHERE author=?", (find_author,))
                # saves the result in books, then calls print_book_data() on it
                books = cur.fetchall()
                print_book_data(books)
            elif (find_option == 2):
                # gets the title and queries catalog with it
                find_title = input("Title: ")
                cur.execute("SELECT * FROM catalog WHERE title=?", (find_title,))
                # saves the result in books, then calls print_book_data() on it
                books = cur.fetchall()
                print_book_data(books)
            else:
                print("Not a valid option")
        elif (choice == 2):
            # prints a coming soon message
            print("\nThis feature coming soon! (Theoretically. Idk, that might be a lie)")
            time.sleep(1)
        elif (choice == 3):
            # asks which book the user wants to update
            title = input("\nWhat's the title of the book you want to update? ")
            author = input("Who's the author of the book? ")
            # asks what the user what's to update
            print("Do you want to modify the:\n1. Title\n2. Author\n3.Description\n4. Genres\n5. Year published\n6. Page count\n7. Rating")
            update_choice = int(input("Your choice: "))
            # chooses what to update
            if (update_choice == 1):
                # updates title
                update = input("What do you want the new title to be? ")
                cur.execute("UPDATE OR IGNORE catalog SET title=? WHERE title=? AND author=?", (update, title, author))
                con.commit()
            elif (update_choice == 2):
                # updates author
                update = input("What do you want the new author to be? ")
                cur.execute("UPDATE OR IGNORE catalog SET author=? WHERE title=? AND author=?", (update, title, author))
                con.commit()
            elif (update_choice == 3):
                # updates description
                update = input("What do you want the new description to be? ")
                cur.execute("UPDATE OR IGNORE catalog SET description=? WHERE title=? AND author=?", (update, title, author))
                con.commit()
            elif (update_choice == 4):
                # updates genres
                update = input("What do you want the new genres to be? (enter in Genre|Genre|... format) ")
                cur.execute("UPDATE OR IGNORE catalog SET genre=? WHERE title=? AND author=?", (update, title, author))
                con.commit()
            elif (update_choice == 5):
                # updates year
                update = int(input("What do you want the new year to be? "))
                cur.execute("UPDATE OR IGNORE catalog SET year=? WHERE title=? AND author=?", (update, title, author))
                con.commit()
            elif (update_choice == 6):
                # updates length
                update = int(input("What do you want the new page count to be? "))
                cur.execute("UPDATE OR IGNORE catalog SET length=? WHERE title=? AND author=?", (update, title, author))
                con.commit()
            elif (update_choice == 7):
                # updates rating
                update = float(input("What do you want the new rating to be? "))
                cur.execute("UPDATE OR IGNORE catalog SET rating=? WHERE title=? AND author=?", (update, title, author))
                con.commit()
            else:
                print("Not a valid option")
        elif (choice == 4):
            # asks the user for the book's information
            title = input("\nWhat's the title? ")
            author = input("Who's the author of the book? ")
            description = input("What's the description? ")
            genres = input("What are the genres? (enter in Genre|Genre|... format) ")
            year = int(input("What year was it published? "))
            length = int(input("What is its page count? "))
            rating = float(input("What is the rating out of five stars? "))
            # add to catalog if it's not a repeat
            cur.execute("""INSERT INTO catalog VALUES(?, ?, ?, ?, ?, ?, ?) 
                ON CONFLICT(title, author, description, genres, year, length, rating) DO NOTHING""", (title, author, description, genres, year, length, rating))
            con.commit()
        elif (choice == 5):
            # asks for the title and author of the book to delete
            title = input("\nWhat's the title of the book you want to delete? ")
            author = input("Who's the author of the book? ")
            # deletes the book
            cur.execute("DELETE FROM catalog WHERE title=? AND author=?", (title, author))
            con.commit()
        elif (choice == 6):
            stat_choice = -1
            while (stat_choice != 0):
                # asks which stats the user wants to see in a loop
                print("\nWhat stats do you want to look at?\n0. None\n1. Averages\n2. Total books\n3. Minimum and maximums\n4. Total page count")
                stat_choice = int(input("Your choice: "))
                if (stat_choice == 0):
                    break
                elif (stat_choice == 1):
                    # prints average rating
                    res = cur.execute("SELECT AVG(rating) FROM catalog")
                    rating_average = res.fetchone()[0]
                    print(f"Average rating: {rating_average:.1f}")
                    time.sleep(1)
                    # prints average length
                    res = cur.execute("SELECT AVG(length) FROM catalog")
                    length_average = res.fetchone()[0]
                    print(f"Average length: {length_average:.0f} pages")
                    time.sleep(1)
                    # average year
                    res = cur.execute("SELECT AVG(year) FROM catalog")
                    year_average = res.fetchone()[0]
                    print(f"Average published year: {year_average:.0f}")
                    time.sleep(1)
                elif (stat_choice == 2):
                    # prints the number of total books in catalog
                    res = cur.execute("SELECT COUNT(*) FROM catalog")
                    print("Total books in the catalog:", res.fetchone()[0])
                    time.sleep(1)
                elif (stat_choice == 3):
                    # prints the min and max rating
                    res = cur.execute("""SELECT title, rating FROM catalog ORDER BY rating DESC LIMIT 1""")
                    max_book = res.fetchone()
                    print("Max rating:", max_book[1], " - ", max_book[0])
                    time.sleep(1)
                    res = cur.execute("""SELECT title, rating FROM catalog ORDER BY rating ASC LIMIT 1""")
                    min_book = res.fetchone()
                    print("Min rating:", min_book[1], " - ", min_book[0])
                    time.sleep(1)
                    # prints the min and max length
                    res = cur.execute("""SELECT title, length FROM catalog ORDER BY length DESC LIMIT 1""")
                    max_book = res.fetchone()
                    print("Max page count:", max_book[1], " - ", max_book[0])
                    time.sleep(1)
                    res = cur.execute("""SELECT title, length FROM catalog ORDER BY length ASC LIMIT 1""")
                    min_book = res.fetchone()
                    print("Min page count:", min_book[1], " - ", min_book[0])
                    time.sleep(1)
                    # prints the min and max of year
                    res = cur.execute("""SELECT title, year FROM catalog ORDER BY year DESC LIMIT 1""")
                    max_book = res.fetchone()
                    print("Max year published:", max_book[1], " - ", max_book[0])
                    time.sleep(1)
                    res = cur.execute("""SELECT title, year FROM catalog ORDER BY year ASC LIMIT 1""")
                    min_book = res.fetchone()
                    print("Min year published:", min_book[1], " - ", min_book[0])
                    time.sleep(1)
                elif (stat_choice == 4):
                    # prints the combined length
                    res = cur.execute("SELECT SUM(length) FROM catalog")
                    print("Total page count:", res.fetchone()[0])
                    time.sleep(1)
                else:
                    print("Not a valid option")
        else:
            print("Not a valid option")

if __name__ == "__main__":
    main()

# genres = stored.split("|")