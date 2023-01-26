import random
result = random.randrange(0,37)

colors = {'PURPLE' : '\033[95m',
    'CYAN' : '\033[96m',
    'DARKCYAN' : '\033[36m',
    'BLUE' : '\033[94m',
    'GREEN' : '\033[92m',
    'YELLOW' : '\033[93m',
    'RED' : '\033[91m',
    'BOLD' : '\033[1m',
    'UNDERLINE' : '\033[4m',
    'END' : '\033[0m'}
    
print("*************************************")
print("*                                   *")
print("*",colors['BOLD']+colors['CYAN'],"Welcome to the Simple Roulette!",colors['END']+colors['END'],"*")
print("*                                   *")
print("*************************************")
print()

bets = []

def get_color():
    global reds, blacks, greens, color, color_amount
    reds = [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]
    blacks = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
    greens = [0,0]
    color = int(input("Choose color: [1] for Red, [2] for Black: "))
    print()
    while(color > 2 or color < 1):
        color = int(input("Invalid choice. Try again: "))
        print()
    color_amount = int(input("How much do you want to bet: "))
    print()
    bets.append(['Color',color, color_amount])

def get_number():
    global number, number_amount
    number = int(input("Enter the number you want to put bet: "))
    print()
    while(number < 0 or number > 36):
        number = int(input("Invalid choice. Try again (Choose between 0,36): "))
        print()
    number_amount = int(input("How much do you want to bet: "))
    print()
    bets.append(['Number', number, number_amount])

def get_even_odd():
    global oddity, oddity_amount
    oddity = int(input("Enter [1] for Even, enter [2] for Odd: "))
    print()
    while(oddity < 1 or oddity > 2):
        oddity = int(input("Invalid choice. Try again: "))
        print()
    oddity_amount = int(input("How much do you want to bet: "))
    print()
    bets.append(['EvenOdd', oddity, oddity_amount])

def get_group():
    global first_twelve, second_twelve, third_twelve, group, group_amount
    first_twelve = [1,2,3,4,5,6,7,8,9,10,11,12]
    second_twelve = [13,14,15,16,17,18,19,20,21,22,23,24]
    third_twelve = [25,26,27,28,29,30,31,32,33,34,35,36]
    group = int(input("Enter the group index of 12's you want to bet: "))
    print()
    while(group < 1 or group > 3):
        group = int(input("Invalid choice. Try again, (There is 3 groups of 12.): "))
        print()
    group_amount = int(input("How much do you want to bet: ")),
    print()
    bets.append(['Group', group, group_amount])

def get_half():
    global first_half, second_half, half, half_amount
    first_half = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    second_half = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    half = int(input("Choose the half you want to play: [1] for 1 to 18, [2] for 19 to 36: "))
    print()
    while(half < 1 or half > 2):
        half = int(input("Invalid choice. Try again, (There is 2 halfs.) : "))
        print()
    half_amount = int(input("How much do you want to bet: "))
    print()
    bets.append(['Half', half, half_amount])

def get_column():
    global first_column, second_column, third_column, column, column_amount
    first_column = [1,4,7,10,13,16,19,22,25,28,31,34]
    second_column = [2,5,8,11,14,17,20,23,26,29,32,35]
    third_column = [3,6,9,12,15,18,21,24,27,30,33,36]
    column = int(input("Enter the index of the column you want to bet: "))
    print()
    while(column < 1 or column > 3):
        column = int(input("Invalid choice. Try again, (There is 3 columns.): "))
        print()
    column_amount = int(input("How much do you want to bet: "))
    print()
    bets.append(['Column', column, column_amount])

def check_color(color, color_amount):
    if color == 1 and result in reds:
        return color_amount * 2 
    elif color == 2 and result in blacks:
        return color_amount * 2
    return 0

def check_number(number, number_amount):
    if result == number:
        return number_amount * 36
    return 0

def check_oddity(oddity, oddity_amount):
    if result % 2 == 0 and oddity == 1:
        return oddity_amount * 2
    elif result % 2 != 0 and oddity == 2:
        return oddity_amount * 2
    return 0

def check_group(group, group_amount):
    if group == 1 and result in first_twelve:
        return group_amount * 2
    elif group == 2 and result in second_twelve:
        return group_amount * 2
    elif group == 3 and result in third_twelve:
        return group_amount * 2
    return 0

def check_half(half, half_amount):
    if half == 1 and result in first_half:
        return half_amount * 2
    elif half == 2 and result in second_half:
        return half_amount * 2
    return 0

def check_column(column, column_amount):
    if column == 1 and result in first_column:
        return column_amount * 2
    elif column == 2 and result in second_column:
        return column_amount * 2
    elif column == 3 and result in third_column:
        return column_amount * 2
    return 0

def get_result():
    total_money = 0
    for bet in bets:
        match bet[0]:
            case 'Color':
                total_money += check_color(bet[1], bet[2])
            case 'Number':
                total_money += check_number(bet[1], bet[2])
            case 'EvenOdd':
                total_money += check_oddity(bet[1], bet[2])
            case 'Group': 
                total_money += check_group(bet[1], bet[2])
            case 'Half':
                total_money += check_half(bet[1], bet[2])
            case 'Column':
                total_money += check_column(bet[1], bet[2])
    
    print(colors['DARKCYAN']+"Ball is on: ",result,colors['END'])
    print()
    print(colors['RED']+"CHECK A ROULETTE TABLE IMAGE TO UNDERSTAND THE RESULT!!!",colors['END'])
    print()
    if total_money > 0:
        print(colors['GREEN']+"Total earnings: ", total_money, "USD.",colors['END'])
    elif total_money == 0:
        print(colors['RED']+"All bets are lost.",colors['END'])

while True: 
    decision = int(input("""    
Enter 1 to bet on colors,
Enter 2 to bet on numbers,
Enter 3 to bet on even-odd,
Enter 4 to bet on groups of 12,
Enter 5 to bet on 1 to 18 and 19 to 36,
Enter 6 to bet on columns,
Enter 0 to continue (Bets will close),

Enter: """))
    print()
    match decision:
        case 0:
            get_result()
            break
        case 1:
            get_color()
        case 2:
            get_number()
        case 3:
            get_even_odd()
        case 4:
            get_group()
        case 5:
            get_half()
        case 6:
            get_column()

