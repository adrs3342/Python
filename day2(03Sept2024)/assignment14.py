i=input("Enter a tuple of integers separated by commas: ")
my_tuple=tuple(int(x) for x in i.split(","))
sort_tuple= tuple(sorted(my_tuple))
t=int(input("Enter the threshold value:"))
print("The sorted tuple in ascending order is: ",sort_tuple,"\n The filtered elements are: ",sort_tuple[sort_tuple.index(t):])