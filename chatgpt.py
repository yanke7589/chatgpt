from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
import openai
from pyrogram.types import CallbackQuery
from config import *
import os,sys,re,requests
import asyncio,time
from random import choice
from bardapi import Bard
from datetime import datetime
import logging

FORMAT = "[BRANDED] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
BRANDED = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START = f"""
๏ ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}

➻ ᴀɴ ᴏᴘᴇɴ-ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛɢᴘᴛ
★ ɪ ᴄᴀɴ ᴀɴsᴡᴇʀ ʏᴏᴜʀ ǫᴜsᴛɪᴏɴ ᴇᴀsɪʟʏ

─────────────────

➻ ɪ ᴀᴍ ᴀᴅᴠᴀɴᴄᴇ ʙᴏᴛ ᴀɴᴅ ᴄᴀɴ 
★ ᴀɴsᴡᴇʀ ʏᴏᴜʀ ᴏ̨ᴜᴇʀɪᴇs ᴇᴀsʟɪʏ

✮ Rᴇᴀᴅ Tʜᴇ ʜᴇʟᴘ sᴇᴄᴛɪᴏɴ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏ

★ ᴘʀᴏᴍᴏᴛᴇ ʙʏ : [𝐕𝐢𝐬𝐜𝐨 𝐀𝐥𝐠𝐞𝐫𝐢𝐚𝐧 ꜱᴜᴘᴘᴏʀᴛ](https://t.me/vddffro)
๏ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴜsᴇ /help
"""
xa = bytearray.fromhex("68747470733a2f2f6769746875622e636f6d2f444158585445414d2f4441585843484154475054").decode()
SOURCE = xa
SOURCE_TEXT = f"""
๏ ʜᴇʏ, ɪ ᴀᴍ [{BOT_NAME}]
➻ ᴀɴ ᴏᴘᴇɴ-ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛɢᴘᴛ
☆ ɪ ᴄᴀɴ ᴀɴsᴡᴇʀ ʏᴏᴜʀ ǫᴜᴀᴛɪᴏɴ ᴇᴀsʟɪʏ

──────────────────
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ
"""


x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=choice(x)
MAIN = [
    [
        InlineKeyboardButton(text="☆ ᴜᴘᴅᴀᴛᴇ ☆" , url=f"https://t.me/musicalgerian"),
        InlineKeyboardButton(text="☆ ꜱᴜᴘᴘᴏʀᴛ ☆", url=f"https://t.me/vddffro"),
    ],
    [
        InlineKeyboardButton(
            text="【+】 ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ 【+】",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="♥ ʜᴇʟᴘ & ᴄᴍᴅs ♥", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="☆ ʜᴇʀᴏᴋᴜ ☆", url=f"https://t.me/BRANDED_PAID_CC"),
        InlineKeyboardButton(text="☆ ᴏᴡɴᴇʀ ☆", url=f"https://t.me/BRANDEDKING82"),
    ],
]
X = [
    [
        InlineKeyboardButton(text="☆ ᴏᴡɴᴇʀ ☆", url=f"https://t.me/BRANDEDKING82"),
              
        InlineKeyboardButton(text="☆ ꜱᴜᴘᴘᴏʀᴛ ☆", url=f"https://t.me/vddffro"),
    ]
    ]
    
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="【+】ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ 【+】",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="☆ ꜱᴜᴘᴘᴏʀᴛ ☆", 
                              url=f"https://t.me/vddffro",
         ),
     ],
]
SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('ʀᴇᴘᴏ' , url=f"https://telegra.ph//file/5374701ae0678848e9631.mp4")]])
HELP_READ = "**➻ ᴜsᴀɢᴇ** /chatgpt <prompt>\n\n ʜᴇʟᴘ: `/chatgpt Space then write your question.`\n\n**➻ ᴜsᴀɢᴇ** : /generate <prompt> \nᴇxᴀᴍᴘʟᴇ: `/generate a book photo`  \n\n➻ ᴜsᴀɢᴇ /lyrics : ʀᴇᴘʟʏ ᴛᴏ ᴀᴜᴅɪᴏ ꜰɪʟᴇ ᴛᴏ ᴅᴇᴛᴇᴄᴛ ʟʏʀɪᴄꜱ**➻ ᴜsᴀɢᴇ /ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.**\n\n©️ ᴏᴡɴᴇʀ : [𝐕𝐢𝐬𝐜𝐨 𝐀𝐥𝐠𝐞𝐫𝐢𝐚𝐧](https://t.me/BRANDEDKING82) **"
HELP_BACK = [
     [
           InlineKeyboardButton(text="★ Qᴜᴇꜱᴛɪᴏɴ ᴛʜᴀᴛ ᴄʜᴀᴛɢᴘᴛ ᴄᴀɴ ꜱᴏʟᴠᴇ ★", url=f"https://t.me/vddffro"),
           
     ],
    [
           InlineKeyboardButton(text="★ ʙᴀᴄᴋ ★", callback_data="HELP_BACK"),
    ],
]

  
#         start
@BRANDED.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def start(client, m: Message):
    try:
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(0.2)
        await accha.edit("sᴛᴀʀᴛɪɴɢ ᴄʜᴀᴛ ɢᴘᴛ ʙᴏᴛ 💘🌹..")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(0.3)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
    except Exception as y:
        await m.reply(y)
