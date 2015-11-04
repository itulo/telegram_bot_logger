Python version: 2.7

BOT
The bot uses pyTelegramBotAPI (https://github.com/eternnoir/pyTelegramBotAPI)
Run:
python bot.py channel_name

Notes:
- The bot's name is @italo_bot, it should be added to whatever channel you want to monitor.
- To simplify things for me, the bot stores only the user's first name in the database

REST API
The rest api uses web.py (http://webpy.org/)
Run:
python rest.py

Endpoints:
/discussion		accepts params user, text and date
/discussion/:id

DATABASE:
Database is in discussions.db and it's sqlite
Table definition:
CREATE TABLE discussions (channel TEXT, user TEXT, text TEXT, date TEXT);

ANSWERS
A) I believe the solutions are correct, requirements (1 and 2) have been addressed. In addition, I have used a variant of the BCE framework: without B because there is no UI, and with a D (database) for classes that access the database. BCE is known among engineers and it gives a structure to abide to when adding new features.
However, I would like to know your opinion.

B) What I would do if I had more time:
- add unit tests
- implement users and channel entities classes, database classes and tables
- use another dbms that has a datetime datatype
- error handling
- use a python framework lika django (and spare myself the implementation of more database classes)