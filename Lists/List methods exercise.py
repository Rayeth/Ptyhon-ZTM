# using this list, 
cart = ["Banana", "Apples", "Oranges", "Blueberries"]

# 1. Remove the Banana from the list
cart.remove("Banana")

# 2. Remove "Blueberries" from the list.
cart.remove("Blueberries")
# 3. Put "Kiwi" at the end of the list.
cart.append("Kiwi")
# 4. Add "Apples" at the beginning of the list
cart.insert(0, "Apples")
# 5. Count how many apples in the cart
print(cart.count("Apples"))
# 6. empty the cart
cart.clear()

print(cart)
