import hashlib

#Take a password input from user
Password = input ("Enter an alphanumeric password: ")

#Generate SHA-256 Hash value
hash_value = hashlib.sha256(Password.encode()).hexdigest()

#Display result
print("Original password", Password)
print("SHA-256 Hash Value")
print(hash_value)