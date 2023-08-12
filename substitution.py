import string
all_letters=string.ascii_letters
dict1={}
k=4
#ENCRYPTION PROCESS
for i in range(len(all_letters)):
    dict1[all_letters[i]]=all_letters[(i+k)%len(all_letters)]

text="""cz uczsdj qv lcf day vjqyq vdos ws kwz icwavgo ygsm sq zcm fqqy-lmd sq skd fgdzsz.
jguqgjz qv zsjcafd dedasz kcy lm aqn zijdcy coo qedj skd vwdoy, lgs vjqyq nqgoy qaom zcm aq
yqgls dedjmskwaf nwoo ld todcjdy gi wa skd uqjawaf. clqgs uwyawfks tcjjwcfdz tcud vqj skd
wuiqjscas vqox. qad lm qad skdm jqoody cncm, vwoody nwsk vgoo lgs edjm gazcswzvwdy
kqllwsz. fcjydadjz tcud lm cjjcafdudas, cay jduqedy wa nkddo-lcjjqnz skqzd skcs kcy
wacyedjsdasom jducwady ldkway. awfks zoqnom
    """
cipher_text=[]

for char in text:
    if char in all_letters:
        temp=dict1[char]
        cipher_text.append(temp)
    else:
        temp=char
        cipher_text.append(temp)

cipher_text="".join(cipher_text)
print("cipher text:", cipher_text)


#DECRYPTION PROCESS
dict2={}
for i in range(len(all_letters)):
    dict2[all_letters[i]]=all_letters[(i-k)%len(all_letters)]

decrypted_text=[]

for char in cipher_text:
    if char in all_letters:
        temp=dict2[char]
        decrypted_text.append(temp)
    else:
        temp=char
        decrypted_text.append(temp)

decrypted_text="".join(decrypted_text)
print("decrypted text:", decrypted_text)