import random

money = 100

#Write your game of chance functions here

#FLIP_COIN FUNCTION----------------------------------
def flip_coin(bet, call):
  if bet > money or bet <= 0:
    print("Not enough money, try again")
    
  else:
    coin = random.randint(0,1)
  
    heads_or_tails = ""
    if (coin == 1):
      heads_or_tails = "Tails"
      if(heads_or_tails == call):
        return bet
      else:
        return bet * -1
    else:
      heads_or_tails = "Heads"
      if(heads_or_tails == call):
        return bet
      else:
        return bet * -1    
    
#ROLL_DICE FUNCTION----------------------------------
def roll_dice(bet, call):
  if bet > money or bet <= 0:
    print("Not enough money, try again")
    
  else:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result = dice1 + dice2
    odd_or_even = ""
  
    if (result == 1) or (result == 3) or (result == 5) or (result == 7) or (result == 9) or (result == 11):
        odd_or_even = "Odd"
        if(odd_or_even == call):
          return bet
        else:
          return bet * -1
    else:
        odd_or_even = "Even"
        if(odd_or_even == call):
          return bet
        else:
          return bet * -1
      
#PICK_CARD FUNCTION----------------------------------
def pick_card(bet):
  if bet > money or bet <= 0:
    print("Not enough money, try again")
    
  else:
    card1 = random.randint(1,13)
    card2 = random.randint(1,13)
    if(card1 > card2):
      return bet
    elif(card1 == card2):
      return 0
    else:
      return bet * -1
  
#ROULETTE FUNCTION----------------------------------
def roulette(bet, call):
  if bet > money or bet <= 0:
    print("Not enough money, try again")
    
  else:
    opt1 = random.randint(0,1)
    opt2 = random.randint(0,10)
    odd_or_even = ""
    if opt1 == 0:
      odd_or_even = "Odd"
    else:
      odd_or_even = "Even"
  
    if (odd_or_even == call):
      return bet
    elif(opt2 == call):
      return bet * 2
    else:
      return bet * -1
  

#Call your game of chance functions here
#money += flip_coin(100,"Heads")
#print(money)

#money += roll_dice(50, "Even")
#print(money)
#money += pick_card(75)
#print(money)
#money += roulette(500, 1)
#print(money)
