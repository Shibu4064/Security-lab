def encrypt(text,k):
    result="" 

    for i in range(len(text)):
        char=text[i]

        if(char.isupper()):
            result=result+chr((ord(char)+k-65)%26+65)

        else:
            result=result+chr((ord(char)+k-97)%26+97)

    return result

text="Lzdqwwrixfnbrx"
k=3
print("key:"+str(k))
#print("cipher text:"+encrypt(text,k))



print("decrypted:"+encrypt(text,26-k%26))