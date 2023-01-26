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
	await message.reply_text(f"➤ 𝓞𝓻𝓲𝓰𝓲𝓸𝓷𝓪𝓵 𝓑𝓞𝓣 :- <a href='https://t.me/msrenamerx_bot'>𝓜𝓼 𝓡𝓮𝓷𝓪𝓶𝓮𝓻 𝓧</𝓪>\n➤ 𝓓𝓮𝓿𝓮𝓵𝓸𝓹𝓮𝓻 :- <a href='https://t.me/mrmalik_offl'>🧑🏻‍🦱𝓜𝓻 𝓜𝓪𝓵𝓲𝓴🧑🏻‍🦱</𝓪>\n➤ 𝓛𝓪𝓷𝓰𝓾𝓪𝓰𝓮 :- 𝓟𝔂𝓽𝓱𝓸𝓷3\n➤ 𝓛𝓲𝓫𝓻𝓪𝓻𝔂 :- 𝓟𝔂𝓻𝓸𝓰𝓻𝓪𝓶 2.0\n➤ 𝓢𝓮𝓻𝓿𝓮𝓻 :- 𝓚𝓞𝓨𝓔𝓑\n➤ 𝓣𝓸𝓽𝓪𝓵 𝓡𝓮𝓷𝓪𝓶𝓮𝓭 𝓕𝓲𝓵𝓮 :- {total_rename}\n➤ 𝓣𝓸𝓽𝓪𝓵 𝓢𝓲𝔃𝓮 𝓡𝓮𝓷𝓪𝓶𝓮𝓭 :- {humanbytes(int(total_size))}\n\n 𝓣𝓱𝓪𝓷𝓴 𝔂𝓸𝓾 <a href='https://t.me/mrmalik_offl'>𝓜𝓻 𝓜𝓪𝓵𝓲𝓴</𝓪> 𝓯𝓸𝓻 𝔂𝓸𝓾𝓻 𝓱𝓪𝓻𝓭 𝔀𝓸𝓻𝓴",quote=True)
