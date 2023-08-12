def vigenere_encrypt(text,key):
    encrypted_text=""
    keylen=len(key)
    keyind=0
    for i in range(len(text)):
        ch=text[i]
        if ch.isalpha():
            ch=ch.lower()
            k=ord(key[keyind])-ord('a')
            ch_int=ord(ch)-ord('a')
            ch_int=(ch_int+k)%26
            encrypted_text+=chr(ord('a')+ch_int)
            keyind=(keyind+1)%keylen
        else:
            encrypted_text+=ch
    return encrypted_text

def vigenere_decrypt(text,key):
    decrypted_text=""
    keylen=len(key)
    keyind=0
    for i in range(len(text)):
        ch=text[i]
        if ch.isalpha():
            ch=ch.lower()
            k=ord(key[keyind])-ord('a')
            ch_int=ord(ch)-ord('a')
            ch_int=(ch_int-k+26)%26
            decrypted_text+=chr(ord('a')+ch_int)
            keyind=(keyind+1)%keylen
        else:
            decrypted_text+=ch
    return decrypted_text




if __name__=="__main__":
    text="i love khona"
    key="life"
    print("main text: ", text)
    encrypted_text=vigenere_encrypt(text,key)
    print("enc msg is:-", encrypted_text)
    decrypted_text=vigenere_decrypt(encrypted_text,key)
    print("dec msg is:-", decrypted_text)

