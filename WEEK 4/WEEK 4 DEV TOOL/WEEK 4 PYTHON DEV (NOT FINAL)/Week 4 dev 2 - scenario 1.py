#Prompt user to enter the role
role = input("Enter your role (admin, user, guest):  ").strip().lower()

#Determine access level from role input

if role == "admin":
    print("access Level: Full privileges granted.")
elif role =="user":
    print("Access Level: Limited privileges granted.")
elif role == "guest":
    print("Access Level: Read-only access granted.")
else:
    print("Invalid role entered. Please choose from admin, user, or guest.")