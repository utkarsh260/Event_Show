#   List Manipulation

my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)

my_list[1] = 4

my_list.remove(3)
print('my_list: ', my_list)

# --------------------------------------------------------------------------------------------------------------------

#   List Comprehension
squares = [x**2 for x in range(1, 11)]

print('squares: ', squares)


# --------------------------------------------------------------------------------------------------------------------

#   List Sorting

names = ["Alice", "Eve", "Charlie", "David", "Bob"]

# Sort the list in alphabetical order
names.sort()

# Print the sorted list
print('names: ', names)

# --------------------------------------------------------------------------------------------------------------------
#   List Concatenation

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenate the two lists
combined_list = list1 + list2

# Print the combined list
print(combined_list)

# --------------------------------------------------------------------------------------------------------------------

#   List Reverse

numbers = [1, 2, 3, 4, 5]

# Reverse the list
numbers.reverse()

# Print the reversed list
print(numbers)
