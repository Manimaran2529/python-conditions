## set is also a collection of data we can store the data with the help for curl braces and the elements are sepreate by the comma
##its is unorder collection of data
##its mutable
##its does not support the duplicates
##its does not support the concatnation and mutlipication
## its does not support indexing and slicing 
# we can modify the elemets

                 ##inbulid methods
                    ## add 
# its used to add the elments in the set
a={1,"maran",3,4}
a.add("mani")
print(a)


                    ## remove  
# #its used to remove the elemets in the set by using the aruguments
a={1,"maran",3,4}
a.pop("maran")
print(a)

                           ##pop 
# its also used to remove an  random elements  in the list
a={1,22,33}
a.remove(1)
print(a) 

                                           ##discard 
# its used to remove the elements in the set if the elemenats is not present its does not rise an error
a={1,2,3,4,5}
a.discard("mani")
print(a)


                                      ##union 
# its used to add the one or more elements in a set its creatng a new set
a={1,2,3,45}
b={1,22,34,5,} 
c=a.union(b)
print(c)

                                ## update 
# its used to add the elements or iterable in the exist set not create an new set
a={1,2,3,45}
b={1,22,34,5,"manim"} 
a.update(b)
print(a)

                                 # copy

                           #general copy  
# its used for copy by using assigment operators we chnage one other aolso change  its return null
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
# its creating a new set  by comparing the two set which has common elements 
# 
a={1,23,4,}
b={1,"mani","maran"}
c=a.intersection(b)
print(c) #o/p={1}

a={1,23,4,5}
b={"harini","mani","maran"}
c=a.intersection(b)
print(c)# if any thing not present its return emptyy set

#intersection_update 
# its  update value if same values are present to update the  exit set  return type is null
# its does not create a nwe sets
a={1,2,3,5}
b={1,"mani"}
a.intersection_update(b)
print(a)

a={1,2,3,5}
b={1,"mani"}
a.intersection_update(b)
print(a)# any thing not present its return empty set

                              ##difference
#its creting a new set return type is set
#compared the two or more set its the elements are in same in remove in  the main set only 
a={1,2,3,"mani"}
b={"mani",10,20,30}
c=a.difference(b)
print(c)

                             ##different.update
#its not creating the  set its update to the exist set
#its return type is null
a={1,2,3,4,6}
b={1,2,3,"mani"}
a.difference_update(b)
print(a)#o/p=>{4,6}

                               ##symmetric_difference
#its  creat a new set by comparing the mutliple set if it has the same elements it remove its  and create the new set by the both elements
#return type is set
a={1,2,3,4,6}
b={1,2,3,"mani"}
c=a.symmetric_difference(b)
print(c)#o/p=>{'mani', 4, 6}


                        #symmetric_difference_upadte
#its same as the symmetric_difference but it update to the exist set
#return type is set
a={1,2,3,4,6}
b={1,2,3,"mani"}
a.symmetric_difference(b)
print(a)#o/p=>{'mani', 4, 6}    


                            ###isdisjoin
#its used for compare the two sets if the set has same elements its return false else true
#its return type is bollean its return false if one elements are same also false
a={1,2,3,4}
b={1,2,3,4}
c=a.isdisjoint(b)
print(c)#false

a={1,2,3,4}
b={5,6,78,8}
c=a.isdisjoint(b)
print(c)#true

                                 ##is subset(small in big)
#its also same as isdisjoin but its check the all the  elements 
#its return true if the all the elements are not same
a={1,2}
b={1,6,78,8}
c=a.issuperset(b)
print(c)#fale

a={1,2,}
b={1,2,3,4}
c=a.issuperset(b)
print(c)#true

                                ##is superset (big in small )
#its also same as isdisjoin but its check the all the  elements 
#its return true if the all the elements are not same
a={1,2,3,4}
b={1,6}
c=a.issuperset(b)
print(c)#false

a={1,2,3,4}
b={1,2}
c=b.issubset(a)
print(c)##true