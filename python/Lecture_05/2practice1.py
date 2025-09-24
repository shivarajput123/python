#ques-01

i = 1
while i <= 100:
    print(i)
    i += 1
print("loop ended")

#ques-02

i = 100
while i >= 1:
    print(i)
    i -= 1
print("loop ended")

#ques-03

n = int(input("enter the n number:"))
i = 1
while i <= 10:
    print(n*i)
    i += 1

#ques-04

list= [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(list):
    print(list[idx])
    idx += 1

#ques-05
num= (1,4,9,16,25,36,49,64,81,100,36)

x = 36

idx = 0
while idx < len(list):
    if (num[idx] == x):
        print("find at idx:",idx)
    else:
        print("finding...")
    idx += 1
