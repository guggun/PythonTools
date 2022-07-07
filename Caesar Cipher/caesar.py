alphabet = "abcdefghijklmnopqrstuvwxyz "
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))


def encrypt(message, shift=3):
    cipher = ""

    for letter in message:
        number = (letter_to_index[letter] + shift) % len(letter_to_index)
        letter = index_to_letter[number]
        cipher += letter

    return cipher


def decrypt(cipher, shift=3):
    decrypted = ""

    for letter in cipher:
        number = (letter_to_index[letter] - shift) % len(letter_to_index)
        letter = index_to_letter[number]
        decrypted += letter

    return decrypted


def main():
     message = 'hs is a essan'
     cipher = encrypt(message, shift=3)
     decrypted = decrypt(cipher, shift=3)

     print('Original message: ' + message)
     print('Encrypted message: ' + cipher)
     print('Decrypted message: ' + decrypted)

main()