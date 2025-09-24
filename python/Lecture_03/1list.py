#list in python

marks=[12,14,16,18]
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])


student = ["karan",95,84,"delhi"]
print(student)
student[0] = "arjun"
print(student)


#list slicing

marks = [85,94,76,63,48]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

#list methods

list = [2,1,3]
print(list.append(4))
print(list.sort())
print(list.sort(reverse=True))
print(list.reverse())
print(list.insert(1,5))
print(list.remove(5))
print(list.pop(3))
print(list)
