import hashlib

stored_username = "Admin"
stored_password = "Admin123"

hash_value = hashlib.sha256(stored_username.encode()).hexdigest()
hash_value2 = hashlib.sha256(stored_password.encode()).hexdigest()

Username = input ("Enter username: ")
password = input ("Enter password: ")

hash_value3 = hashlib.sha256(Username.encode()).hexdigest()
hash_value4 = hashlib.sha256(password.encode()).hexdigest()

if hash_value == hash_value3 and hash_value2 == hash_value4:
    print("Username and Password are verified")
else:
    print("Username or password is incorrect")
    




