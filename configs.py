# (c) @KGN_OFFICIAL

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 12336818))
    API_HASH = os.environ.get("API_HASH", "de4c34807c8963ba9418e01c7cc15c4c")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -100)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/Mdisk_Links_Sender_Bot>Mdisk_Links_Sender_Bot</a>

📝 Language: <a href='https://www.python.org'> Python V3 </a>

📚 Library: <a href='https://docs.pyrogram.org'> Pirogram </a>

📡 Server: <a href='https://heroku.com'> Heroku+Github </a>

👨‍💻 Created By: <a href='https://t.me/Z_Harbour_bot'> Z_Harbour_bot </a> </b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer: <a href='https://t.me/Z_Harbour_bot'> Z_Harbour_bot </a> </b>

<u>If You Want Bot Source Code Purchase It From The Developer.</b> </u>
"""

    HOME_TEXT = """

<b>Hello {} Dear🥰,

<a>I'm Mdisk Search Robo😛</a>

I Can Search Any Stuff!🔍 What do You Want?Just Drop A Name!☺️

<a>Co-devloper @Z_Harbour_bot🌷</a></b>
"""


    START_MSG = """
<b>Hello Dear {}☺️,

<a>I'm Mdisk Search Robo</a>

<i> I Can Search Any Mobi-Seriez-Showz! And Can Provide You Direct Mdisk Links! If Found On My Database:) </i>

<a> If You Didn't Find Your Query Then Please Request in D.M_ing My Father👨‍👦@Z_Harbour_bot❤😊 </a></b>
"""


