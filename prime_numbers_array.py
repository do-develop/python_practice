# Given k numbers which are less than n, return the set of prime number among them
# Note: The task is to write a program to print all Prime numbers in an Interval.

num = 100

def prime_number_array(num):
    prime_numbers = []
    for number in range(num):
        if number > 1: #all prime numbers are greater than 1
            for i in range(2, number):
                if(number % i) == 0:
                    break
            else:
                prime_numbers.append(number)
    return prime_numbers

print(prime_number_array(num))