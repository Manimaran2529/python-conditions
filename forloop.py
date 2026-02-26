#to find the second largest values
"""a=[1,2,3,45,7,4]
largest=0
second=0
third=0

for i in a :
    if i>largest:
        second=largest
        largest=i
    elif i>second and second!=largest:
        third=second
        second=i
    elif i>third and i!=second:
         third=i
print("largest number",largest)
print("second largest",second)
print(third)"""

#Count Vowels in String s = "interview"
"""s = "interview"
v="aeiou"
count=0
for i in s:
    if i in v:
        count=count+1
print(count)"""

#Check Palindrome (Without Using [::-1]) s = "madam"
"""s = "madam"
m=""
for i in s:
    m=i+m
if m==s:
    print("Palindrome")
else:
    print("not Palindrome")"""

#Find Factorial of a Number n = 5
"""n = 5
fact=1
for i in range(n,0,-1):
    a=i*fact
    fact=a        
print(fact)"""

#Print Prime Numbers from 1 to 50
"""for i in range(2,51):
    for j  in range(2,i):
        if i%j == 0:
            break
    else:
         print(i)"""


"""a=int(input("enter a password length"))
mani="ab#$*cd2345ef!@#$%^&*()ghijkABCDEFG167890HIJKLMANOQRSTUVWZYZlmnopqrstuvwxyz"
seed=int(input("enter  a number to get different number"))
password=""
gen=mani
for i in range(a):
    index=(i*seed+7)%len(gen)
    password=password+gen[index]

print(password)"""

""" to print the numbers how many times its repated
a = [1, 2, 3, 4, 1]
b = []

for i in a:
    if i not in b:
        count = 0
        
        for j in a:
            if i == j:
                count = count + 1
        
        b.append(i)
        print(i, "=", count)

   """

#Given a string containing letters, digits, and symbols, determine if 
# it reads the same forwards and backwards 
# when considering only alphabetic characters (case-insensitive).
"""a=["M","A","M"]
B=[]
c=[]
for i in a:
    lo=i.lower()
    B.append(lo)

for j in B:
    c.insert(0,j)


if B==c:
    print("paladrome","1")
else:
    print("not paladrome","0")    """


""""a=int(input("enter a array size:"))
b=input("enter a datatypes you want:")
if b=="int":
    print([ int(input("enter a number"))  for _ in  range(0,a+1) ])
   
elif b=="decimal":
     print([ float(input("enter a number"))  for _ in  range(0,a+1) ])

elif b=="string":
     print([ input("enter a number") for _ in  range(0,a+1) ])"""
 

 
a=int(input("enter a number from 1-7"))

match a:
    case 1:
        print("monday")