# def wordgame() :
 
#     answer = "hello"
#     chancesLeft = 3
#     guessed_letters = []

#     while chancesLeft > 0 :
#         displayWord = ''
        
#         for letter in answer :
#             if letter in guessed_letters :
#                 displayWord += letter
#             else:
#                 displayWord += '_'
#             displayWord += ' '
#         print(displayWord.strip())
#         print(f'{chancesLeft} chances left')
#         print(f'guessed letters :  {guessed_letters}')

#         guess = input("guess a letter : ")
#         guessed_letters.append(guess)

#         if guess in answer :
#             print("Correct")
#         else:
#             print("Nope :(")
#             chancesLeft -= 1

#         won = True
#         for letter in answer :
#             if letter not in guessed_letters :
#                 won = False
#                 break

#         if won :
#             print("You win !")
#             return    
#     print("Sorry you lost !")
#     print(f'Answer is {answer}')

# wordgame()


    


def wordguess() :
    answer = "Hello"
    chances_left = 5
    guessedLetters = []

    while chances_left > 0 :
        displayWord = ""   
   
        for letter in answer :
            if letter in guessedLetters :
                displayWord += letter
            else:
                displayWord += "_"
            displayWord += " "
        print(displayWord.strip())
        print(f"{chances_left} chances left")
        print(f'guesses : {guessedLetters}')

        guess = input("Guess a letter")
        guessedLetters.append(guess)
        if guess in answer :
            print("correct")
        else:
            print("Nope :(")
            chances_left -= 1

        won = True
        for letter in answer:
            if letter not in guessedLetters:
                won =False
                break
        if won:
            print("You win !")
            return
    print("Sorry you lose") 
    print(f"Answer is {answer}")

        

wordguess()       