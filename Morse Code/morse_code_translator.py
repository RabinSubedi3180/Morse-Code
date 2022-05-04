import pickle


def encode(msg):
    split_msg = msg.split()
    encoded_word_list = []
    for word in split_msg:
        word_list = []
        for char in word:
            if char != '':
                morse = list(morse_code.keys())[
                    list(morse_code.values()).index(char)]
            else:
                morse = " "
            word_list.append(morse)
        encoded_word = " ".join(word_list)
        encoded_word_list.append(encoded_word)
    encoded_msg = "  ".join(encoded_word_list)
    return encoded_msg


def decode(encoded_msg):
    split_msg = encoded_msg.split("  ")
    decoded_word = ''
    decoded_wordlist = []
    for encoded_word in split_msg:
        e_letter = encoded_word.split()
        character = []
        for char in e_letter:
            if char != " ":
                decrypt = list(morse_code.values())[
                    list(morse_code.keys()).index(char)]
                character.append(decrypt)
            decoded_word = ''.join(character)
        decoded_wordlist.append(decoded_word)
    decoded_msg = ' '.join(decoded_wordlist)
    return decoded_msg


if __name__ == "__main__":
    with open("morse_code.pkl", "rb") as f:
        morse_code = pickle.load(f)
    print("This program encodes your message into morse code and decodes the morse encoded message into normal message")
    while True:
        user_choice = input(
            "Press e to encode and d to decode your message and r to exit the program: ")[0].lower()
        if user_choice == 'e':
            message = input(
                "Please enter your message to encode it:\n").upper()
            print(encode(message))
        elif user_choice == 'd':
            message = input("Please enter your message to decode it:\n")
            print(decode(message))
        elif user_choice == 'r':
            print("Thank you for using this program!!!")
            break
        else:
            print("Invalid choice!!! Please try again!!!")
