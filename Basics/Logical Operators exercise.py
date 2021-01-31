is_magician = False
is_expert = False

# check if magician and expert: "you are a master magician"
if is_magician and is_expert:

    print('You\'re a master magician')

# check if magician but not expert: "at least you're getting there"
elif is_magician and not is_expert:

    print('At least you are getting there')

# if you are not a magician: "You need magic powers"
# optional : elif not is_magician:
else:

    print('You need magic powers')



