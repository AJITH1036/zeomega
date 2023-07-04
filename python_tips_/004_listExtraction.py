my_list = [1,2,3,4,5]

# print(my_list)

# print(*my_list)


def sum_of_elements(*arg) :
    total = 0
    for i in arg:
        total += i

    return total

result = sum_of_elements(*[1,2,3,4,5])
print(result)    
