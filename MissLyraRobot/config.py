# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "7262250"  
    API_HASH = "07a185a62d8a3d127164197475533c4a"
    TOKEN = "5528054140:AAGYclMKyb86cFJ0dKiaMEJyD8JE2cqezDE"
    OWNER_ID = "5353614138"
    OWNER_USERNAME = "itz_xoxo"
    MONGO_DB_URI = "mongodb+srv://bot:bot@cluster0.febee.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    MONGO_DB = "MissLyraRobot"
    SUPPORT_CHAT = "ttest_me"
    JOIN_LOGGER = "-1001736567149"
    EVENT_LOGS = "-1001736567149"
    ERROR_LOG = "-1001736567149"

    # RECOMMENDED
    INFOPIC = "https://telegra.ph/file/dac56ba4d9f84aff89a6c.jpg"   
    CF_API_KEY = ""
    LASTFM_API_KEY = ""
    BOT_USERNAME = "Diva1bot"
    WALL_API = ""
    OPENWEATHERMAP_ID = ""
    TEMP_DOWNLOAD_DIRECTORY = ""
    REM_BG_API_KEY = ""
    TIME_API_KEY = ""
    CASH_API_KEY = ""
    REM_BG_API_KEY = ""
    ARQ_API_KEY = "ASIOAB-SAODKO-MLCITA-XOSMGD-ARQ"
    ARQ_API = "ASIOAB-SAODKO-MLCITA-XOSMGD-ARQ"
    ARQ_API_URL = "aww"
    HEROKU_APP_NAME = ""
    HEROKU_API_KEY = "24a86373-653c-446d-99ac-826ae6973c36"
    BOT_ID = "5528054140"
    STRING_SESSION = "1BVtsOHoBu5Jj5mHdqyudrBd3lnHF2imbCXyTn-mfu6fjHdmsBUITHPvlnFK1GCHFFVQQ0llKRlvNFJ6A1jQcM3iMhlfXHPtv9D2iFWY979wfRa3FGpHdD4RcP2FSlnp86EjpK2AcoGdfhty7sOjmvWHWvWMIaUbSV97dfxlnm8xgYHJXT-KUSHvvOxSuS_QbnQXRMK1cvHIRU8hqUzF0Pp3lTAXz-gjF-N2XzekQXJG13rNgxErsceYn0tOdkeHvZTlLKoOfrpXguB9Swml_1DytCC-FOUsySl0gsXu-j4Jl8MAl8f7iZCwsJ0MUcb_9OU25UDAAiOR55Kvz26azuAq72PKUCUE="
    SESSION_STRING = "1BVtsOHoBu5Jj5mHdqyudrBd3lnHF2imbCXyTn-mfu6fjHdmsBUITHPvlnFK1GCHFFVQQ0llKRlvNFJ6A1jQcM3iMhlfXHPtv9D2iFWY979wfRa3FGpHdD4RcP2FSlnp86EjpK2AcoGdfhty7sOjmvWHWvWMIaUbSV97dfxlnm8xgYHJXT-KUSHvvOxSuS_QbnQXRMK1cvHIRU8hqUzF0Pp3lTAXz-gjF-N2XzekQXJG13rNgxErsceYn0tOdkeHvZTlLKoOfrpXguB9Swml_1DytCC-FOUsySl0gsXu-j4Jl8MAl8f7iZCwsJ0MUcb_9OU25UDAAiOR55Kvz26azuAq72PKUCUE="
    SQLALCHEMY_DATABASE_URI = "postgres://xkncmhpw:9f1Z_dF2OMcgWejkDDsJuaPq4MdkSu5u@lallah.db.elephantsql.com/xkncmhpw"
    DATABASE_URL = "postgres://xkncmhpw:9f1Z_dF2OMcgWejkDDsJuaPq4MdkSu5u@lallah.db.elephantsql.com/xkncmhpw"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = "1844469309"
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = "1844469309"
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = "1844469309"
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = "1844469309"
    WOLVES = "1844469309"
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    ALLOW_CHATS = True
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "awoo"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
