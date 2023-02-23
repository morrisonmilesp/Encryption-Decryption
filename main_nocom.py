
# How to decrease number of saved characters, repeat characters?


def encryption():
    import subprocess

    key = input("Input your password: ")
    translated_key = [ord(character) for character in key]

    if len(translated_key) <= 0:
        print("")
        print("WARNING - not entering a password means your message will not be encrypted "
              "it will only be translated using ASCII")
        print("If you want to encrypt your message, restart the program")

    print("")

    message = input("Input your message: ")
    translated_message = [ord(character) for character in message]

    encrypted_message = []

    if len(translated_key) > 0:
        for position_value in range(len(translated_message)):
            position_loop_value = position_value % len(translated_key)
            encrypted_message.append(translated_message[position_value] + translated_key[position_loop_value])

        subprocess.run("pbcopy", universal_newlines=True, input=str(encrypted_message))
        print("")
        print("Here is your encrypted message: " + str(encrypted_message))
        print("The encrypted message has automatically been saved to your keyboard")
        print("This is the password you set to unlock it: " + key)

    else:
        subprocess.run("pbcopy", universal_newlines=True, input=str(translated_message))
        print("")
        print("Here is your ASCII translated message: " + str(translated_message))
        print("The translated message has automatically been saved to your keyword")
        print("No password is necessary to unlock it using this programs Decrypt function")


def decryption():
    import ast
    encrypted_message_str = input("Input the secret code: ")

    while encrypted_message_str[0] != "[" or encrypted_message_str[len(encrypted_message_str) - 1] != "]":
        print("")
        print("The secret code you input is in the incorrect format, please input exactly what you received")
        encrypted_message_str = input("Input the secret code: ")

    encrypted_message_list = ast.literal_eval(encrypted_message_str)
    password = list(input("Input the password: "))

    password_translated = [ord(character) for character in password]

    decrypted_message = []
    if len(password_translated) > 0:
        for position_value in range(len(encrypted_message_list)):
            position_loop_value = position_value % len(password_translated)
            decrypted_message.append(chr(encrypted_message_list[position_value] -
                                         password_translated[position_loop_value]))
    else:
        for position_value in range(len(encrypted_message_list)):
            decrypted_message.append(chr(encrypted_message_list[position_value]))

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
