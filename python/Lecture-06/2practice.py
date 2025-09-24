#ques -01
cities = ["delhi","gaziabad","gorakhpur","allahabad","banaras"]
movies = ["chhichhore","three idiot","dangal","sultan"]

def len_list(list):
    print(len(list))

len_list(cities)
len_list(movies)

#ques -02
cities = ["delhi","gaziabad","gorakhpur","allahabad","banaras"]
def print_list(list):
    for item in list:
        print(item,end=" ")
print_list(cities)


#ques -03
def fact_val(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
fact_val(5)

#ques-04
def convert(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =",inr_val,"NIR")
convert(100)
