# Given an array nums, write a function to move all zeroes to the end of it
# while maintaining the relative order of the non-zero elements.

array1 = [0,1,2,0,3,0,4,0,5]
array2 = [1,7,8,10,0,3,0,2,5,0,9]

def moveZeroToTheEnd(num_arr):
    for i in num_arr:
        if 0 in num_arr:
            num_arr.remove(0)
            num_arr.append(0)
    return num_arr

print(moveZeroToTheEnd(array1))
print(moveZeroToTheEnd(array2))