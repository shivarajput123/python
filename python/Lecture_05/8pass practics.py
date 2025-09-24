for i in range(10):
    pass
print("Loop finished")



n = 10
sum = 0
for i in range(1,n+1):
    sum += i
print("total sum =",sum)


n = 10
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum =",sum)


n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print ("factorial =",fact)