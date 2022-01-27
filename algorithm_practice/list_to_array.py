from array import array

# initialise list
test_list = [3, 5, 7, 9, 11]
print("The original list: " + str(test_list))

# convert list to Python array
test_array = array("i", test_list)

# print the conversion result
print("List is converted to array: " + str(test_array))
