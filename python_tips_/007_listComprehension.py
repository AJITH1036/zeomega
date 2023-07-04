numbers = [56,86,84,57,93,75,94,58,67,49,78,85]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)



dictionary = {'first_element': 1, 'second_element': 2,
              'third_element': 3, 'fourth_element': 4}      
odd_value_elements = {key : num for (key,num) in dictionary.items() if num % 2 ==1 }    
print(odd_value_elements)