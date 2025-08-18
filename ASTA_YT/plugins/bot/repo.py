from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from ASTA_YT import app
from config import BOT_USERNAME
from ASTA_YT.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ˹ ᴀsᴛᴀ-ᴍᴜsɪᴄ ˼ ʙᴏᴛ ✪
 
 ❍ • ʙsᴅᴋ ʀᴇᴘᴏ ʟᴇɢᴀ ◉‿◉ •
 
 ❍ • ᴘᴇʜʟᴇ ᴀsᴛᴀ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ •
 
 ❍ • ᴄʜᴜᴘ ᴄʜᴀᴘ ʙᴏᴛ ʟᴇᴋᴇ ɴɪᴋᴀʟ •
 
 ❍ • ʀᴇᴘᴏ ᴛᴏ ɴᴀʜɪ ᴍɪʟᴇɢᴀ ʙᴇᴛᴀ ⊂◉‿◉ •
 
 ❍ • ᴀɢʀ ʀᴇᴘᴏ ᴄʜᴀʜɪʏᴇ ᴛᴏ ᴀsᴛᴀ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟɴᴀ ᴘᴀᴅᴇɢᴀ •
 
 ❍ • ᴀsᴛᴀ ᴘᴀᴘᴀ • **"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("•ᴀᴅᴅ ᴍᴇ•", url=f"https://t.me/Laibaamusicbot?start=_tgr_wnBXNLAzMGM1")
        ],
        [
          InlineKeyboardButton("•sᴜᴘᴘᴏʀᴛ•", url="https://t.me/oldskoolgc"),
          InlineKeyboardButton("•ᴏᴡɴᴇʀ•", url="https://t.me/ixasta"),
        ],
        [
          InlineKeyboardButton("•ᴜᴘᴅᴀᴛᴇs•", url="https://t.me/ixasta1"),
        ],
        [
          InlineKeyboardButton("˹ʟᴧɪʙᴧ ꭙ ϻᴜsɪᴄ˼", url=f"https://t.me/Laibaamusicbot"),
          InlineKeyboardButton("˹sσᴜϻʏᴧ ꭙ ϻᴜsɪᴄ˼ ♪", url=f"https://t.me/soumyamusicrobot"),
        ],
        [
          InlineKeyboardButton("˹ʀᴧᴅʜɪᴋᴧ ꭙ ϻᴜsɪᴄ˼", url=f"https://t.me/radhikaamusicbot"),
          InlineKeyboardButton("˹ᴧᴧʏʀᴧ ꭙ ᴍᴜsɪᴄ˼", url=f"https://t.me/aayramusicbot"),
        ],
        [
          InlineKeyboardButton("˹ᴠᴧʀsʜᴧ ꭙ ϻᴜsɪᴄ˼", url=f"https://t.me/varshaamusicbot"),
          InlineKeyboardButton("Ҩ፝֟፝ɴ┋ꕶʜɪᴢ֟፝ᴜᴋᴀ ♡", url=f"https://t.me/Shizuka_Chat_Robot"),
        ],
        [
          InlineKeyboardButton("•ᴏʟᴅ ꜱᴋᴏᴏʟ ɢᴄ•", url=f"https://t.me/oldskoolgc"),
          InlineKeyboardButton("˹ᴀsᴛᴀ ꭙ ꜱᴜᴘᴘᴏʀᴛ˼", url=f"https://t.me/ixasta1"),
        ],
        [
          InlineKeyboardButton("ᴀʟʟ ʙᴏᴛ", url=f"https://t.me/ixasta1/69"),
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/l1yzh0.jpg",
        caption="✨ ʀᴇᴘᴏ ʙᴜᴛᴛᴏɴꜱ ✨",
        reply_markup=reply_markup
    )
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/l1yzh0.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/BABY-MUSIC/BABASTAUNE/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[•ʙᴏᴛ-ᴏᴡɴᴇʀ•](https://t.me/ixasta) | [•ᴜᴘᴅᴀᴛᴇs•](https://t.me/ixasta1)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
