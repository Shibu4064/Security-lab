def vigenere_decrypt(ciphertext,key):
    key=''.join(filter(str.isalpha,key.upper()))
    decrypted_text=""
    key_index=0

    for char in ciphertext:
        if char.isalpha():
            shift=ord(key[key_index])-ord('A')
            if char.isupper():
                decrypted_char=chr((ord(char)-shift-ord('A'))%26+ord('A'))
            else:
                decrypted_char=chr((ord(char)-shift-ord('a'))%26+ord('a'))
            decrypted_text+=decrypted_char
            key_index=(key_index+1)%len(key)
        else:
            decrypted_text+=char
    return decrypted_text


ciphertext="LXFOPVEFRNHR"
key="LEMON"
decrypted_msg=vigenere_decrypt(ciphertext,key)
print("decrypted message: ", decrypted_msg)

