def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_len = len(key)
    key_ind = 0

    for i in range(len(text)):
        ch = text[i]

        if ch.isalpha():
            ch = ch.lower()

            # Calculate the shift value for the current character
            k = ord(key[key_ind]) - ord('a')

            # Perform the Vigenere encryption by shifting the character
            ch_int = ord(ch) - ord('a')
            ch_int = (ch_int + k) % 26

            # Append the encrypted character to the result string
            encrypted_text += chr(ord('a') + ch_int)

            # Update the index for the key, wrapping around if necessary
            key_ind = (key_ind + 1) % key_len
        else:
            # If the character is not an alphabet, append it directly to the result string
            encrypted_text += ch

    return encrypted_text


def vigenere_decrypt(text,key):
    decrypted_text=""
    key_len=len(key)
    key_ind=0

    for i in range(len(text)):
        ch=text[i]
        if ch.isalpha():
            ch=ch.lower()
            k=ord(key[key_ind])-ord('a')
            ch_int=ord(ch)-ord('a')
            ch_int=(ch_int-k+26)%26                               #only change is in here
            decrypted_text+=chr(ord('a')+ch_int)
            key_ind=(key_ind+1)%key_len
        else:
            decrypted_text+=ch
    return decrypted_text
		    
if __name__=="__main__":
    text="i love someone and she is the love of my life"    
    key="pinkfloyd"
    print("text: ", text)
    encrypted_text=vigenere_encrypt(text,key)
    print("encrypted text: ", encrypted_text)
    decrypted_text=vigenere_decrypt(encrypted_text,key)
    print("decrypted text: ", decrypted_text)
