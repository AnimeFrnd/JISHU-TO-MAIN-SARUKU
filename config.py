import os
import logging
from logging.handlers import RotatingFileHandler

def get_int_env(var_name, default):
    try:
        return int(os.environ.get(var_name, default))
    except ValueError:
        return default  # Fallback to default if conversion fails

def str_to_bool(value):
    return str(value).lower() in ("true", "1", "yes")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = get_int_env("API_ID", 7515868)
API_HASH = os.environ.get("API_HASH", "")

OWNER_ID = get_int_env("OWNER_ID", 6081617163)
DB_URL = os.environ.get("DB_URL", "mongodb+srv://bestanimeandcartoonsclips:VrMTuRFUEZdKsoV7@cluster0.ayqz3o3.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "aryabro")

CHANNEL_ID = get_int_env("CHANNEL_ID", -1002292066966)
FORCE_SUB_CHANNEL = get_int_env("FORCE_SUB_CHANNEL", -1002233627155)
FORCE_SUB_CHANNEL2 = get_int_env("FORCE_SUB_CHANNEL2", -1002216108152)
FORCE_SUB_CHANNEL3 = get_int_env("FORCE_SUB_CHANNEL3", -1002093762218)
FORCE_SUB_CHANNEL4 = get_int_env("FORCE_SUB_CHANNEL4", -1002430646198)

FILE_AUTO_DELETE = get_int_env("FILE_AUTO_DELETE", 86400)  # Auto delete in seconds
PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = get_int_env("TG_BOT_WORKERS", 6)

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/dc14717927ef75bdee500-7ba298be2fcf353255.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/dc14717927ef75bdee500-7ba298be2fcf353255.jpg")

# Proper handling of admins
ADMINS = {6081617163}  # Use a set to avoid duplicates
env_admins = os.environ.get("ADMINS", "6081617163").split()
ADMINS.update(int(x) for x in env_admins if x.isdigit())  # Ensuring only valid numbers
ADMINS.add(OWNER_ID)  # Ensuring OWNER_ID is in ADMINS
ADMINS = list(ADMINS)  # Convert back to list for compatibility

CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = str_to_bool(os.environ.get('PROTECT_CONTENT', "False"))
DISABLE_CHANNEL_BUTTON = str_to_bool(os.environ.get('DISABLE_CHANNEL_BUTTON', "True"))

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"

USER_REPLY_TEXT = "</b>❌సారీ మావా నువ్వు నా ᴏᴡɴᴇʀ కాదు..!😜\n\n❌Don't Send Me Messages Directly I'm Only File Share Bot ! \n\n 𝐉𝐨𝐢𝐧 𝐍𝐨𝐰 🌚 ➥ 「<a href='https://t.me/TELUGU_SARUKU_BITLU'>𝙏𝙀𝙇𝙐𝙂𝙐 𝙎𝘼𝙍𝙐𝙆𝙐 𝘽𝙄𝙏𝙇𝙐 🥵</a>」</b>"

START_MSG = os.environ.get("START_MESSAGE", "<b><blockquote>Orey!! {first}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ! \n\n 𝐉𝐨𝐢𝐧 𝐍𝐨𝐰 🌚 ➥ 「<a href='https://t.me/TELUGU_SARUKU_BITLU'>𝙏𝙀𝙇𝙐𝙂𝙐 𝙎𝘼𝙍𝙐𝙆𝙐 𝘽𝙄𝙏𝙇𝙐 🥵</a>」</b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE",
                           "Hello {mention}\n\n<b>ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ. \n\n కింద ఇచ్చిన 4 చానెల్స్ లో జాయిన్ అయ్యి తరవాత Try Again క్లిక్ చేస్తే File📁 వస్తది..:) 🥰</b>")

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
