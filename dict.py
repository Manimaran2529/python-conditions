## its a  non-primitive datatypes  we can  store the values in the form of key values  for  each value their is an seperate key
# its  support both homogenes and hetorogences datatypes
## its mutable 
## its a sequence of order 
##its support dulpicates values but does  not support the duplicates key if  we  give duplicate keys is over written to te previous  value
# its does no suppport of indexing and slicing if we want to acess single values we  can use  by the key
#its does   ot support concatation and multiplication  we  using (+)operatores we can add the by using the inblud method

## to create a dic
a={"a":"apple","b":"ball"}
print(a)


                    ##update
# to add a new items in a list we use a update method there are three method
#1st method
a={"a":"apple","b":"ball"}
a.update([("c","cat"),("d","dog")])
print(a)
#2ndmethod in this we add only one item
a={"a":"apple","b":"ball"}
a.update({"c":"cat"})
print(a)
#3rdmethod
a={"a":"apple","b":"ball"}
a.update(c="cat",d="dog")
print(a)


                  #set default(its return types is none and user input)
# this method is used te get the values of the one varibale
#its return type is any and none 
# id the key are present is display the values if its not prensent its shows none
# and if the key is not present its add the key to the disc
a={"a":"apple","b":"ball"}
c=a.setdefault("a")
print(c)

#if the key are not present 
a={"a":"apple","b":"ball"}
b=a.setdefault("c","not present")
print(b,a)  # o/p => not present {'a': 'apple', 'b': 'ball', 'c': 'not present'}

#id we pass one arugument only
a={"a":"apple","b":"ball"}
b=a.setdefault("c") 
print(b,a)#o/p=>None {'a': 'apple', 'b': 'ball', 'c': None}

                       ##pop its used to delete the item in the disc and return the any or none
#if the values are present
a={
    "a":"mani",
    "b":"maran",
    "c":"harini"
}
a.pop("b")
print(a)# o/=> {'a': 'mani', 'c': 'harini'}


#if the values are not present 
a={
    "a":"mani",
    "b":"maran",
    "c":"harini"
}
a.pop("d")
print(a) #o.p=> key error 

#its also return the values
a={
    "a":"mani",
    "b":"maran",
    "c":"harini"
}
e=a.pop("c")
print(e)#o/p=> harini

                               ##get 
#its used to get the item from the dic and its does the modify the dic or did not add the missing item to the dict
a={
    "a":"mani",
    "b":"maran",
    "c":"harini"
}
c=a.get("a")
print(c)

                                ###pop.items
#its used to delete the last item from the dic
a={
    "a":"mani",
    "b":"maran",
    "c":"harini"
}
a.popitem()
print(a)

                                   ### from key
# when we have a diffrent key and  have a same values we use from key for creating
# we can pass the keys in the iteratble 
d={}.fromkeys[1,2,3,4],"py"
print(d)#o/p=> {1: 'py', 2: 'py', 3: 'py', 4: 'py'}

               ###copy
##there are three copy in dict(general copy,deepcopy,shallow copy)
#general copy and parent dic have a same memory adress we can the one other also change
a={
    1:2,
    "b":"apple"
}
b=a
b["c"]="mani"
print(b)#{1: 2, 'b': 'apple', 'c': 'mani'}
print(a)#{1: 2, 'b': 'apple', 'c': 'mani'}

#shallow copy
#the outer dic have different adresss the inner has same adress
a={
    1:2,
    "b":"apple"
}
b=a.copy()
b["c"]="mani"
print(b)#{1: 2, 'b': 'apple', 'c': 'mani'}
print(a)#{1: 2, 'b': 'apple'}

a={
    1:2,
    "b":["apple","cat"],
}
b=a.copy()
b["b"][0]="mani"
print(b)#{1: 2, 'b': ['mani', 'cat']}
print(a)#{1: 2, 'b': ['mani', 'cat']}


#deepcopy both also have a different adress so the parents dict did not change
#outer
import copy
a={
    1:2,
    "b":["apple","cat"],
    "c":"mani"
}
b=copy.deepcopy(a)
b["c"]="change"
print(b)#{1: 2, 'b': ['apple', 'cat'], 'c': 'change'}
print(a)#{1: 2, 'b': ['apple', 'cat'], 'c': 'mani'}

#inner 
import copy
a={
    1:2,
    "b":["apple","cat"],
}
b=copy.deepcopy(a)
b["b"][0]="mani"
print(b)#{1: 2, 'b': ['mani', 'cat']}
print(a)#
{1: 2, 'b': ['apple', 'cat']}

               ##clear
#its used to empty the dictinary remove all the keys and values in the dict and return the empty dict
a={1: 2, 'b': ['apple', 'cat'], 'c': 'mani'}
a.clear()
print(a) #o/p={}

                      ###keys
#its used to only print the keys present in the dict
a={1: 2, 'b': ['apple', 'cat'], 'c': 'mani'}
b=a.keys()
print(b)#o/p=([1, 'b', 'c'])

                         #values
#its used to print only the values present in the dict 
a={1: 2, 'b': ['apple', 'cat'], 'c': 'mani'}
b=a.values()
print(b)#o/p=([2, ['apple', 'cat'], 'mani'])

                          #items
# its used to print the both keys and values in the form of tuple 
a={1: 2, 'b': ['apple', 'cat'], 'c': 'mani'}
b=a.items()
print(b)#o/p=([(1, 2), ('b', ['apple', 'cat']), ('c', 'mani')])

                               #looping
#in dict we use only the for loop
a={1: 2, 'b': ['apple', 'cat'], 'c': 'mani'}

for i in a:
    print(i) #its only print the keys only  1 b c 

a={1: 2, 'b': ['apple', 'cat'], 'c': 'mani'}

for i in a.values():
    print(i,end=" ")#its used to print only the values  2 ['apple', 'cat'] mani 


a={1: 2, 'b': ['apple', 'cat'], 'c': 'mani'}

for i in a.items():
    print(i,end=" ")# its used to print the both keys and values  (1, 2) ('b', ['apple', 'cat']) ('c', 'mani') 


##comprehension
a = {1: 2, 'b': 'apple', 'c': 'mani'}

b = {k:v for k,v in a.items()}

print(b)#o/p={1: 2, 'b': 'apple', 'c': 'mani'}