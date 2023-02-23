#  Displacement Encryption and Decryption
#  Created by: Miles Morrison
#  Date: 10/19/2021
#  Encrypt is largely completed, next up is Decrypt

def encryption():
    # subprocess is used to copy encrypted message to keyboard automatically
    import subprocess

    key = input("Input your password: ")
    # Numerical translation using ASCII
    translated_key = [ord(character) for character in key]

    # No encryption warning -
    # With no password, there is no displacement and therefore no encryption
    if len(translated_key) <= 0:
        print("")
        print("WARNING - not entering a password means your message will not be encrypted "
              "it will only be translated using ASCII")
        print("If you want to encrypt your message, restart the program")

    print("")

    message = input("Input your message: ")
    # Numerical translation using ASCII
    translated_message = [ord(character) for character in message]

    # Displacement Encryption
    # When position_value > len(key) an error is thrown because that position doesn't exist for key
    # So we essentially make key's length infinite by repeating it so this error isn't thrown
    # Ex: For a 6 figure key, key[7] = key[1] & key[8] = key{2} etc.

    encrypted_message = []

    if len(translated_key) > 0:
        for position_value in range(len(translated_message)):
            position_loop_value = position_value % len(translated_key)
            encrypted_message.append(translated_message[position_value] + translated_key[position_loop_value])

        subprocess.run("pbcopy", universal_newlines=True, input=str(encrypted_message))
        print("")
        print("Here is your encrypted message: " + str(encrypted_message))
        print("The encrypted message has automatically been saved to your keyword")
        print("This is the password you set to unlock it: " + key)

    else:
        subprocess.run("pbcopy", universal_newlines=True, input=str(translated_message))
        print("")
        print("Here is your ASCII translated message: " + str(translated_message))
        print("The translated message has automatically been saved to your keyword")
        print("No password is necessary to unlock it using this programs Decrypt function")


def decryption():
    # Abstract syntax Tree contains function called literal_eval() which extracts python literals from strings
    import ast
    encrypted_message_str = input("Input the encrypted message: ")

    # Ensures user input a str containing a list literal
    while encrypted_message_str[0] != "[" or encrypted_message_str[len(encrypted_message_str) - 1] != "]":
        print("")
        print("The secret code you input is in the incorrect format, please input exactly what you received")
        encrypted_message_str = input("Input the secret code: ")

    # Turns str containing list into a list literal
    encrypted_message_list = ast.literal_eval(encrypted_message_str)
    key = list(input("Input the password: "))

    # Translates input key using ASCII
    key_translated = [ord(character) for character in key]

    # Decrypts the message by using the inverse of the operation used for encryption
    # I could eventually set these functions equal to variable so user can go into code and alter operation
    decrypted_message = []
    if len(key_translated) > 0:
        for position_value in range(len(encrypted_message_list)):
            position_loop_value = position_value % len(key_translated)
            decrypted_message.append(chr(encrypted_message_list[position_value] -
                                         key_translated[position_loop_value]))
    else:
        for position_value in range(len(encrypted_message_list)):
            decrypted_message.append(chr(encrypted_message_list[position_value]))

    # Compiles each decrypted character into the message
    final_message = ''.join(decrypted_message)
    print("")
    print("Your decrypted message is: " + final_message)


def main():
    decision = input("Enter 'e' to Encrypt or 'd' to Decrypt: ")
    if decision == "e" or decision == "E":
        encryption()
    elif decision == "d" or decision == "D":
        decryption()
    else:
        print("An invalid character was entered, please try again")


main()
