#question-01

dict = {
     "cat" : "a small animal",
     "table" : ["a piece of furniture", "list of facts & figures"]
 }
print(dict)


#question-02

subject = {"python","java","c++","python","javascript","java","python","java","c++","c"}

print(subject)
print(len(subject))


#question-03
mark = {}

x = int(input("enter phy :"))
mark.update({"phy":x})

y = int(input("enter chem :"))
mark.update({"chem":y})

z = int(input("enter math :"))
mark.update({"math":z})

print(mark)


#question-04
value = {9,"9.0"}
print (value)

#OR
value = {
    ("flaot",9.0),
    ("int",9)
}
print (value)