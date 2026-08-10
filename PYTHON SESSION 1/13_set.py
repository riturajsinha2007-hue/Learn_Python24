# sets = { 1, 2, 3 ,4 , 5, 6,7 ,5,5,6 }

# empty_set = set() #empth set , this is not sets = {}

# print(sets)

# sets.add(55)

# print(sets, type(sets))

s = {10, 20, 30}

# 8. add()
s.add(40)
print(s)  
# Output: {10, 20, 30, 40}

# 9. remove()
s.remove(20)
print(s)  
# Output: {10, 30, 40}

# 10. discard() (no error if element not found)
s.discard(50)
print(s)  
# Output: {10, 30, 40}

# 11. pop() (removes random element)
print(s.pop())  
# Output: (random element, e.g., 10)

# 12. clear()
s.clear()
print(s)  
# Output: set()
