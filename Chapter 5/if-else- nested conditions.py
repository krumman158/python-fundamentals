password='@Rummankhan786'
email="mkzw2003@gmail.com"

password=password.strip()

if password == "":
    print("Invalid password")
elif len(str(password))  <=8:
    print("Invalid password")
elif not(any(p.islower() for p in password)):
    print("Invalid password")
elif not(any(p.isupper() for p in password)):
    print("Invalid password")
elif password==email:
    print("Invalid password")
elif " " in password:
    print("Invalid password")
elif not(password[0].isalnum() and password[-1].isalnum()):
    print("Invalid password")

# match case
command = "start"

match command:
    case "start":
        print("Program started")
    case "stop":
        print("Program stopped")
    case "restart":
        print("Program restarted")
    case _:
        print("Unknown command")

