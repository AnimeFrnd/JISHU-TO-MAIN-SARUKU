from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        text = (
            "<b><blockquote>❃ 💓 ᴏᴡɴᴇʀ (ᴄᴜᴛɪᴇ❣️) : <a href='https://t.me/Nithya_Sree_Bot'>𝓝𝓲𝓉𝓱𝓎𝓪 𝓼𝓱𝓻𝓮𝓮 🥀🦋</a>\n"
            "❃ 🫡ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href='https://t.me/Telugu_Saruku_Bitlu'>ᴛᴇʟᴜɢᴜ sᴀʀᴜᴋᴜ ʙɪᴛʟᴜ 🥵</a>\n"
            "❃ 🥵 ʟ€@ᴋ$: <a href='https://t.me/+4QSB2tPk-ME2NDdl'>ᴄʟɢ ɢɪʀʟ ᴀɴᴅ ʟᴜᴠʀs 😛</a>\n"
            "❃ 🔞 ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟ : <a href='https://t.me/+aph6xGmeXgU2NzFl'>ᴀᴅᴜʟᴛ ᴍᴏᴠɪᴇs 🤤</a>\n"
            "❃ 🌝 ɪɴsᴛᴀ ʟᴇᴀᴋs: <a href='https://t.me/+ғᴜʏ𝟹ʟᴊʀsᴊᴘɢ𝟶ɴɢɪ𝟷'> ɪɴsᴛᴀɢʀᴀᴍ 🫣 </a>\n"
            "❃ 🌚 ᴄᴇʟᴇʙʀɪᴛɪᴇs ʟᴇᴀᴋs : <a href='https://t.me/+-duU_vRUZzswZDY1'>ʜᴇʀᴏɪɴᴇs 🫠 </a>\n"
            "❃ 🫰 ғɪʟᴛᴇʀ ʙᴏᴛ : <a href='https://t.me/Aryas_Movies_Finder_bot'>ғɪʟᴛᴇʀ ʙᴏᴛ 🫶</a></blockquote></b>"
        )

        try:
            # Ensure the text is UTF-8 encoded
            text.encode('utf-8')
        except UnicodeEncodeError as e:
            print(f"Error encoding text: {e}")
            # Handle encoding issue here, e.g., by removing problematic characters
            text = text.replace("🦋", "")  # Example: Replace problematic characters (customize this as needed)
        
        await query.message.edit_text(
            text=text,
            disable_web_page_preview=True,
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
