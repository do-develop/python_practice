# Using Ternary Operator
a, b = 10, 20
print("Both a and b are equal" if a == b
        else "a is greater than b"
        if a > b
        else "b is greater than a")

# Could be written as nested if-else
if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")
