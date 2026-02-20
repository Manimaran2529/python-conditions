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


