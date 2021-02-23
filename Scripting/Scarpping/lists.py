from itertools import chain

li = [[1,2,3,4,5],[4,6,7,3,4]]
t=[['a', 'b', 'c'],['d', 'e', ['f']]]


def list_sum(li):

    sum_li = sum(li, [])

    return sum_li

#print(list_sum(t))



# def chain_func(*args):

#     for arg in args:
#         mega_chain = list(chain.from_iterable(arg))
#         print(mega_chain)

# chain_func(t, li)

flat_list = []

for sublist in t:
    for item in sublist:
        flat_list.append(item)

print(flat_list)









