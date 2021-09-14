def check(password):
    with open('passwords.txt', 'r') as file:
        password_list = [line.strip() for line in file]

    for item in password_list:
        if item == password:
            return True
            break
        else:
            return False
