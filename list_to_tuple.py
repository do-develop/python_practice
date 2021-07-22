# How to convert list to tuple

# Approach 1 - Using tuple(list_name)
def convert1(list):
    return tuple(list)

list = [1,2,3,4,5]
print(convert1(list))

# Approach 2 - Using a loop inside tuple()
def convert2(list):
    return tuple(i for i in list)

list = [1,2,3,4,5]
print(convert2(list))

# Approach 3 - unpack the list inside a tuple literal
def convert3(list):
    return (*list,)

list = [1,2,3,4,5]
print(convert3(list))