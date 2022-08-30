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
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL",)
    ABOUT_BOT_TEXT = """<b>This is Mdisk Search Bot.

🤖<i> My Name</i>: <a href='https://t.me/Mdisk_Links_Sender_Bot>Mdisk_Links_Sender_Bot</a>

📝<i> Language </i> : <a href='https://www.python.org'> Python V3</a>

📚<i> Library</i>: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡<i> Server</i>: <a href='https://heroku.com'>Heroku</a>

👨‍💻<i> Created By</i>: <a href='https://t.me/Z_Harbour_bot'>sigma_male007</a> </b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Developer<i></u>: <a href='https://t.me/Z_Harbour_bot'> sigma_male007 </u></i></a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer @Z_Harbour_bot </b>
"""

    HOME_TEXT = """
<b>Hello {} Darling 🥰,

I'm Mdisk Search Robo😛</a>

I Can Search Any Stuff!🔍 What do You Want?Just Drop A Name!☺️

<a>Co-devloper @Z_Harbour_bot🌷</a></b>
"""


    START_MSG = """
<b>Hello Dear {}😍,

I'm Mdisk Search Robo</a>

I Can Search Any Mobi-Series-Shows! And Can Provide You Direct Mdisk Links! 

<a>Myh Father @sigma_male007❤ </a></b>
"""


