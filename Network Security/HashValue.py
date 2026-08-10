import hashlib

#input sentence
message = "cyber security is most important for protecting digital information"

#Generate SHA-3_256 hash value
hash_value = hashlib.sha3_256(message.encode())

#Print the hash value in hexadecimal format
print("Input message: ", message)
print("SHA-3_256 Hash Value: ", hash_value.hexdigest())