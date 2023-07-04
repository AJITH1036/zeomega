def main():
    while True :
        try:
            number = int(input("Enter a number : "))
        except ValueError:
            print('Entered value is not a number ! please check... ')
        else:
            break
    print(f'Number is {number}')    

main()     