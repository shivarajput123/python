#question-01

# movie1 = input("enter first movie:")
# movie2 = input("enter second movie:")
# movie3 = input ("enter third movie:")
# movies = [movie1,movie2,movie3]
# print(movies)
# print(type(movies))

# movies = []
# mov1  = input("enter 1st movie:")
# mov2  = input("enter 2st movie:")
# mov3  = input("enter 3st movie:")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)


# movies = []
# mov  = input("enter 1st movie:")
# movies.append(mov)
# mov  = input("enter 2st movie:")
# movies.append(mov)
# mov  = input("enter 3st movie:")
# movies.append(mov)

movies = []
movies.append(input("enter 1st movie:"))
movies.append(input("enter 2st movie:"))
movies.append(input("enter 3st movie:"))
print(movies)



#question-02

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("palendrome")
else:
    print("NOT palendrome")


#question-03

grade = ("C","D","A","A","B","B","A")
print(grade.count("A"))


grade = ["C","D","A","A","B","B","A"]
grade.sort()
print(grade)
