marks = { "rahan": 34 ,
         "rahul": 57 ,
         "rajeev": 87 ,
          "champak": 67 ,
           90   :"raj" }

# print(marks)
# print(marks,type(marks))
# print(marks["rahan"])

# print(marks.items()) #provide touples

# print(marks.keys())
# print(marks.values())

# marks.update({"rahan" : 89 , ...}) # to update the dictionary

# print(marks)

# print(marks.get("rahan")) #if key doesnt exits it return none

# print(marks["rajeev"]) # unlesss returns error

# 6. pop(key)
marks.pop("rahul")
print(marks)  
# Output: {'name': 'Rituraj', 'age': 21}

# 7. popitem()
print(marks.popitem())  
# Output: ('age', 21)
print(marks)  
# Output: {'name': 'Rituraj'}

# 8. clear()
marks.clear()
print(marks)  
# Output: {}

# 9. copy()
new_dict = {"a": 1, "b": 2}
copy_dict = new_dict.copy()
print(copy_dict)  
# Output: {'a': 1, 'b': 2}