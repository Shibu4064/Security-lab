n=11329931
p=0
for i in range(2,n):
    if n%i==0:
        p=i
        break
print(p)

q=int(n/p)
print(q)

phi_n=(p-1)*(q-1)
print(phi_n)

def big_mod(x,e,n):
    if e==1:
        return(x%n)
    k=big_mod(x,e//2,n)%n
    res=(k*k)%n
    if e%2==1:
        res=(res*x)%n
    return res

d=6176291
e=big_mod(d,phi_n-1,phi_n)
print(e)

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