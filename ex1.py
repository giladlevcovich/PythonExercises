secret_code='1234'
money='1000'

def check_secret_code(entered_secret_code):
    if entered_secret_code==secret_code:
        return True
    else:
        return False

def update_secret_code():
    new_secret_code= input("Enter new secret code")
    while not new_secret_code.isdigit():
        print("You didn't enter a number, enter again")
        new_secret_code=input()
    secret_code=new_secret_code