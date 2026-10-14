import random
import string


chars = string.printable
chars = list(chars)
key = chars.copy()
random.shuffle(key)
#encrypt
text = input("Enter your message: ")
c_text = ""
for letter in text:
    index = chars.index(letter) #находим число из массива
    c_text += key[index] #добавляем в массив буквы по значению индекса (в chars и key значения будут разными)
print(f"Encrypt message: {c_text}")

print()
#decrypt
c_text = input("Enter your encrypt message: ")
text = ""
for letter in c_text:
    index = key.index(letter)
    text += chars[index]
print(f"Decrypt message: {text}")

