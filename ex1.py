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
    new_secret_code= input("Enter new secret code")
    while not new_secret_code.isdigit():
        print("You didn't enter a number, enter again")
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
        money_to_withdraw = input();
    while True:
        if money_to_withdraw=='1':
            money=money-20
            break
        if money_to_withdraw=='2':
            money=money-50
            break
        if money_to_withdraw=='3':
            down=input("How much money to down?")
            while not down.isdigit():
                print("You didn't enter a number, enter again")
                down=input()
            money=money-down
            break



