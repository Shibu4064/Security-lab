def mod_pow(base,expo,mod):
    result=1
    while expo>0:
        if expo%2==1:
            result=(result*base)%mod
        base=(base*base)%mod
        expo=expo//2
    return result

def extended_gcd(a,b):
    if a==0:
        return 0,1,b
    gcd,x1,y1=extended_gcd(b%a,a)
    x=y1-(b//a)*x1
    y=x1
    return gcd,x,y

# def rsa_encrypt(m,e,n):
#     return mod_pow(m,e,n)

# def rsa_decrypt(c,d,n):
#     return mod_pow(c,d,n)

def main():
    n=670726081
    p=0
    for i in range(2,n):
        if n%i==0:
            p=i
            break
    q=int(n/p)
    phi_n=(p-1)*(q-1)
    print("p--",p)
    print("q--",q)
    d=12345
    gcd,x,y=extended_gcd(d,phi_n)
    if x>=0:
        e=x
    else:
        e=x+phi_n
    print("e--",e)
    m="ilove"
    e=33519389
    cipher=[]
    for i in range(len(m)):
        pos=ord(m[i])-ord('a')+1
        cipher.append((pos**e)%n)
    for i in range(len(cipher)):
        print(cipher[i])
    for i in range(len(cipher)):
        pos=cipher[i]
        ans=(pos**d)%n
        ch=chr(ans-1+ord('a'))
        print(ch,end="")

    # m=1545788
    # enc=rsa_encrypt(m,e,n)
    # dec=rsa_decrypt(enc,d,n)

    # print("public key pair: ",(e,n))
    # print("private key pair: ",(d,n))
    # print("plain text", m)
    # print("cipher text: ", enc)
    # print("decrypted msg: ", dec)
    # print("-------RSA Signature----------")
    # signature=mod_pow(m,d,n)
    # plain_text=mod_pow(signature,e,n)
    # print(m)
    # print(signature)
    # print(plain_text)
    # if(plain_text==m):
    #     print("signature is valid")
    # else:
    #     print("signature is not valid")

if __name__=="__main__":
    main()






# m="iwanttobuysomething"
# d=6176291
# e=11
# n=11329931
# cipher=[]
# for i in range(len(m)):
#     pos=ord(m[i])-ord('a')+1
#     cipher.append((pos**e)%n)
# for i in range(len(cipher)):
#     pos=cipher[i]
#     ans=(pos**d)%n
#     ch=chr(ans-1+ord('a'))
#     print(ch,end="")