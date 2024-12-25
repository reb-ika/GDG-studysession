 #write a program to find the largest number in a list
def largest_number(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest
print(largest_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))