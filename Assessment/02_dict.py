

sample_dict = {'a': 1, 'b': 3, 'c': 5}
print(sample_dict.keys())






def update_Dict():
    sample_dict['d'] = 10
    sample_dict.update({'e':5})
    print(sample_dict)


def changeValues():
    for x,y in sample_dict.items() :
        sample_dict[x]= y + 1
    print(sample_dict.keys())

