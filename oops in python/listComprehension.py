

even = []
odd = []

list = [even.append(i) if i%2 == 0 else odd.append(i)  for i in range(10,100) ]

char = [ character for character in "Geeks"]

# print(char)

num = int(input("Enter number"))
std = [i**3 for i in range(num)]
# print(std)


check = [f"{i} is even number" if i%2 == 0 else f'{i} is odd number' for i in range(10)]
print(check)

