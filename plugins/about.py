import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"πΎππππππππ π±πΎπ :- <a href='https://t.me/msrenamerx_bot'>πΌπ πππππππ π</a>\nπ³ππππππππ :- <a href='https://t.me/mrmalik_offl'>π§π»βπ¦±πΌπ πΌπππππ§π»βπ¦±</a>\nπ»πππππππ :- πΏπ’πππππΉ\nπ»ππππππ’ :- πΏπ’ππππππ πΈ.πΆ\nππππππ :- ππππππ\nπππππ πππππππ π΅πππ :- {total_rename}\nπππππ πππ£π πππππππ :- {humanbytes(int(total_size))}\n\n πππππ π’ππ **<a href='https://t.me/mrmalik_offl'>πΌπ πΌππππ</a>** πππ π’πππ ππππ π πππ",quote=True)
