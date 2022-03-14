import os

with open("a1.txt") as file:
    read = file.readlines()
    login = read[0].strip()
    password = read[1].strip()
    newlog = input("Welcome, enter your login :  ").lower().strip()
    newpass = input("Enter your password :  ").lower().strip()


    while newlog != login or newpass != password:
        os.system("cls")
        print("Login or password is wrong. Try again")
        newlog = input("Enter your login :  ").lower().strip()
        newpass = input("Enter your password :  ").lower().strip()
        os.system("cls")
    os.system("cls")
    print("Welcome to your account!")

    new = input("Do you wish your update login or password [y/n]?").lower().strip()

    while new != "y" and "n":
        os.system("cls")
        print("wrong!")
        new = input("Do you wish your update login or password [y/n]?").lower().strip()

    os.system("cls")
    if new == 'y':
        newlogin = input("Enter your new login!: ").lower().strip()
        newll = input("Confirm your new login!: ").lower().strip()
        while newll != newlogin:
            os.system('cls')
            print("Logins are not the same!")
            newlogin = input("Enter your new login! ").lower().strip()
            newll = input("Confirm your new login!: ").lower().strip()
            os.system('cls')
        newpassword = input("Enter your new password: ")
        newp1 = input("Confirm your new password: ")
        os.system('cls')
        while newpassword != newp1:
            print("Your passwords aren't the same!")
            newpassword = input("Enter your new password: ")
            newp1 = input("Confirm your new password: ")
            os.system('cls')

        print("Login and password Changed succsesfully!")
    elif new == "n":
        os.system(exit())

