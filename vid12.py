#strings

username = input("enter your username")

if len(username) > 12:
    print("Username cannot be more than 12 characters long")
elif not username.find(" ") == -1:
    print("Username cannot have spaces")
elif not username.isalpha():
    print("Username cannot have digits")
else:
    print(f"Welcome {username}")