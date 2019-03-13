secret_code='1234'
money='1000'

def check_secret_code(entered_secret_code):
    if entered_secret_code==secret_code:
        return True
    else:
        return False