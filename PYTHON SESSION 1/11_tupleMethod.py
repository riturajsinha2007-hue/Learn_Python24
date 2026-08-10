a = (1 , 22, 45 , 22 , "lund" , "ganja" , 69.69 , True )

print(a)
number = a.count(22) #it will count the index number of first 22 only
print(number)

print(a.index("lund"))   # Output: 4

print(len(a))  #length of touple

#python only have 2 methods..

#touple oprationnnnn
c = (1, 2, 3)
b = (4, 5)
#c+b= concatnation
print(c + b)   # (1, 2, 3, 4, 5) Concatenation


n = (1, 2)
# repeation Nx3
print(n * 3)   # (1, 2, 1, 2, 1, 2) repeation


m = (10, 20, 30)
print(20 in a)   # True
print(40 not in a)   # True membershi test


# ndexing & Slicing is same as list ,
# touple just creat a new touple (imutabl)


# Tuple Unpacking

# Advanced Uses
# Tuples as dictionary keys

# Returning multiple values from functions