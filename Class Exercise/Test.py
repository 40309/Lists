#Tony K.
#07/01/2015
#Christmas Functions

def encrypting():
    message = input("Please enter your message you want to encrypt: ")
    shift_value = int(input("Please enter your shift value: "))
    encrypted_message = ""
    for character in message:
        encrypt = ord(character)
        encrypt = encrypt + shift_value
        number_2 = chr(encrypt)
        encrypted_message = encrypted_message + number_2
    return encrypted_message

def decrypting():
    message = input("Please enter your message you want to decrypt: ")
    shift_value = int(input("Please enter the shift value: "))
    decrypted_message = ""
    for character in message:
        decrypt = ord(character)
        decrypt = decrypt - shift_value
        number_2 = chr(decrypt)
        decrypted_message = decrypted_message + number_2
    return decrypted_message

def display(encrypted_message):
    print(encrypted_message)

def display(decrypted_message):
    print(decrypted_message)


#main

def main():
    checker = False
    while checker == False:
        choice = input("Do you want to encyrpt or decrypt a message: ")
        choice = choice.upper()
        choice = choice[0]
        print()
        if choice == "E":
            encrypted_message = encrypting()
            display(encrypted_message)
            checker = True
        elif choice == "D":
            decrypted_message = decrypting()
            display(decrypted_message)
            checker = True
        else:
            print("Please Try again")
    print("Thank you for using my program :)")
    
    
