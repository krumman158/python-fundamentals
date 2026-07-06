#                                            Types of Functions

# 1) Action Functions -> Designed to perform an operation in the system instead of returning values.
# E:g store application log messages in a file

def write_log(message):
    with open(r"C:\Main\Python\app.log","a") as file:
        file.write(message + "\n")

write_log('App Started')

# 2) Transformation Functions -> Raw data goes in gets Transformed and returns processed data.

# E:g  clean eamil addressed and splits them into structured data.
def clean_and_split_email(email):
    cl_email=email.strip().lower()
    username,domain=cl_email.split("@")
    return {"username":username,"domain":domain}

emaill=clean_and_split_email('  mkzw2003@gmail.com  ')
print(emaill)

# 3) Validation Functions -> checks something is valid or not and return True/False
# E:g ->  check wether password meets the min requirement of 8 characters

def check(password):
    return len(password)>=8

print(check('123456'))
print(check('12345678'))

#E:g -> check if email has basic valid format

def check2(email):
    return '@' in email and '.' in email
    

print(check2('mkzw2003@gmail.com'))
print(check2('mkzw2003'))

# 4) orchestrator Functions ->  controls the program flow by calling other functions in the correct order.

# E:g -> receive email from user, validate the email, if unvalid log error in file, if valid then clean and structure email, log each step of program

def orchestartor_func():
    write_log('App started')
    email=input('Please enter your email: ')
    if not check2(email):
        write_log(f" Invalid email received")
    else:
        cl=clean_and_split_email(email)
        write_log(f'Processed Email: {cl}')
    write_log('App Stopped')
orchestartor_func()