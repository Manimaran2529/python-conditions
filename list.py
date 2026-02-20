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