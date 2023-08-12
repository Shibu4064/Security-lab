def count_letter_appreances(paragraph):
    letter_counts={}

    for char in paragraph:
        if char.isalpha():
            char=char.upper()
            letter_counts[char]=letter_counts.get(char,0)+1
    return letter_counts

if __name__=="__main__":
    paragraph="""cz uczsdj qv lcf day vjqyq vdos ws kwz icwavgo ygsm sq zcm fqqy-lmd sq skd fgdzsz.
jguqgjz qv zsjcafd dedasz kcy lm aqn zijdcy coo qedj skd vwdoy, lgs vjqyq nqgoy qaom zcm aq
yqgls dedjmskwaf nwoo ld todcjdy gi wa skd uqjawaf. clqgs uwyawfks tcjjwcfdz tcud vqj skd
wuiqjscas vqox. qad lm qad skdm jqoody cncm, vwoody nwsk vgoo lgs edjm gazcswzvwdy
kqllwsz. fcjydadjz tcud lm cjjcafdudas, cay jduqedy wa nkddo-lcjjqnz skqzd skcs kcy
wacyedjsdasom jducwady ldkway. awfks zoqnom
    """

    letter_appreances=count_letter_appreances(paragraph)

    for letter, count in letter_appreances.items():
        print(f"letter '{letter}'= {count} times.")


text = """ cz uczsdj qv lcf day vjqyq vdos ws kwz icwavgo ygsm sq zcm fqqy-lmd sq skd fgdzsz.
jguqgjz qv zsjcafd dedasz kcy lm aqn zijdcy coo qedj skd vwdoy, lgs vjqyq nqgoy qaom zcm aq
yqgls dedjmskwaf nwoo ld todcjdy gi wa skd uqjawaf. clqgs uwyawfks tcjjwcfdz tcud vqj skd
wuiqjscas vqox. qad lm qad skdm jqoody cncm, vwoody nwsk vgoo lgs edjm gazcswzvwdy
kqllwsz. fcjydadjz tcud lm cjjcafdudas, cay jduqedy wa nkddo-lcjjqnz skqzd skcs kcy
wacyedjsdasom jducwady ldkway. awfks zoqnom """
text = text.replace('D', 'e')
text = text.replace('S', 't')
text = text.replace('Q', 'a')
text = text.replace('C', 'h')
text = text.replace('A', 'n')
text = text.replace('J', 'o')
text = text.replace('W', 'd')
text = text.replace('Z', 'i')
text = text.replace('K', 'b')
text = text.replace('L', 'y')
text = text.replace('M', 'g')
text = text.replace('G', 'r')
text = text.replace('V', 'f')
text = text.replace('F', 'c')
text = text.replace('U', 'u')
text = text.replace('N', 's')
text = text.replace('E', 'w')
text = text.replace('I', 'm')
text = text.replace('T', 'k')
text = text.replace('X', 'l')

# text = text.replace('H', 'p')\
# text = text.replace('X', 'v')\
# text = text.replace('P', 'j')\
print('The deciphered text is as follows.\\n')
print(text)