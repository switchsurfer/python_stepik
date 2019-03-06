def modify_list(l):
    l[:] = [i//2 for i in l if not i % 2]

lst = [1,2,3,4,5,6]
print(modify_list(lst))
print(lst)
modify_list(lst)
print(lst)