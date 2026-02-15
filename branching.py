                  #if else"

#Write a program to check whether a number is positive or negative.
"""a=int(input("enter a number to check positive or negative:"))
if a>=0:
   print("positive numbers" )
else:
    print("neagtive number")"""

#Check whether a number is even or odd.
"""a=int(input("enter a number to check add or even:"))
if a%2==0:
    print("even number",a)
else:
    print("odd number",a)"""

#Check whether a person is eligible to vote (age ≥ 18).
"""age=int(input("enter your age:"))
if(age>=18):
    print("your are eligible for vote")
else:
    print("your are not eligible for vote")"""

#check whether a number is divisible by 5
"""number=int(input("Enter a number for checking:"))
if (number%5==0):
    print(number,"its divible by 5")
else:
    print(number,"its not divisble by 5 ")"""
#Check whether a character is a vowel or consonant.
"""vowels="aeiou"
special="@#!$%^&*(){}[];"
word=input("enter a word:")
if any(letter in vowels or letter in special for letter in word):
    print("not consonant")
else:
    print("consonants")"""

                      # if-elif

#Write a program to find the greatest of two numbers.
"""a=10
b=20
if a<b:
    print("b is greater")
if a>b:
    print("b is greater")
else:
    print("equal)"""

#Write a program to find the greatest of two numbers.
"""a=int(input("enter a  first number:"))
b=int(input("enter a second number:"))
c=int(input("enter a third number:"))
if a>b and a>c:
    print(a,"a is greater")
elif b>a and b>c:
    print(b,"b is greater")
elif c>a and c>b:
    print(c,"c is greater")
else:
    print("equal")"""

#Input marks and print grade 90–100 → A 80–89 → B 70–79 → C 60–69 → D Below 60 → Fail
"""mark=int(input("enter a mark to check grade:"))
if 100>=mark>=90:
    print("A grade🧡")
elif 89>=mark>=80:
    print("B grade👌")
elif 79>=mark>=70:
    print("c grade 🙌")
elif 69>=mark>=60:
    print("D grade 👍")
else:
    print("fail 😔")"""
#Check whether a year is a leap year.
"""year=int(input("enter a year:"))
if year%4==0 and year%100!=100:
    print("leap year")
elif year%400==0:
    print("leap year")
else:
    print("not leap year")"""
#Create a simple calculator (+, -, *, /) using if-elif.
"""a=int(input("enter a first number:"))
b=int(input("enter a second number:"))
c=input("enter a operation +,-,*,//,%:")
if c=="+":
    print("the addition of  a and b is:",a+b)
elif c=="-":
    print("the sub of a and  b is:",a-b)
elif c=="*":
    print("the multiplication of a and b is:", a*b)
elif c=="//":
    print("the floor division of a and b  is:",a//b)
elif c=="%":
    print("the modolus of a and b is:",a%b)
elif c=="/":
    print("the divided of a and b :",a/b)
else:
    print("enter a valid operation")"""
    
                  #nested if
#Write a program to approve or reject a loan based on salary and credit score conditions.
"""sal=int(input("enter your salary amount:"))
if sal>=20000:
    credit=int(input("enter your  credit score:"))
    if 200<=credit<=500:
        loan=int(input("enter your loan amount💵:"))
        if loan<=100000:
            print("loan approved successfully 🥳",loan)
        else:
            print("loan amount is maxmium 😑",loan)
    else:
       print("low credit score👎")
else:
    print("low salary we did not provide a loan🥲")"""       

#Write a program to check whether a year is leap year and if February has 28 or 29 days.
"""year=int(input("enter a year:"))
month=input("enter a month").lower()
if year%4==0 and year%100!=0 or year%400==0:
    print("leap year")
    if month=="feb":
        print("it have 29 days")
    else:
        print("it have 28 days")
else:
    print("not leap year")"""

        ###Real-world Logic (Interview Type)
#Check whether a number is a palindrome (like 121).
"""a=input("enter a number")
b=""

for i in a:
    b=i+b
if b==a:
        print("palindrom")
else:
        print(" not palindrom")"""

#Check whether a character is:UppercaseLowercaseDigitSpecial character
"""a=input("enter a word:")
upper="ABCDEFGHIJKLMNOPQRSTUVWXYY"
lower="abcdefghijklmnopqrstuvwxyz"
digit="123456789"
if any( letter in upper for letter in a):
    print("uppercase")
elif any(letter in lower for letter in a):
    print("lowercase")
elif any( letter in digit for letter in a):
    print("digits")
else:
    print("special character")"""