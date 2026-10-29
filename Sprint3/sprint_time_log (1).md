# CSE 310 - Sprint Time Log

Name: Luce DeWitt

Sprint #: 3

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
| 10/19/26 | 10:15    |MTG & IM| Planning meeting                           | 60          |
| 10/20/16 | 4:07     |   IM   | Created plan, set up, tutorial, readme     | 60          |
| 10/21/26 | 10:20    |   TP   | Merged branches, completed transactions.tsx| 60          |
| 10/21/26 | 5:04     |   IM   | Tutorial                                   | 60          |
| 10/22/26 | 4:16     |   IM   | Tutorial, experimentation                  | 60          |
| 10/23/26 | 10:17    |MTG & TP| Stand up meeting, backend setup            | 6/71        |
| 10/26/26 | 10:23    |   TP   | Updating Expo, Budget screen, presentation | 59          |
| 10/26/26 | 4:35     |   IM   | Experimentation, learning, planning        | 60          |
| 10/27/26 | 5:50     |   IM   | Learning (aggregate, views, updating)      | 39          |
| 10/27/26 | 6:55     |   IM   | Updating, deleting                         | 25          |
| 10/28/26 | 10:19    |TP & MTG| Team presentations                         | 58          |
| 10/28/26 | 8:26     |   IM   | Created database, table data               |             |
|          |          |        |                                            |             |
|          |          |        |                                            |             |
|          |          |        |                                            |             |

_Note: Add more rows as needed._

## Sprint Totals

|Categroy                       |Total Time (Hours:Minutes)|
|-------------------------------|:------------------------:|
|IM - Individual Module         | 6h 4m                    |
|TP - Team Project              | 4h 8m                    |
|MTG - Class Meetings           | 2h 4m                    |
|**TOTAL**                      |                          |


<br>
<br>
<br>
<br>


## Personal Notes (ignore)
<span style="color: #F12B76">Requirements</span>
- Create a SQL database with at least one table (your software can create the table or you can use already existing table)
- Software should query data from the database
- Software should add new data to the database
- Software should update data from the database
- Software should delete data from the database

<span style="color: #FFE338">Stretch challenge</span>
- Use at least two of the aggregate functions to summarize numerical data in your database
(https://www.sqlitetutorial.net/sqlite-aggregate-functions/)

<span style="color: #F12B76">Idea: </span>
a library catalog. It should let the user search for, update?, delete, and add books. (If there's time, function fully with tracking borrowing records)
- Column ideas: name, author, description, genre, tags, year, length (pages), <span style="color: #FFE338">rating?</span> (rating could update it? or just have that as a seperate thing, might be weird)
- Extra column ideas: number of times checked out, date checked out, checked out status, number of copies, type (book vs ebook)

<span style="color: #3794FF">Doing:</span>
More tutorial (finished star source mini tutorial) <span style="color: #62F40C">✓</span>
Question at bottom of tutorial.py <span style="color: #62F40C">✓</span>
Experimentation (label) in tutorial.py. Currently has errors (why?) <span style="color: #62F40C">✓</span>
-What do I need to know? Search, filtering (just show? or save as a different group?), <span style="color: #62F40C">✓</span> add, tags? (Lists?), aggregate functions <span style="color: #62F40C">✓</span>
What are aggregate functions? <span style="color: #62F40C">✓</span>
How to update data?

<span style="color: #3794FF">Notes:</span>
- use execute() with single operations, and executemany() with multiple (like insert, update, delete)
- call con.commit() after operations that change data or structure (INSERT, UPDATE, DELETE, CREATE TABLE, DROP TABLE, CREATE VIEW, DROP VIEW) (SELECT is read only and doesn't need it)