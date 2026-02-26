# its used to minimed the code of for loop in a single line 


#From a = [-5, 3, -2, 7]  Convert negative numbers to 0, keep positive same.
a = [-5, 3, -2, 7]
print([i if i >=0  else "0" for i in a ])


# From a = [100, 45, 60, 30] Store "Pass" if ≥ 50 "Fail" otherwise
a = [100, 45, 60, 30]
print(["pass" if i>=50  else "fail" for i in a])


# Create a list of tuples like: (number, square) for numbers 1 to 10
print([(i,i**2 ) for i in range(1,11)])

#From a list of words: ["apple", "hi", "banana", "cat"] Store only words with length > 3.
a=["apple", "hi", "banana", "cat"] 
print([ i  for i in a if len(i)>3 ])

# From 1 to 20, store numbers divisible by both 2 and 3.
print([i for i in range(1,21) if i%2==0 and i%3==0])

#Create a list of boolean values showing whether numbers from 1 to 10 are divisible by 3
print( [i%3==0 for i in range(1,10) ])


