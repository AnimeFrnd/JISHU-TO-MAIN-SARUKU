import unicodedata

def sanitize_text(text: str) -> str:
    # Remove non-UTF-8 characters by normalizing the string
    return ''.join(c for c in text if unicodedata.category(c) != 'Cn')

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

        sanitized_text = sanitize_text(text)

        try:
            await query.message.edit_text(
                text=sanitized_text,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🪿 Close", callback_data="close")
                        ]
                    ]
                )
            )
        except UnicodeEncodeError as e:
            print(f"Error encoding text: {e}")
            # You can further handle the encoding issue or log the error here.
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
