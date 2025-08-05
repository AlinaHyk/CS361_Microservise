# CS361_Microservice

How to REQUEST data
Create register_input.txt with this format:
action: register
username: kaitlyn
email: kaitlyn@example.com
password: pass123

Example code that you can refer to:

FOR ANY ACTIONS FIRST start the microservice first by running this in your terminal: python final_v.py

Here is the first time user registration example: 

with open("register_input.txt", "w") as f:
    f.write("action: register\n")
    f.write("username: user\n")
    f.write("email: userlastname@example.com\n")
    f.write("password: 2023\n")

In the above example what will happen is: The microservice will create a new user account with username "user", email "userlastname@example.com", and password "2023" (what has been provided in input file). 

The microservice will validate the information and either welcome the new user or return an error if the email/username already exists or if validation fails.

For login, change the action and leave username blank:
with open("register_input.txt", "w") as f:
    f.write("action: login\n")          
    f.write("username: \n")             
    f.write("email: userlastname@example.com\n")  
    f.write("password: 2023\n")     

In this second example we use the microservice to authenticate/check an existing user using their email "userlastname@example.com" and password "2023", so in this case microservice will check if the provided credentials match a registered user and either confirm successful login or return an error for invalid credentials.
\\\




How to RECEIVE data
Read from register_result.txt or alternative file with the same format of your liking.

The response that you will get is either:
success: true
message: success message related to the action requested 

OR

success: false
message: error message 

Here is an example of how you can use the implementation to see all of the messages for actions on which you ran the microservice: 

import os
import time

# Wait for the microservice to create the response file
while not os.path.exists("register_result.txt"):
    time.sleep(0.1)  # Check at the time intervals of your liking

# Read the entire response file
with open("register_result.txt", "r") as f:
    response = f.read()

# The responses will look like this:
# success: true
# message: "Welcome, user!"

print("Microservice response:")
print(response)

# You can then clean up by deleting the response file
os.remove("register_result.txt")

Brief Instructions of Usage:
============================
1. Start microservice: python final_v.py (keep this running)
2. In your program: Create register_input.txt
3. Microservice responds: Read register_result.txt
