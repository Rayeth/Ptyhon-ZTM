some_list = ['a', 'b', 'c', 'b', 'm', 'n', 'n']

sorted_list = sorted(some_list)
for item in sorted_list:
    if sorted_list.count(item) > 1:
        print(item)
        sorted_list.remove(item)
    else:
        continue
    