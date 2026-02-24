# a list is a collection of datatypes, we can store the element in a  seq  by help for  enclosing formate like square bracket
# a list is allowed for the indexing and slicing the elements or values 
# a list  is allowing a duplicates
# a list is a order of seq 
# its 
#syntax
#var=[value1,values2,etc..]
a=[10,"20",30]
print(a)
           # len(function)
# its used for count the number of elements or values prsent in the list
a=[1,2,3,4,10]
print(len(a))
              #indexing
# we can access the element by using the index values there are two types of indexing values 
            #positive and # negative indexing
#positive indexing its start from left to right (0 to len(seq))
#negative  indexing start from  right to left  -1 to -len(seq)

a=[1,2,34,4]
print(a[1])# 1 is the indexing value

a=[1,2,3,4,"mani"]
print(a[-1])
                 #slicing
#  we can  accessse  group of elements ,values ,data  by using slicing
    # in sliecing we have (start,stop,step) here start and step is a inbuild and stop is  not inbuild
a=['a',"b","c",3]
print(a[0:5:1])#here 0 is start value,5 is the stop value,and 1 is a step values


#to print from first to last number
a=[1,3,4,5,6,8,8,9,32,3,46.7,3,4,5]

print(a[0:len(a):1])# its use to find the length of the list

# to print the number one after after
a=[1,3,4,5,6,8,8,9,32,3,46.7,3,4,5]
print(a[0:len(a):2])# here  we add the step value to 2

#print the  all number from list
a=[1,3,4,5,6,8,8,9,32,3,46.7,3,4,5,] 
print(a[::])# here the start from 0 and end with end of  list step value is 1

       ### concatenation
# it used to join , merger the sequences + is a concatenation
a=[1,2,3]
b=[4,5,6]
print(a+b)

              ###mutiplication *, its used to repeat the values  in a one sequence
a=[1,2]
print(a*2)#the multplication nnumber shold alsways in the intergers

#         inbulid method
#what is inbulid method
# its have a separate  properties for a sepearte  datatype like list ,tuple 
# its used only for the seperate data types for example list has some like append ,extend,remove like that 

#append 
# its used for add the element in a sequence at a last position
# we can add a only one element in a list two more or empty its give an errror
# but we can add  a two or more element in a nested list

#For example1:
a=[10,20,30]
a.append("mani")
print(a)

#for example 2
a=[10,20,30]
a.append([10,20,30])
print(a)

#extend its used for add a more than one element in a sequence
a=[10,20]
a.extend(["10",20,"mani"])
print(a)

a=[10,20]
a.extend("mani")# without the square bracket its run the strinf in a sequence like "m","a","n","i"
print(a)

a=[10,20]
a.extend([[10,"mani"]])# ts used for add the nested list
print(a)

#insert 
# 
# without th index value its give a error
# its also used for insert the element in  a list by using a index value
a=[10,20,20]
a.insert(0,"mani")
print(a)

#pop
#without the index alue it will remove the last value in the sequences
# its  used for remove the element in a sequences
a=[10,20,30]
a.pop(1)
print(a)

a=[1,2,3]
a.pop()
print(a)

# remove
#its used for remove the value for a sequence by giving a var
a=[10,20]
a.remove(10)# without the value its give an error
print(a)

              ####copy###
# its used for duplicated the sequence
#there are the three typre of copy are 
 #general copy
 #shallow copy
 #deep copy


#general copy 
# its has the same id 
# its used to copy the sequences
#  its does not create new object 
# one duplicate chnage the main also change
# for example
a=[10,20,30]
b=a# b is general copy
print(b) 

 #shallowcopy 
# ist also used for dupllcated the  sequence or object
# Its has  different id 
# changE in duplicated not affted the main list
#we can access the outer sequences only
a=[10,20,50]
b=a.copy()
b.append(10)
print(b)
print(a) #o/p [10, 20, 50, 10] [10, 20, 50]

# deepcopy for use deep copy we nedd to a module
#we can access the outer and inner sequences 
from copy import deepcopy
a=[10,20]
b=deepcopy(a)
b.append([10,20])
print(b)
print(a)

# clear is used for delete the sequ
a=[10,20]
a.clear()
print(a)

a=[1,2,3,4]
print(a.count(1))