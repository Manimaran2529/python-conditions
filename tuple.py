# tuple  is collection of element in  a single variable  
# we can not  modify the elemets  
# tuple is denote by paranthesis  without praranthenis 
# tuple is also ave indexing ans slicing
#its a homogences and heterogences 
#its also allowing a duplicates 
# its also a order of sequences
#its also support the concatination and muliplication
                    

                   #error
a=10,20,30
a[0]="mani" # type errror we did not modify the elements
print(a)

a=10,20,30
a.append(10)#AttributeError: 'tuple' object has no attribute 'append'
print(a)

                     # inbulid method 

# its as only the two inblid methods are #count , index
# count 
a=10,20,30,10
print(a.count(10))# its used for ham many time the elements occurences

#index
a=10,20,30
print(a.index(10)) # its used to find the elements index value 

