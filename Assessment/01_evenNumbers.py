
# 1. Print even numbers from 10 to 100
def evenNumbers():
    for i in range(10,100) :
        if i%2 == 0 :
            print(i)




sample_dict = {'a': 1, 'b': 3, 'c': 5}
#   2. update above dict with new key 'd' and value = 10
def update_Dict():
    sample_dict.update({'d':10})
    print(sample_dict)




# 3. Get all the keys, values from sample_dict and update the value of existing key
def changeValues():
    for x,y in sample_dict.items() :
        sample_dict[x]= y + 1
    print(sample_dict)




# 4. Write a funcion to convert '1,2,3,4,5' to [1, 2, 3, 4, 5] 
def convertToList() :
    num = '1,2,3,4,5'
    num1 = num.split(',')
    print(num1)
    numlist = []
    for x in num1:
      numlist.append(int(x))
    print(numlist)
  

# 5. Write a function t convert [1, 2, 3, 4, 5] to '12345'
def convertToString() :
   numlist = [1, 2, 3, 4, 5] 
   new_String = ''
   for x in numlist:
      new_String += str(x)
   print(new_String)
 
 
   



sample_list = [1, 3, 5, 5, 6, 7, 7, 8, 8, 9, 10]
# 6. Return a list with unique values.
def duplicate(): 
    new_list = set(sample_list)   
    print( "New list is " + str(list(new_list)))



# 7. Sort the list and return the result based on the number of occurances.
def occurence() :
  
  new_list = set(sample_list)
  for x in new_list:
    count = sample_list.count(x)   
    print(f'count of {x} is {count}')




# evenNumbers()
# update_Dict()
# changeValues()
# duplicate()
# convertToString() 
convertToList()  
# occurence()


