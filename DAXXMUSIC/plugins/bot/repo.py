from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from DAXXMUSIC import app
from config import BOT_USERNAME

start_txt = """**
✪ ωεℓ¢σмє тσ χᴅ яєρσ ✪
 
 ➲ ᴀʟʟ ʀᴇᴘᴏ ᴇᴀsɪʟʏ ᴅᴇᴘʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ ᴡɪᴛʜᴏᴜᴛ ᴀɴʏ ᴇʀʀᴏʀ ✰
 
 ➲ ɴᴏ ʜᴇʀᴏᴋᴜ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ ɴᴏ ɪᴅ ʙᴀɴ ɪssᴜᴇ ✰
 
 ➲ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰
 
 ➲ ʀᴜɴ 24x7 ʟᴀɢ ғʀᴇᴇ ᴡɪᴛʜᴏᴜᴛ sᴛᴏᴘ ✰
 
 ► ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛʜᴇɴ sᴇɴᴅ ss
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("Δᴅᴅ ᴍє", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("нєℓρ", url="https://t.me/ITZ_4_U/2"),
          InlineKeyboardButton("σωиєя", url="https://t.me/CoronaXvirus"),
          ],
               [
                InlineKeyboardButton("Δʙᴏᴜᴛ Nandan", url="https://t.me/ABOUT_NANDAN"),

],
[
              InlineKeyboardButton("「ᴠᴀᴍᴘ ⚚ ϐοτz」", url=f"https://t.me/About_Nandan"),
              InlineKeyboardButton("︎「ᴠᴀᴍᴘ ⚚ иєƚωσɾƙ」", url=f"https://t.me/Vamp_Network"),
              ],
              [
              InlineKeyboardButton("ᴀʙᴏᴜᴛ ɴᴀɴᴅᴀɴ", url=f"https://t.me/About_Nandan"),
InlineKeyboardButton("ᴅᴘ ᴡᴏʀʟᴅ", url=f"https://t.me/CoronaXvirus"),
],
[
InlineKeyboardButton("sᴛʀɪɴɢʙᴏᴛ", url=f"https://t.me/DairyMilk_STRING_BOT"),
InlineKeyboardButton("ғᴇᴅᴇʀᴀᴛɪᴏɴ", url=f"https://t.me/CoronaXvirus"),
],
[
              InlineKeyboardButton("ᴍᴜsɪᴄ ʙᴏᴛ ʀᴇᴘᴏ", url=f"https://t.me/N91Ab/6"),
              InlineKeyboardButton("sƚΔƚυs", url=f"https://t.me/CoronaXvirus"),
              ],
              [
              InlineKeyboardButton("𝗞ɪᴅѕ 𝗢ғ 𝗧ᴇʟᴇɢʀᴀᴍ︎", url=f"https://t.me/ho_gya_viral"),
InlineKeyboardButton("ɪɴsᴛᴀ", url=f"https://instagram.com/NANDAN_SINGH_0852?igshid=MzNlNGNkZWQ4Mg=="),
],
[
InlineKeyboardButton("ᴡʜᴀᴛsᴀᴘᴘ", url=f"https://wa.me/qr/6207739436"),
InlineKeyboardButton("ᴜᴘᴄᴏᴍɪɴɢ", url=f"https://t.me/admin"),
],
[
InlineKeyboardButton("ɴᴀɴᴅᴀɴ | 𝐃𝐏𝐙 | 𝐄𝐃𝐈𝐓𝐙 ✨", url=f"https://t.me/ABOUT_NANDAN"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/360676a2c160029e03e46.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
