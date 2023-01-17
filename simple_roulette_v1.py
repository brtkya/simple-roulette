#Simple Roulette by Berat / 2023

def colors():
    global color
    class color:
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
    color = color()
colors();

import random
result = random.randrange(0,37)

def roulette():
    global reds, blacks, greens
    reds = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    blacks = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    greens = [0,0]
roulette();

def welcome():
    print("*************************************")
    print("*                                   *")
    print("*",color.BOLD+color.CYAN,"Welcome to the Simple Roulette!",color.END+color.END,"*")
    print("*                                   *")
    print("*************************************")
    print()
welcome();

decision = int(input("""    
Enter 1 to bet on colors,
Enter 2 to bet on numbers,
Enter 3 to bet on even-odd,
Enter: """))
print()

if decision == 1:
    
    def colors_mech():
        print(color.BLUE+"***  Put your bets. Enter 0 if you want to skip a bet.  ***"+color.END)
        print()
        red_balance = int(input("Bet for reds: "))
        print()
        black_balance = int(input("Bet for blacks: "))
        print()
        if red_balance == 0 and black_balance == 0:
            print("There is no bet.")
            print()
        if red_balance != 0 and result in reds:
            print(color.GREEN+"Ball is on red. Earnings: ", (red_balance * 2),  color.END)
            print()
        elif red_balance != 0 and result not in reds:
            print(color.RED+"You lost bet on red, ball is not on red." , color.END)
            print()
        if black_balance != 0 and result in blacks:
            print(color.GREEN+"Ball is on black. Earnings: ", (black_balance * 2),  color.END)
            print()
        elif black_balance != 0 and result not in blacks:
            print(color.RED+"You lost bet on black, ball is not on black.",color.END)
            print()
    colors_mech();
    
elif decision == 2:
    
    def number_mech():
        numbers_choosen = []
        for number in range(37):
            print()
            number = int(input("Choose numbers between [0,36] to put bet: "))
            print()
            numbers_choosen.append(number)
            number_decision = int(input("Enter 1 to keep choosing, Enter 2 to stop: "))
            if number_decision == 1:
                continue
            else:
                break
        print()
        print("Numbers with bet on: ",numbers_choosen)
        print()
        number_balances = []
        for number in numbers_choosen:
            print("Number to bet on: ",number)
            number_balance = int(input("Put your bet on: "))
            print()
            number_balances.append(number_balance)
        print("Ball is on: ",result)
        for number in numbers_choosen:
            if number == result:
                print()
                print(color.GREEN+"You predicted the number correct. Earnings: ",number_balance*36,color.END)
            else:
                continue
        if result not in numbers_choosen:
            print(color.RED+"You have lost.",color.END)
    number_mech();

elif decision == 3:
    
    def even_odd_mech():
        print()
        print(color.BLUE+"***  Put your bets. Enter 0 if you want to skip a bet.  ***",color.END)
        print()
        even_balance = int(input("Bet for even numbers: "))
        print()
        odd_balance = int(input("Bet for odd numbers: "))
        print()
        print("Ball is on: ", result)
        if even_balance == 0 and odd_balance == 0:
            print()
            print("There is no bet.")
        if result % 2 == 0:
            if even_balance != 0:
                print()
                print(color.GREEN+"You won the even number bet. Earnings: ", even_balance * 2,color.END)
        elif result % 2 != 0:
            if odd_balance != 0:
                print()
                print(color.GREEN+"You won the odd number bet. Earnings: ", odd_balance * 2,color.END)       
    even_odd_mech();

 













