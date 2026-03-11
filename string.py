# String is a datatype that holds a sequence of characters.

# We can store both cased and uncased characters in a string.

#its support both conacation and muliplication also

# String is immutable, so we cannot modify the string elements directly.

# It is an ordered collection of characters.

# It supports duplicate characters.

# It supports both indexing and slicing.

# If we add or remove characters, Python creates a new string
# with a new memory address. It does not modify the original string.

# Cased characters mean uppercase and lowercase letters.
# Example: A, B, C, a, b, c

# Uncased characters mean numbers and special characters.
# Example: 1, 2, 3, @, #, $

# We can store a string within:
# Single quotes (' ')
# Double quotes (" ")
# Triple quotes (''' ''' or """ """)

#basic creating od string

a="mani"
print(a)

#its support indexing 
a="mani"
print(a[0])#o/p=>m

#its support slicing 
a="mani_maran"
print(a[0:4])#mani

a="mani_maran"
print(a[-1:-5])

a="manimaran"
print(a[2:-1])

#inbulid methods:

                                         #lower 
a="MANI"
b=a.lower()
print(a)#mani

                                           #islower 
a="MANI"
a=a.islower()
print(a)#false

a="mani"
a=a.islower()
print(a)#true

                                       #upper 
a="mani"
b=a.upper()
print(b)#MANI

                                           #isupper
a="MANI"
a=a.isupper()
print(a)#true

a="mani"
a=a.isupper()
print(a)#FALSE

                                               #TITTLE
a="mani"
a=a.title()
print(a)#Mani

                                                     #istittle
a="Mani"
a=a.istitle()
print(a)#true



a="mani"
a=a.istitle()
print(a)#false
  
                            ##concatnation

a="mani"
b='maran'
c=a+b
print(c)#manimaran
                                 ###multiplication
a="manimaran"
c=a*2
print(c)#"manimaranmanimaran"