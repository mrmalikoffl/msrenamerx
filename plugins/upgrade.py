"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Upload File Size Upto 2GB
	Price Rs 49  ind /🌎 0.8$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Upload File Size Upto 2GB
	Price Rs 99  ind /🌎 1.2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Upload File Size Upto 2GB
	Price Rs 199  ind /🌎 2.5$  per Month
	
	
	Pay Using Upi I'd ```msmalikoffl@oksbi```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mrmalik_offl"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mrmalik_offl")], 
        			[InlineKeyboardButton("Paytm",url = "https://te.legra.ph/Payment-01-04"),
        			InlineKeyboardButton("Paytm",url = "https://te.legra.ph/Payment-01-04")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🪙 Silver Tier 🪙** 
	Daily  Upload  limit 10GB
	Upload File Size Upto 2GB
	Price Rs 49  ind /🌎 0.8$  per Month
	
	**💫 Gold Tier 💫**
	Daily Upload limit 50GB
	Upload File Size Upto 2GB
	Price Rs 99  ind /🌎 1.2$  per Month
	
	**💎 Diamond 💎**
	Daily Upload limit 100GB
	Upload File Size Upto 2GB
	Price Rs 199  ind /🌎 2.5$  per Month
	
	
	Pay Using Upi I'd ```msmalikoffl@oksbi```
	
	After Payment Send Screenshots Of 
        Payment To Admin @mrmalik_offl"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/mrmalik_offl")], 
        			[InlineKeyboardButton("Paytm",url = "https://te.legra.ph/Payment-01-04"),
        			InlineKeyboardButton("Paytm",url = "https://te.legra.ph/Payment-01-04")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
