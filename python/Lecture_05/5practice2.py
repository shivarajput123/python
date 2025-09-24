# #ques-01

# list = [1,4,9,16,25,36,49,64,81,100]

# for element in list:
#     print (element)

#ques-02

tup = (1,4,9,16,25,36,49,64,81,100,49)
x = 49

idx = 0
for el in tup:
    if(el==x):
        print("number is present in tuple",idx)
    idx += 1

