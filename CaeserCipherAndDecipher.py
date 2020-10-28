## Author: Feras
## Problem: A Caesar Cipher and Decipher program

def encode(sentence,shift):
    result = ""
    for i in range(len(sentence)):
        for j in sentence[i]:
            if j.isupper():
                result += chr((ord(j) + shift - 65) % 26 + 65)
            elif j.islower():
                result += chr((ord(j) + shift - 97) % 26 + 97)
            elif j == " ":
                result += j
    return result


def decode(sentence,shift):
    result = ""
    for i in range(len(sentence)):
        for j in sentence[i]:
            if j.isupper():
                result += chr((ord(j) - shift - 65) % 26 + 65)
            elif j.islower():
                result += chr((ord(j) - shift - 97) % 26 + 97)
            elif j == " ":
                result += j
    return result

"""Test inputs, just uncomment the statements"""
# test = "I am genius"
# test = "He is a master math teacher"
# test = "Zeitz is an ancient place of Slavonic origin"
test = "Konigs expressed the opinion that the alkaloids were derivatives of pyridine or quinoline"

shift = 5
print(encode(test, shift))
print(decode(encode(test, shift), shift))