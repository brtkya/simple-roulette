#Simple Roulette by Berat / 2023

import random
result = random.randrange(0,37)

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
Enter 4 to bet on groups of 12,
Enter 5 to bet on 1 to 18 and 19 to 36,
Enter 6 to bet on columns,
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
        print(color.PURPLE+color.BOLD+"***  Ball is on: ",result,(" ***"),color.END,color.END)
        print()
        if red_balance != 0 and result in reds:
            print(color.GREEN+"You won!",result,"is red. Earnings: ", (red_balance * 2),  color.END)
            print()
        elif red_balance != 0 and result not in reds:
            print(color.RED+"You lost bet on red, ball is not on red." , color.END)
            print()
        if black_balance != 0 and result in blacks:
            print(color.GREEN+"You won!",result,"is black. Earnings: ", (black_balance * 2),  color.END)
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
        print(color.PURPLE+color.BOLD+"***  Ball is on: ",result,(" ***"),color.END,color.END)
        print()
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
        print(color.PURPLE+color.BOLD+"***  Ball is on: ",result,(" ***"),color.END,color.END)
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

elif decision == 4:

    def twelve_mech():
        def twelve_lists():
            global first_twelve, second_twelve, third_twelve
            first_twelve = [1,2,3,4,5,6,7,8,9,10,11,12]
            second_twelve = [13,14,15,16,17,18,19,20,21,22,23,24]
            third_twelve = [25,26,27,28,29,30,31,32,33,34,35,36]
        twelve_lists();
        print(color.BLUE+"***  Put your bets. Enter 0 if you want to skip a bet.  ***"+color.END)
        print()
        first_twelve_balance = int(input("Bet for first twelve: "))
        print()
        second_twelve_balance = int(input("Bet for second twelve: "))
        print()
        third_twelve_balance = int(input("Bet for third twelve: "))
        print()
        if first_twelve_balance == 0 and second_twelve_balance == 0 and third_twelve_balance == 0:
            print("There is no bet.")
            print()
        print(color.PURPLE+color.BOLD+"***  Ball is on: ",result,(" ***"),color.END,color.END)
        print()
        if first_twelve_balance != 0 and result in first_twelve:
            print(color.GREEN+"You won!",result,"is in first twelve. Earnings: ", (first_twelve_balance * 2),  color.END)
            print()
        elif first_twelve_balance and result not in first_twelve:
            print(color.RED+"You lost bet on first twelve, ball is not in first twelve." , color.END)
            print()
        if second_twelve_balance != 0 and result in second_twelve:
            print(color.GREEN+"You won!",result,"is in second twelve. Earnings: ", (second_twelve_balance * 2),  color.END)
            print()
        elif second_twelve_balance and result not in second_twelve:
            print(color.RED+"You lost bet on second twelve, ball is not in second twelve." , color.END)
            print()
        if third_twelve_balance != 0 and result in third_twelve:
            print(color.GREEN+"You won!",result,"is in third twelve. Earnings: ", (third_twelve_balance * 2),  color.END)
            print()
        elif third_twelve_balance and result not in third_twelve:
            print(color.RED+"You lost bet on third twelve, ball is not in third twelve." , color.END)
            print()
    twelve_mech();

elif decision == 5:

    def interval_mech():
        def interval_lists():
            global first_interval, second_interval
            first_interval = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
            second_interval = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        interval_lists();
        print(color.BLUE+"***  Put your bets. Enter 0 if you want to skip a bet.  ***"+color.END)
        print()
        print(color.YELLOW+"First interval is 1 to 18, second interval is 19 to 36."+color.END)
        print()
        first_interval_balance = int(input("Bet for first interval: "))
        print()
        second_interval_balance= int(input("Bet for second interval: "))
        print()
        if first_interval_balance == 0 and second_interval_balance == 0:
            print("There is no bet.")
            print()
        print(color.PURPLE+color.BOLD+"***  Ball is on: ",result,(" ***"),color.END,color.END)
        print()
        if first_interval_balance != 0 and result in first_interval:
            print(color.GREEN+"You won!",result,"is in first interval. Earnings: ", (first_interval_balance * 2),  color.END)
            print()
        elif first_interval_balance and result not in first_interval:
            print(color.RED+"You lost bet on first interval, ball is in second interval." , color.END)
            print()
        if second_interval_balance != 0 and result in second_interval:
            print(color.GREEN+"You won!",result,"is in second interval. Earnings: ", (second_interval_balance * 2),  color.END)
        elif second_interval_balance and result not in second_interval:
            print(color.RED+"You lost bet on second interval, ball is in first interval." , color.END)
            print()
    interval_mech();

elif decision == 6:

    def column_mech():
        def column_lists():
            global first_column, second_column, third_column
            first_column = [1,4,7,10,13,16,19,22,25,28,31,34]
            second_column = [2,5,8,11,14,17,20,23,26,29,32,35]
            third_column = [3,6,9,12,15,18,21,24,27,30,33,36]
        column_lists();
        print(color.BLUE+"***  Put your bets. Enter 0 if you want to skip a bet.  ***"+color.END)
        print()
        first_column_balance = int(input("Bet for first column: "))
        print()
        second_column_balance = int(input("Bet for second column: "))
        print()
        third_column_balance = int(input("Bet for third column: "))
        print()
        if first_column_balance == 0 and second_column_balance == 0 and third_column_balance:
            print("There is no bet.")
            print()
        print(color.PURPLE+color.BOLD+"***  Ball is on: ",result,(" ***"),color.END,color.END)
        print()
        if first_column_balance != 0 and result in first_column:
            print(color.GREEN+"You won!",result,"is in first column. Earnings: ", (first_column_balance * 2),  color.END)
            print()
        elif first_column_balance and result not in first_column:
            print(color.RED+"You lost bet on first column, ball is not in first column." , color.END)
            print()
        if second_column_balance != 0 and result in second_column:
            print(color.GREEN+"You won!",result,"is in second column. Earnings: ", (second_column_balance * 2),  color.END)
            print()
        elif second_column_balance and result not in second_column:
            print(color.RED+"You lost bet on second column, ball is not in second column." , color.END)
            print()
        if third_column_balance != 0 and result in third_column:
            print(color.GREEN+"You won!",result,"is in third column. Earnings: ", (third_column_balance * 2),  color.END)
            print()
        elif third_column_balance and result not in third_column:
            print(color.RED+"You lost bet on third column, ball is not in third column." , color.END)
            print()
    column_mech();





 













