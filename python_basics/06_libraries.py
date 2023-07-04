import random

def toss():
   coin = random.choice(["heads","tails"])
   print(coin)

# toss()

def guessingGame():
   num = random.randint(1,10)
   guess = int(input("Enter your guess: "))
   if(num == guess) :
        print("you are correct")
   else:
       print(f"Wrong ! the number is {num}")

# guessingGame()
       

def shuffle():
    cards = ["king","queen","jack"]
    random.shuffle(cards)
    for card in cards :
        print(card)

shuffle()