from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = (
                "<b><blockquote>❃ 💓 ᴏᴡɴᴇʀ (ᴀʀʏᴀ) : <a href='https://t.me/Arya_Bro'>ᴀʀʏᴀ ʙʀᴏ❤‍🔥</a>\n"
            "❃ 🫡ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href='https://t.me/Telugu_Saruku_Bitlu'>ᴛᴇʟᴜɢᴜ sᴀʀᴜᴋᴜ ʙɪᴛʟᴜ 🥵</a>\n"
            "❃ 🥵 ʟ€@ᴋ$: <a href='https://t.me/+4QSB2tPk-ME2NDdl'>ᴄʟɢ ɢɪʀʟ ᴀɴᴅ ʟᴜᴠʀs 😛</a>\n"
            "❃ 🔞 ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/+aph6xGmeXgU2NzFl'>ᴀᴅᴜʟᴛ ᴍᴏᴠɪᴇs 🤤</a>\n"
            "❃ 🌝 ɪɴsᴛᴀ ʟᴇᴀᴋs: <a href='https://t.me/+ғᴜʏ𝟹ʟᴊʀsᴊᴘɢ𝟶ɴɢɪ𝟷'> ɪɴsᴛᴀɢʀᴀᴍ 🫣 </a>\n"
            "❃ 🌚 ᴄᴇʟᴇʙʀɪᴛɪᴇs ʟᴇᴀᴋs : <a href='https://t.me/+-duU_vRUZzswZDY1'>ʜᴇʀᴏɪɴᴇs 🫠 </a>\n"
            "❃ 🫰 ғɪʟᴛᴇʀ ʙᴏᴛ : <a href='https://t.me/Aryas_Movies_Finder_bot'>ғɪʟᴛᴇʀ ʙᴏᴛ 🫶</a></blockquote></b>"
            ),
            disable_web_page_preview=True,  # ✅ Added missing comma
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🪿 Close", callback_data="close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
