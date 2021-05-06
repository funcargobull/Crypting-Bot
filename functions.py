from cryptography.fernet import Fernet

def encrypt(filename, key):
# Зашифруем файл и записываем его
	f = Fernet(key)
	with open(filename, 'rb') as file:
		# прочитать все данные файла
		file_data = file.read()
	encrypted_data = f.encrypt(file_data)
	with open(filename, 'wb') as file:
		file.write(encrypted_data)

def decrypt(filename, key):
# Расшифруем файл и записываем его
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # читать зашифрованные данные
        encrypted_data = file.read()
    # расшифровать данные
    decrypted_data = f.decrypt(encrypted_data)
    # записать оригинальный файл
    with open(filename, 'wb') as file:
        file.write(decrypted_data)