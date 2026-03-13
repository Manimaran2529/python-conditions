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
##its used to convert charatter into  a lower case 
a="MANI"
a=a.lower()
print(a)#mani

                                           #islower 
##its used to check the values is lower or not its return boolean values                                            
a="MANI"
a=a.islower()
print(a)#false

a="mani"
a=a.islower()
print(a)#true

                                       #upper 
##its used to convert charatter into  a upper case 
a="mani"
b=a.upper()
print(b)#MANI

                                        #isupper
##its used to check the values is upper or not its return boolean values    
a="MANI"
a=a.isupper()
print(a)#true

a="mani"
a=a.isupper()
print(a)#FALSE

                                        #TITTLE
# its convert the the each word first letter into a upper case
a="mani"
a=a.title()
print(a)#Mani

                                        #istittle
#its return the boolen values its the chartcter is n tiille its shoes true or false
a="Mani"
a=a.istitle()
print(a)#true

a="Mani Maran"
a=a.istitle()
print(a)#true

a="Mani maran"
a=a.istitle()
print(a)#false

a="mani"
a=a.istitle()
print(a)#false
  
                             ##capitalize
#its convert only the first letter in uppr like tittle
a="manimaran"    
a=a.capitalize()
print(a)#Manimaran

a="mani maran"
a=a.capitalize()
print(a)#Mani maran ## (but in tittle the iutpt becomes  Mani Maran)

                        ##concatnation
#its used to add a string 

a="mani"
b='maran'
c=a+b
print(c)#manimaran
                         ###multiplication
# its is used to mutplication the string 
a="manimaran"
c=a*2
print(c)#"manimaranmanimaran"

                           ####Swap case
# its used to  convert the charcater into oppsoise like upper into lower and lower into upper
a="Mani Maran"
a.swapcase()
print(a)#o/p=>mANI mARAN

a="mANI mARAN"
a=a.swapcase()
print(a)#Mani Maran


                               ###index
#if the value is  rise an error ishows -1 not an errror but in index its rise an error
#its used to find the index position of a character in a string
#its take three arugments values start and stop 
#its have two indexing one from left to  right and 
#rindex   its give  the last indexing position of a elements 
#if the value is  rise an error ishows  an errror not an -1
a="manimaran is a good boy"
b=a.index("a")
print(b)#o/p=>1

a="manimaran is a good boy"
b=a.index("a")
print(b)#o/p=>13(last occurences position of the charcters)

a="manimaran is a good boy"
b=a.index("a",2,6)# a is a value and 2 is the start and 6 is a stop
print(b)#o/p=>5


a="manimaran is a good boy"
b=a.index("22")
print(b)#o/p=>error 

                                ##find (its smiliar to the index method)
#if the value is  rise an error ishows -1 not an errror but in index its rise an error
#its used to find the index position of a character in a string
#its take three arugments values start and stop 
#its have two indexing one from left to  right and 
# rfind  its give  the last indexing position of a elements 
#if the value is  rise an error ishows -1 not an errror
 
a="manimaran is a good boy"
b=a.find("a")
print(b)#o/p=>1

a="manimaran is a good boy"
b=a.rfind("a")
print(b)#o/p=>13(last occurences position of the charcters)

a="manimaran is a good boy"
b=a.find("a",2,6)# a is a value and 2 is the start and 6 is a stop
print(b)#o/p=>5


a="manimaran is a good boy"
b=a.find("22")
print(b)#o/p=>-1 

                               ###count 
#its used to  count the  ocuunerences of the charactes how many times ist preset
#its take three aruguments but other non primituve one aruguments only

a="manimaran is a very good boy"
b=a.count("m")
print(b)#o/p=> 2


a="manimaran is a very good boy"
b=a.count("m",3,6)#start and stop values
print(b)#o/p=>1


                     ##split
#its used to split the string and return in the list
a="Manimaran is a very goodboy"
b=a.split()
print(b)#o/p=>['Manimaran', 'is', 'a', 'very', 'goodboy']

a="Manimaran is a very goodboy"
b=a.split("i") #its remove i and split wherever the i present 
print(b)#o/p=>['Man', 'maran ', 's a very goodboy']

#maxsplit(its used to detemine how many slipt we want )
a="Manimaran is a very goodboy"
b=a.split( maxsplit=1)#its split one times see the comma
print(b)#['Manimaran', 'is a very goodboy']

a="Manimaran is a very goodboy"
b=a.split( maxsplit=2)#its split the sring into two see the comma
print(b)#['Manimaran', 'is', 'a very goodboy']

                              ##splitlines
#whereever we use the backslash n (\n) that time we use splitline for split the string 
a="Manimaran\nis\na\nnever\ngoodboy"
b=a.splitlines()
print(b)#['Manimaran', 'is', 'a', 'never', 'goodboy']

a="Manimaran\nis\na\nnever\ngoodboy"
b=a.splitlines(keepends=True)
print(b)#['Manimaran\n', 'is\n', 'a\n', 'never\n', 'goodboy']


                              ##strip(its default remove the space in the starting and ending)
#its used to remov the characters in a string 

a="     manimaranmmmmm         "
print(a.strip( ))#(manimaranmmmmm)#its remove the spaced default

a="manimaranmmmmm"
b=a.strip("m")#its remove only the m in the first and last side
print(b)#animaran

a="manimaranmmmmm"
b=a.strip("ma")#its does not excuted group of character is extues char bu char
print(b)#nimaran


#lstrip(its only remove the left character only )
a="manimaranmmmmm"
b=a.lstrip("m")#its excuted only in the left side not right side
print(b)#animaranmmmmm

#rstrip(its only remove the right character only )
a="manimaranmmmmm"
b=a.rstrip("m")#its excuted only in the right side not left side
print(b)#manimaran

#removeprefix(its remove only the charcter at time based upon the feed)
a="mmanimaran"
b=a.removeprefix("m")#remove only one m  in the left side 
print(b)#manimaran

a="mmanimaran"
b=a.removeprefix("mm")#remove two mm in the leftside 
print(b)

#removesuffix its remove the charcter ina right side  
a="mmanimaranmm"
b=a.removesuffix("mm")#remove two mm in the rightside 
print(b)#mmanimaran

a="mmanimaranmm"
b=a.removesuffix("m")#remove only one m in the rightside 
print(b)#mmanimaranm