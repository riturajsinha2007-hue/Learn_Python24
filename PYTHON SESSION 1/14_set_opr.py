s1 = {2 , 34 , 56 , 78, 6 }
s2 = {56 , 34 , 787 , 98 , 2 , 90 ,6}

# 1. Union (combine elements)
# print(s1 | s2)  
print(s1.union(s2)) #union

# 2. Intersection (common elements)
# print(s1& s2) 
print(s1.intersection(s2))  #intersection

# 3. Ds1fference (elements in A but not in B)
# print(s1 - s2)  
print(s1.difference(s2)) 

# 4. Symmetric Difference (elements in either A or B but not both)
print(s1^ s2)  
print(s1.symmetric_difference(s2))


A = {1, 2, 3}
B = {1, 2, 3, 4, 5}

# 5. issubset()
print(A.issubset(B))  
# Output: True

# 6. issuperset()
print(B.issuperset(A))  
# Output: True

# 7. isdisjoint()
C = {6, 7}
print(A.isdisjoint(C))  
# Output: True
