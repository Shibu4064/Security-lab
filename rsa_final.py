# n=11329931
# p=0
# for i in range(2,n):
#     if n%i==0:
#         p=i
#         break
# print("p:-",p)

# q=int(n/p)
# print("q:-",q)

# phi_n=(p-1)*(q-1)
# print("phi_n:-", phi_n)

# def big_mod(x,e,n):
#     if e==1:
#         return(x%n)
#     k=big_mod(x,e//2,n)%n
#     res=(k*k)%n
#     if e%2==1:
#         res=(res*x)%n
#     return res

# d=617291
# e=big_mod(d,phi_n-1,phi_n)
# print("e:-",e)

# m=1545788
# c=big_mod(m,e,n)
# print("cipher text:-", c)

# dec=big_mod(c,d,n)
# print("decrypted msg:-", dec)



message = "thegranddesignbreaksthenewsbittertosomethattocreateauniversefromabsolutenothinggodisnotnecessaryallthatisneededarethelawsofnaturethatistherecanhavebeenabigbangcreationwithoutthehelpofgodprovidedthelawsofnaturepredatetheuniverseourconceptoftimebeginswiththecreationoftheuniversethereforeifthelawsofnaturecreatedtheuniversetheselawsmusthaveexistedpriortotimethatisthelawsofnaturewouldbeoutsideoftimewhatwehavethenistotallynonphysicallawsoutsideoftimecreatingauniversenowthatdescriptionmightsoundsomewhatfamiliarverymuchlikethebiblicalconceptofgodnotphysicaloutsideoftimeabletocreateuniverse"
d=617291
e=1186211
n=11329931
cipher=[]
for i in range(len(message)):
    pos=ord(message[i])-ord('a')+1
    cipher.append((pos**e)%n)
for i in range(len(cipher)):
    print(cipher[i])
# for i in range(len(cipher)):
#     pos=cipher[i]
#     ans=(pos**d)%n
#     ch=chr(ans-1+ord('a'))
#     print(ch,end="")