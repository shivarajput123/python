collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("apnacollege")
collection.add((1,2,3))

collection.remove(1)

collection.clear()

print(len(collection))




print(set.pop())# set = {"hello","apnacollege","world","coding","python"}

print(set.pop())



set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))