# (c) @KGN_OFFICIAL

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 9323694))
    API_HASH = os.environ.get("API_HASH", "34a0b2551aacd866c3729f7044525353")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -100))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -1001557431626)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖 My Name: <a href='https://t.me/Mdisk_Links_Sender_Bot>Mdisk_Links_Sender_Bot</a>

📝 Language: <a href='https://www.python.org'> Python V3 </a>

📚 Library: <a href='https://docs.pyrogram.org'> Pirogram </a>

📡 Server: <a href='https://heroku.com'> Heroku/Github </a>

👨‍💻 Developed By: <a href='https://t.me/Z_Harbour_bot'> Z_Harbour_bot </a> 
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer: Anonymous </b>

<u> Source Code Is Private For Privacy</b> </u>
"""

    HOME_TEXT = """

<b>Hello Dear {} 😘

<a>I'm Mdisk Search Robo</a>

I Can Search Any Stuff!🔍 What do You Want?Just Drop A Name!☺️

"""


    START_MSG = """
<b>Hello Dear {} 😘

<a>I'm Mdisk Search Robo</a></b>

<i> I Can Search Any Mobi-Seriez-Showz! And Can Provide You Direct Mdisk Links! If Found On My Database:) </i>

<a> If You Didn't Find Your Query Then Please Request on @blackest_harbour❤😊 </a>
"""


