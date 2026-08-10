from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

import base64

#secret key (16 bytes for AES-128)
key = b'1234567890abcdef'

#input message
message = input("Enter the message to encrypt: ")

#AES encryption
cipher = AES.new(key, AES.MODE_ECB)
encrypted_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
encrypted_text = base64.b64encode(encrypted_bytes).decode()

print(f"Encrypted message: {encrypted_text}")

#AES decryption
decipher = AES.new(key, AES.MODE_ECB)
decrypted_bytes = unpad(decipher.decrypt(base64.b64decode(encrypted_text)), AES.block_size)
decrypted_text = decrypted_bytes.decode()
print(f"Decrypted message: {decrypted_text}")