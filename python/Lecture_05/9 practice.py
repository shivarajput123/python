# # # # def string(s):
# # # #     d = {"upper_case":0,"lower_case":0,"digit":0}
# # # #     for i in s:
# # # #         if i.isupper():
# # # #             d["upper_case"]+=1
# # # #         elif i.islower():
# # # #             d["lower_case"]+=1
# # # #         elif i.isdigit():
# # # #             d["digit"]+=1
# # # #         else:
# # # #             pass
# # # #     print(d)
# # # #     print(d["upper_case"])
# # # #     print(d["lower_case"])
# # # #     print(d["digit"])
# # # # string('The123AbcD456E')




# # # def change_str(str1):
# # #     return(str1[-1]+str1[1:-1]+str1[0])
# # # print(change_str('Hello'))



# # import random
# # test_list=[1,4,5,6,3]
# # print("the original str:",str(test_list))

# # random.shuffle(test_list)
# # print("ofter shuffle str:",str(test_list))
# # # name = "anuj"
# # # print("hell " + name)




# def vowel_count(str):
#     count = 0
#     vowel = "aeiouAEIOU"
#     for i in str:
#         if i in vowel:
#             count =count+1
#     print("no. of vowel:",count)
# vowel_count("pythonprogramming")



def ispalindrome(str):
    return str == str[::-1]

str = input("enter the str:")
k = ispalindrome(str)
if k:
    print("yes palindrome")
else:
    print("no palindrome")