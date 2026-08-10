#list is container to store a set of values any datatype

frinds = [ "akash",69, 96.96, True, "blue" , "rohen" , "lund" ]
print(frinds[5])
frinds[5] = "laudha"  #unlike string list are mutable


print(frinds[0:])  #to print range of datatype
print(frinds[1:4])


# Example: pick the 5th element ("blue") and then the 4th letter
print(frinds[4][3])   # Output: 'e'
print(frinds[6][0])   # 'l' from "lund"