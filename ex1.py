secret_code='1234'
money='1000'

def check_secret_code(entered_secret_code):
    global secret_code
    if entered_secret_code==secret_code:
        return True
    else:
        return False

def update_secret_code():
    global secret_code
    new_secret_code= input("Enter new secret code: \n")
    while not new_secret_code.isdigit():
        print("You didn't enter a number, enter again: \n")
        new_secret_code=input()
    secret_code=new_secret_code


def money_withrawal():
    global money;
    print("How much you want to withdraw?\n"
          "enter 1 for 20\n"
          "enter 2 for 50\n"
          "enter 3 for other value\n")
    money_to_withdraw=input();
    while not money_to_withdraw.isdigit():
        print("You didn't enter a number, enter again")
        money_to_withdraw = input()
    while True:
        if money_to_withdraw=='1':
            money=int(money)-20
            break
        if money_to_withdraw=='2':
            money=int(money)-50
            break
        if money_to_withdraw=='3':
            down=input("How much money to down?")
            while not down.isdigit():
                print("You didn't enter a number, enter again")
                down=input()
            money=int(money) - int(down)
            break
while True:
    entered_code = input("Enter secret code:")
    if not check_secret_code(entered_code):
        print("Enter again, the code that was entered is not valid")
        continue

    print("Enter 1 for current money in account\n"
          "enter 2 for money withrawal\n"
          "enter 3 to change your secret code\n"
          "enter 4 to get out of the ATM\n")
    chose = input()
    if chose == '1':
        print(money)
        continue
    if chose == '2':
        money_withrawal()
        continue
    if chose == '3':
        update_secret_code()
        continue
    if chose == '4':
        break
print("Goodbye :)")
