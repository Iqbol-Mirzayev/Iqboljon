with open("a1.txt") as file:
    read = file.readlines()
    login = read[0].strip()
    password = read[1].strip()
    newlog = input("welcome inter login :  ").lower().strip()
    newpass = input("welcome inter password :  ").lower().strip()
    