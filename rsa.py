def egcd(a,b):
    if b==0:
        return a,1,0
    d,x1,y1=egcd(b,a%b)
    x=y1
    y=x1-y1*(a//b)
    return d,x,y

def find_modular_inverse(e,phi):
    g,x,y=egcd(e,phi)
    if g!=1:
        return -1
    else:
        return(x%phi+phi)%phi

def big_mod(a,b,m):
    if b==0:
        return 1
    x=big_mod(a,b//2,m)
    x=(x*x)%m
    if b%2==1:
        x=(x*a)%m
    return x

def encrypt(m,e,n):
    v=[]
    for char in m:
        val=ord(char)-ord('a')+1
        ans=big_mod(val,e,n)
        v.append(ans)
    return v

def decrypt(c,d,n):
    s=""
    for val in c:
        ans=big_mod(val,d,n)
        s=s+chr(ans-1+ord('a'))
    return s

def find_p(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return i
    return 1

def print_num(x):
    if x<0:
        print("-",end="")
        x=x-x
    if x>9:
        print_num(x//10)
    print(x%10,end="")

def main():
    n=670726081  
    d=12345
    p=find_p(n)
    q=n//p
    phi=(p-1)*(q-1)
    e=find_modular_inverse(d,phi)

    print("public key pair: ", end=" ")
    print_num(d)
    print(" ",end="")
    print_num(n)
    print()
    print("private key pair: ", end=" ")
    print_num(e)
    print(" ",end="")
    print_num(n)
    print()

    m="hellomonicahowyoudoing"
    encrypted_msg=encrypt(m,e,n)
    decrypted_msg=decrypt(encrypted_msg,d,n)

    print("encrypted msg: ", end="")
    for num in encrypted_msg:
        print_num(num)
        print(" ", end="")
    print()
    print("decrypted msg: ", decrypted_msg) 

if __name__=="__main__":
    main()