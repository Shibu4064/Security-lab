import numpy as np
keymatrix=np.array([[6,24,1],[13,16,10],[20,17,15]])
plainsegment=3

def pad_plain_text(plain_text):
    padsize=len(plain_text)%plainsegment
    if padsize==0:
        return plain_text
    padsize=plainsegment-padsize
    for i in range(padsize):
        plain_text+='x'
    return plain_text

def encode_hill_cipher(plain_text):
    cipher=""
    plain_text=pad_plain_text(plain_text)
    print("padded plain text: ", plain_text)
    for i in range(0,len(plain_text),plainsegment):
        segment=plain_text[i:i+plainsegment]
        cipher_seg=""
        for i in range(plainsegment):
            sum=0
            for j in range(plainsegment):
                sum=sum+(ord(segment[j])-ord('a'))*keymatrix[i][j]
            cipher_seg=cipher_seg+chr((sum%26)+ord('a'))
        cipher=cipher+cipher_seg
    return cipher

if __name__=="__main__":
    plain_text="hello"
    print("plain text: ", plain_text)
    cipher_text=encode_hill_cipher(plain_text)
    print("cipher text: ", cipher_text)