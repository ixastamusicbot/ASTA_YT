import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_USERNAME = getenv("OWNER_USERNAME", "zxasta")
BOT_USERNAME = getenv("BOT_USERNAME", "radha_music_bot")
BOT_NAME = getenv("BOT_NAME", "˹ʀᴧᴅʜᴧ ꭙ ᴍᴜꜱɪᴄ˼ ♪")
ASSUSERNAME = getenv("ASSUSERNAME", "VILLAIN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", -1002029289902))
OWNER_ID = int(getenv("OWNER_ID", 5909658683))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ✅ FIXED API (returns {"status":"running"})
API_URL = getenv("API_URL", "https://api.nexgenbots.xyz")
VIDEO_API_URL = getenv("VIDEO_API_URL", "https://api.video.thequickearn.xyz")
API_KEY = getenv("API_KEY", "NxGBNexGenBotsee4f86")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/ITzastamusic/LAIBA_MUSIC"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN")

PRIVACY_LINK = getenv(
    "PRIVACY_LINK",
    "https://telegra.ph/Privacy-Policy-for-YukkiMusic-08-30"
)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ixasta1")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/odsnetwork")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET")

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")
STRING6 = getenv("STRING_SESSION6")
STRING7 = getenv("STRING_SESSION7")

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

START_IMG_URL = getenv("START_IMG_URL", "https://files.catbox.moe/fu6jk3.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/26nzoq.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/f2s4ws.jpg"
STATS_IMG_URL = "https://files.catbox.moe/z0gh23.jpg"

TELEGRAM_AUDIO_URL = "https://files.catbox.moe/2y5o3g.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/2y5o3g.jpg"

STREAM_IMG_URL = "https://telegra.ph/file/d30d11c4365c025c25e3e.jpg"
SOUNCLOUD_IMG_URL = STREAM_IMG_URL
YOUTUBE_IMG_URL = TELEGRAM_AUDIO_URL

SPOTIFY_ARTIST_IMG_URL = TELEGRAM_AUDIO_URL
SPOTIFY_ALBUM_IMG_URL = TELEGRAM_AUDIO_URL
SPOTIFY_PLAYLIST_IMG_URL = STREAM_IMG_URL


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60 ** i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit(
        "[ERROR] - SUPPORT_CHANNEL must start with https://"
    )

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit(
        "[ERROR] - SUPPORT_CHAT must start with https://"
    )
