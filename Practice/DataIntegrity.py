import hashlib

#original sentence
message ="Cyber security is important"

#Generate SHA-3_256 hash value
Orginal_hash_value = hashlib.sha3_256(message.encode()).hexdigest()

print("Input message: ", message)
print("SHA-3_256 Hash Value: ", Orginal_hash_value)

#Verify the integrity 
received_message = input("Please enter the received message: ")
received_hash_value = hashlib.sha3_256(received_message.encode()).hexdigest()

print("Received SHA-3 hash: ", received_hash_value)

if Orginal_hash_value == received_hash_value:
    print("Data integrity verified. The received message is authentic.")
else:
    print("Data integrity verification failed. The received message may have been tampered with.")