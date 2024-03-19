import re
print("Password complexity checker\n")
password=input("enter your password: ")
length=len(password)
score=0
# check for length of password
if length>=8:
    score+=1
    
# check for uppercase letters
if re.search(r'[A-Z]', password):
        score+=1

# Check for lowercase letters
if re.search(r'[a-z]', password):
    score+=1

# Check for numbers
if re.search(r'[0-9]', password):
    score+=1

# Check for special characters
if re.search(r'[^A-Za-z0-9]', password):
    score+=1

if score <= 2:
    print("Your password is: Weak")
elif score <= 4:
    print("Your password is: Moderate")
else:
    print("Your password is: Very Strong")




    
    
