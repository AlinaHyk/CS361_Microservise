import time
import os

def read_input():
    with open("register_input.txt", "r") as f:
        lines = f.readlines()
    
    data = {}
    # the following asumes that file is strucuted as:
    # action: register
    # username: kaitlyn
    # email: kaitlyn@example.com
    # password: 123
    # And it assumes that the user information has already been acquired, so if I misunderstood, please correct me.
    for line in lines:
        key, value = line.strip().split(":", 1) # Split at first ":" only
        data[key.strip()] = value.strip()
    return data

def write_result(success, message):
    with open("register_result.txt", "w") as f:
        f.write(f"success: {success}\n")
        f.write(f"message: \"{message}\"\n")

def validate_fields(username, email, password):
    if not username or not email or not password:
        return False, "All fields are required; Please fill them out."
    if "@" not in email:
        return False, "Invalid email format" # I am doing a very simple check here, but if desired, there can be a more sophisticated check loop for email entry.
    if len(password) < 6:
        return False, "Password must be at least 6 characters" #Again, if there are any other requirements, such as specific characters or use of numbers, it can be added here.

    return True, ""

def chek_if_user_exists(username, email): #checks if a user already exists in the system 
    try:
        with open("users.txt", "r") as f:
            content = f.read()
        return username in content or email in content
    except:
        return False

def save_user(username, email, password): #the format will be liek that: alice,alice@site.com,password123 (pelase let me knwo if you would like it to be differnt)
    with open("users.txt", "a") as f:
        f.write(f"{username},{email},{password}\n")

def process_registration(username, email, password):
    valid, error = validate_fields(username, email, password)
    if not valid:
        return False, error
    
    if chek_if_user_exists(username, email):
        return False, "Username or email already exists; please try again"
    
    save_user(username, email, password)
    return True, f"Welcome, {username}!"

def authenticate_user(email, password): #for login in with the existing account 
    try:
        with open("users.txt", "r") as f:
            for line in f:
                parts = line.strip().split(",") #again, this works with the formaitng of: alice,alice@site.com,password123, let me knwo if I need to change it. 
                if parts[1] == email and parts[2] == password:
                    return True, parts[0]
        return False, None
    except:
        return False, None

def process_login(email, password):
    if not email or not password:
        return False, "Email and password required"
    
    success, username = authenticate_user(email, password)
    if success:
        return True, f"Login successful, welcome back {username}!"
    else:
        return False, "Invalid email or password, please try again"

def run_microservice():
    print("User Registration Microservice started... :)")
    
    while True:
        if os.path.exists("register_input.txt"):
            data = read_input()
            
            action = data.get("action", "")
            username = data.get("username", "")
            email = data.get("email", "")
            password = data.get("password", "")
            
            if action == "register":
                success, message = process_registration(username, email, password)
                write_result(str(success).lower(), message)
            
            elif action == "login":
                success, message = process_login(email, password)
                write_result(str(success).lower(), message)
            
            os.remove("register_input.txt")
        
        time.sleep(1) #That's to establish a regular checking mechanism for new users that have been registered.

if __name__ == "__main__":
    run_microservice()
