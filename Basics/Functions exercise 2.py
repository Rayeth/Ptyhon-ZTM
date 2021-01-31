def highest_even(li):
    even_li = []
    # check if even
    for item in li:
        if item % 2 == 0:
            even_li.append(item)
        else:
            continue
    #return max(even_li) instead of sorting
    sorted(even_li).reverse
    return even_li[0]
   

print(highest_even([10,2,3,4,8,11]))