# Intro
In this codebase I implement a Telegram bot that logs disussions from a channel/group to a database, and a rest api that allows to get such discussions with filtering on user, text, and date

# Technical Details
I use a variant of the BCE framework here. There is no UI, so there is no B level. However I have added a D level for classe accessing a database.

Python version used is 2.7

## Bot
The bot uses [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)

Run:
```
python bot.py channel_name
```

### Notes
* The bot's name is @italo_bot, it should be added to whatever channel you want to monitor (if you create your own bot, talk to the BotFather to change its privacy settings - by default it will not listen to all messages in a channel)
* To make things simple the bot stores only the user's first name in the database

## Rest Api
The rest api uses [web.py](http://webpy.org/)

Run:
```
python rest.py
```
Try open your browser at [http://localhost:8080/discussion?user=italo](http://localhost:8080/discussion?user=italo)

### Endpoints
* /discussion (accepts parameters user, text and date)
* /discussion/:id

## DATABASE
Database is in discussions.db and it's SQLite

### Table definition
CREATE TABLE discussions (channel TEXT, user TEXT, text TEXT, date TEXT);

