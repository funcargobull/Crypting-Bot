import telebot, os
from cryptography.fernet import Fernet
from binascii import Error as binascii_error
from functions import *

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=["encrypt"])
def on_encrypt(message):
	msg = bot.send_message(message.from_user.id, "Send me a file:")
	bot.register_next_step_handler(msg, next_encrypt)
	
def next_encrypt(message):
	try:
		file_id = message.document.file_id
		file_info = bot.get_file(file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		with open(file_info.file_path, 'wb') as new_file:
			new_file.write(downloaded_file)
		key = Fernet.generate_key()
		encrypt(file_info.file_path, key)
		bot.send_message(message.from_user.id, f"Key: {key.decode('utf-8')}")
		with open(file_info.file_path, 'rb') as file:
			bot.send_document(message.from_user.id, file)
		os.remove(file_info.file_path)
	except AttributeError:
		bot.send_message(message.from_user.id, "You did not send a file!")

@bot.message_handler(commands=["decrypt"])
def on_decrypt(message):
	msg = bot.send_message(message.from_user.id, "Send me a key:")
	bot.register_next_step_handler(msg, next_decrypt)

def next_decrypt(message):
	global key
	key = message.text
	msg = bot.send_message(message.from_user.id, "Send me a file:")
	bot.register_next_step_handler(msg, one_more_decrypt)

def one_more_decrypt(message):
	global key
	try:
		file_id = message.document.file_id
		file_info = bot.get_file(file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		with open(file_info.file_path, 'wb') as new_file:
			new_file.write(downloaded_file)
		decrypt(file_info.file_path, key)
		with open(file_info.file_path, 'rb') as file:
			bot.send_document(message.from_user.id, file)
		os.remove(file_info.file_path)
	except AttributeError:
		bot.send_message(message.from_user.id, "You did not send a file!")
	except binascii_error:
		bot.send_message(message.from_user.id, "You sent an incorrect key!")
		os.remove(file_info.file_path)

bot.polling(none_stop=1)