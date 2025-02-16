import os
import asyncio
import humanize
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from bot import Bot
from config import (
    ADMINS, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, 
    PROTECT_CONTENT, FILE_AUTO_DELETE, START_PIC
)
from helper_func import subscribed, encode, decode, get_messages
from database.database import add_user, del_user, full_userbase, present_user

# Convert FILE_AUTO_DELETE to human-readable time
file_auto_delete = humanize.naturaldelta(FILE_AUTO_DELETE)


@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except:
            pass

    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")

        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            ids = range(start, end+1) if start <= end else range(start, end-1, -1)
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        else:
            return

        temp_msg = await message.reply("Please Wait...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something Went Wrong..!")
            return

        await temp_msg.delete()

        sent_msgs = []
        for msg in messages:
            caption = (
                CUSTOM_CAPTION.format(
                    previouscaption=msg.caption.html if msg.caption else "",
                    filename=msg.document.file_name
                )
                if CUSTOM_CAPTION and msg.document else msg.caption.html if msg.caption else ""
            )

            reply_markup = msg.reply_markup if DISABLE_CHANNEL_BUTTON else None
            try:
                sent_msg = await msg.copy(
                    chat_id=message.from_user.id, caption=caption, 
                    parse_mode=ParseMode.HTML, reply_markup=reply_markup, 
                    protect_content=PROTECT_CONTENT
                )
                sent_msgs.append(sent_msg)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                sent_msg = await msg.copy(
                    chat_id=message.from_user.id, caption=caption, 
                    parse_mode=ParseMode.HTML, reply_markup=reply_markup, 
                    protect_content=PROTECT_CONTENT
                )
                sent_msgs.append(sent_msg)
            except:
                pass

        # Send file deletion warning
        k = await client.send_message(
            chat_id=message.from_user.id,
            text=f"<b>❗️ <u>IMPORTANT</u> ❗️</b>\n\nThis Video / File Will Be Deleted In {file_auto_delete} (Due To Copyright Issues).\n\n📌 Please Forward This Video / File To Somewhere Else And Start Downloading There."
        )

        # Schedule the file deletion
        asyncio.create_task(delete_files(sent_msgs, client, k))
        return

    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('🥵 Oᴜʀ Mᴀɪɴ Cʜᴀɴɴᴇʟ 🥵', url='https://t.me/Telugu_Saruku_Bitlu')
        ],[
            InlineKeyboardButton('🌚 Hollywood Hot Movies', url='https://t.me/+aph6xGmeXgU2NzFl'),
            InlineKeyboardButton('🌝 N#D€ Videos @!nd L€@k$', url='https://t.me/+4QSB2tPk-ME2NDdl')
        ],[
            InlineKeyboardButton('🤤 ᴀʙᴏᴜᴛ ᴍᴇ', callback_data='about'),
            InlineKeyboardButton('🔒 Close', callback_data='close')
                    
                ]
            ]
        )

        await message.reply_photo(
            photo=START_PIC,  # Start message image
            caption=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=f'@{message.from_user.username}' if message.from_user.username else None,
                mention=message.from_user.mention,
                id=message.from_user.id
            ),
            reply_markup=reply_markup,
            quote=True
        )
        return


@Bot.on_message(filters.command('start') & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton("❃ Join Channel ❃", url=client.invitelink),
            InlineKeyboardButton("❃ Join Channel ❃", url=client.invitelink2),
        ],
        [
            InlineKeyboardButton("❃ Join Channel ❃", url=client.invitelink3),
            InlineKeyboardButton("❃ Join Channel ❃", url=client.invitelink4),
        ]
    ]
    try:
        buttons.append([
            InlineKeyboardButton(
                text='Try Again',
                url=f"https://t.me/{client.username}?start={message.command[1]}"
            )
        ])
    except IndexError:
        pass

    await message.reply(
        text=FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name,
            username=f'@{message.from_user.username}' if message.from_user.username else None,
            mention=message.from_user.mention,
            id=message.from_user.id
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )


@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text="Processing...")
    users = await full_userbase()
    await msg.edit(f"{len(users)} Users Are Using This Bot")


@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0

        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1

        status = f"""<b><u>Broadcast Completed</u></b>

<b>Total Users :</b> <code>{total}</code>
<b>Successful :</b> <code>{successful}</code>
<b>Blocked Users :</b> <code>{blocked}</code>
<b>Deleted Accounts :</b> <code>{deleted}</code>
<b>Unsuccessful :</b> <code>{unsuccessful}</code>"""

        return await pls_wait.edit(status)
    else:
        msg = await message.reply("Use This Command As A Reply To Any Telegram Message Without Spaces.")
        await asyncio.sleep(8)
        await msg.delete()


# Function to handle file deletion
async def delete_files(messages, client, k):
    await asyncio.sleep(FILE_AUTO_DELETE)
    for msg in messages:
        try:
            await client.delete_messages(chat_id=msg.chat.id, message_ids=[msg.id])
        except Exception as e:
            print(f"Failed to delete media {msg.id}: {e}")
    await k.edit_text("Your Video / File Is Successfully Deleted ✅")


# 🔹 Jishu Developer  
# 🔹 Telegram Channel: @Madflix_Bots  
# 🔹 Backup Channel: @JishuBotz  
# 🔹 Developer: @JishuDeveloper  
