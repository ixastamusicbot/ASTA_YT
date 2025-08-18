from ASTA_YT.core.bot import ASTA
from ASTA_YT.core.dir import dirr
from ASTA_YT.core.git import git
from ASTA_YT.core.userbot import Userbot
from ASTA_YT.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ASTA()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
