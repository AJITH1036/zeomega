   

num = '1,2,3,4,5'
num1 = num.split(',')
print(num1)

numlist = []

# converting string to list 
def convertToList() :
    for x in num1:
      numlist.append(int(x))
    print(numlist)
    



# converting list to string
def convertToString() :
   new_String = ''
   for x in numlist:
      new_String += str(x)
   print(new_String)



convertToList() 
convertToString()   
   
   