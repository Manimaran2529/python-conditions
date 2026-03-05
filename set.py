## set is also a collection of data we can store the data with the help for curl braces and the elements are sepreate by the comma
##its is unorder collection of data
##its mutable
##its does not support the duplicates
##its does not support the concatnation and mutlipication
## its does not support indexing and slicing 
# we can modify the elemets

                 ##inbulid methods
## add its used to add the elments in the set
a={1,"maran",3,4}
a.add("mani")
print(a)


## remove  its used to remove the elemets in the set by using the aruguments
a={1,"maran",3,4}
a.pop("maran")
print(a)

##pop its also used to remove an  random elements  in the list
a={1,22,33}
a.remove(1)
print(a) 

##discard its used to remove the elements in the list if the elemenats is not present its does not rise an error
a={1,2,3,4,5}
a.discard("mani")
print(a)


##union its used to add the one or more elements in a set its creatng a new set
a={1,2,3,45}
b={1,22,34,5,} 
c=a.union(b)
print(c)

## update its used to add the elements or iterable in the exist set not create an new set
a={1,2,3,45}
b={1,22,34,5,"manim"} 
a.update(b)
print(a)

                                 # copy

#general copy  its used for copy by using assigment operators we chnage one other aolso change  its return null
a={1,"harini",3,45}
b==a
b.pop()
print(a)
print(b)


#shallow copy
#its also used for copy the elements in the exsiting list but one change other did not change 
a={1,"harini",3,45}
b=set.copy(a)
b.pop()
print(a)
print(b)

                     #intersection
                     #  is used to return the common value  from a set
a={1,23,4,}
b={1,"mani","maran"}
c=a.intersection(b)
print(c) #o/p={1}

a={1,23,4,5}
b={"harini","mani","maran"}
c=a.intersection(b)
print(c)# if any thing not present its return emptyy set

#intersection_update its  update value if same values are present to upadte the  exit set  return type is null
a={1,2,3,5}
b={1,"mani"}
a.intersection_update(b)
print(a)

a={1,2,3,5}
b={1,"mani"}
a.intersection_update(b)
print(a)# any thing not present its return empty set

                              ##difference
#its used for find the same elements in the set if the elements are same in two sets it remove it
a={1,2,3,"mani"}
b={"mani",10,20,30}
c=a.difference(b)
print(c)

