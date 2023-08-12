text="hello"
keymatrix=[[6,24,1],[13,16,10],[20,17,15]]
keylen=3
textlen=len(text)
cipher=""
while textlen%keylen!=0:
    text=text+'x'
    textlen=textlen+1
    print("padded text=",text)
for i in range(0,textlen,keylen):
    textsegment=text[i:i+keylen]
    ciphersegment=""
    for j in range(keylen):
        sum=0
        for k in range(keylen):
            sum+=(ord(textsegment[k])-ord('a'))*keymatrix[j][k]
        ciphersegment+=chr(ord('a')+(sum+26)%26)
    cipher+=ciphersegment
print(cipher)    