#  callback 
@BRANDED.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@BRANDED.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_photo(START_IMG,
                        caption=HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@BRANDED.on_message(filters.command(['source', 'repo'], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
#  alive
@BRANDED.on_message(filters.command(["ping","alive"], prefixes=["+", "/", "-", "?", "$", "&","."]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "ᴀɪ ʙᴏᴛ ᴀʟɪᴠɪɴɢ..."
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("ᴀɪ ʙᴏᴛ sᴛᴀʀᴛᴇᴅ......")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"ʜᴇʏ ʙᴀʙʏ!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME}) ɪꜱ ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ꜰɪɴᴇ ᴡɪᴛʜ sᴘᴇᴇᴅ ᴏꜰ \n➥ `{ms}` ms\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ || [𝐕𝐢𝐬𝐜𝐨 𝐀𝐥𝐠𝐞𝐫𝐢𝐚𝐧](https://t.me/BRANDEDKING82)||",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

#  main   
openai.api_key = OPENAI_KEY
@BRANDED.on_message(filters.command(["chatgpt","ai","ask","a"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "HELP:**\n\n`ʟɪᴋʜᴏ ᴜꜱᴋᴇ ʙᴀᴀᴅ ꜱᴘᴀᴄᴇ ᴛʜᴇɴ ᴀᴀᴘɴᴀ Qᴜᴇꜱᴛɪᴏɴ ᴘᴜᴄʜᴏ`")
        else:
            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2)
            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n {BOT_NAME} ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: {e} ")

#  bard 

'''bard = Bard(token=BARD_TOKEN)   
@BRANDED.on_message(filters.command("bard"))
async def bard_bot(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n` /bard How r u? `")
        else:
            a = message.text.split(' ', 1)[1]
            response=bard.get_answer(f"{a}")["content"]
            await message.reply_text(f"{response}\n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ:  {e} ")

    '''
openai.api_key = OPENAI_KEY
@BRANDED.on_message(filters.command(["image","photo","img","generate"],  prefixes=["+", ".", "/", "-", "?", "$","#","&"] ))
async def chat(bot, message):
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        if len(message.command) < 2:
            await message.reply_text(
            "**Example:**\n\n`/generate image name what do you want`")
        else:
            a = message.text.split(' ', 1)[1]
            response= openai.Image.create(prompt=a ,n=1,size="2192x1924")
            image_url = response['data'][0]['url']
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_photo(image_url,caption=f"✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ {telegram_ping} ",parse_mode=ParseMode.DISABLED,reply_markup=InlineKeyboardMarkup(X)) 
    except Exception as e:
            await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} `")
openai.api_key = OPENAI_KEY
@BRANDED.on_message(filters.command(["text","audiototext","lyrics"],  prefixes=["","+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if message.reply_to_message and message.reply_to_message.media:
            
            m = await message.reply_to_message.download(file_name="BRANDED.mp3")
            audio_file = open(m, "rb")
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
            x=transcript["text"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"`{x}` \n ✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ {telegram_ping}")     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} `")



s = bytearray.fromhex("68747470733a2f2f6769746875622e636f6d2f444158585445414d2f4441585843484154475054").decode()

if SOURCE != s:
    print("ᴋᴀʀ ʟɪʏᴀ ᴇᴅɪᴛᴍɪʟ ɢᴀʏᴀ ꜱᴜᴋᴏᴏɴ ᴊᴇꜱᴀ ᴛʜᴀ ᴡᴇꜱᴀ ᴋᴀʀᴅᴇ ` https://github.com/WCGKING/BRANDED-CHATGPT")
    sys.exit(1)  


if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        BRANDED.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN [🍑 ⋆ ʏᴏᴜʀ ʙʀᴀɴᴅᴇᴅ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ ꜱᴛᴀʀᴛ ⋆ 🍑]
    ★·.·´¯`·.·★ᴛʜɪꜱ ʀᴇᴘᴏ ᴍᴀᴅᴇ ʙʏ 𝐕𝐢𝐬𝐜𝐨 𝐀𝐥𝐠𝐞𝐫𝐢𝐚𝐧 ★·.·´¯`·.·★
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    BRANDED.stop()
    print("*☆* ʙʀᴀɴᴅᴇᴅ ᴄʜᴀᴛɢᴘᴛ ʙᴏᴛ ꜱᴛᴀʀᴛ ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴜꜱɪɴɢ ᴛʜɪꜱ ʀᴇᴘᴏ @BARNDRD_BOT @BRANDED_WORLD @BRANDED_PAID_CC *☆* !")
