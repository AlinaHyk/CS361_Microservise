import time
import os

def testing(action, username="", email="", password=""):
    # Creating a test input doc
    with open("register_input.txt", "w") as f:
        f.write(f"action: {action}\n")
        f.write(f"username: {username}\n")
        f.write(f"email: {email}\n")
        f.write(f"password: {password}\n")
    
    while not os.path.exists("register_result.txt"):
        time.sleep(0.1)
    
    with open("register_result.txt", "r") as f:
        result = f.read()
    
    os.remove("register_result.txt")
    print(result)

# tests
print("Registering a new user:")
testing("register", "kaitlynCARLOS", "kaitlyn@email.com", "YespassKKK123")

print("Trying to register a duplicate user:")
testing("register", "kaitlynCARLOS", "kaitlyn@email.com", "YespassKKK123")

print("Registering with email that does not pass the varification:")
testing("register", "john", "hereisanemailhopeyouenjoyit", "pass123")

print("Login:")
testing("login", "", "kaitlyn@email.com", "YespassKKK123")

print("Login with wrong password:")
testing("login", "", "kaitlyn@email.com", "Imnothim")
