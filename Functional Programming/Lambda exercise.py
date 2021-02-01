my_list = [5,4,3]

#list that contans sqaure values fo my_list

print(list(map(lambda item: item**2, my_list)))

#List Sorting based on second value

a= [(0,2), (4,3), (9,9), (10,-1)]

a.sort(key = lambda x: x[1])

print(a)