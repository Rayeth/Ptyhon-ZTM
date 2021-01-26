#What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!

new_list = ['a', 'b', 'c']
# b
print(new_list[1])
# b
print(new_list[-2])
# [b, c]
print(new_list[1:3])
new_list[0] = 'z'
# [z, b, c]
print(new_list)

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
# [z, 2, 3, 5]
print(my_list)
# [1, 2, 3, 5]
print(bonus)