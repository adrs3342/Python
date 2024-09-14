#WAP to count number of occurence in an alpha string

string = input("Enter a string: ")
d = {}
# for i in range(len(string)):
#     if string[i].isalpha():
#         if string[i] in d:
#             d[string[i]] += 1
#         else:
#             d[string[i]] = 1
#
# for key in d:
#     print(f"Number of occurrence of __|{key}|__ in string is {d[key]}")

d = {k : string.count(k) for k in string if k not in d and k.isalpha()}
print(d)