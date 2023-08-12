def encrypt(text,k):
    result=""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            result+=chr((ord(char)+k-65)%26+65)
        else:
            result+=chr((ord(char)+k-97)%26+97)
    return result
text="lkdwhwridlolqwkhhadp"
k=3
#print("c="+encrypt(text,k))

print("d="+encrypt(text,26-k%26))