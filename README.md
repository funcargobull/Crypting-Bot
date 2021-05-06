# Crypting-Bot
Simple Telegram Bot, which does cool operations with your files

### Principle of operation
This bot can encrypt/decrypt files using symmetric encryption based on the AES algorithm
### Get started
1. Open Telegram and find @BotFather
2. Create a new bot
3. Copy token and paste it here
 
	```
	bot = telebot.TeleBot("TOKEN")
	```
4. Install module **cryptography** using **pip**
	```
	pip install cryptography
	```
5. Start bot.py. Profit!
### Commands
1. /encrypt - you will need to send a file (if it is an image - do not compress it!) and you will get an encrypted file and key
2. /decrypt - you will need to send an encrypted file and key and you will get the original file
### Notes
This bot does **NOT** contain /start and /help commands. Only above ones.
