# Given an array containing None values fill in the None values with most recent
# non-None value in the array

array1 = [1, None, 2, 3, None, None, 5, None, 8, None]

def fillTheBlanks(array):
    valid = 0
    new_array = []
    for i in array:
        if i is not None:
            new_array.append(i)
            non_none = i
        else:
            new_array.append(non_none)
    return new_array

print(fillTheBlanks(array1))