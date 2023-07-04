

sample_list = [1, 3, 5, 5, 6, 7, 7, 8, 8, 9, 10]
new_list = set(sample_list)

def duplicate():    
    print(list(new_list))

duplicate()


def occurence() :
  for x in new_list:
    count = sample_list.count(x)   
    print(f'count of {x} is {count}')
          
occurence()


