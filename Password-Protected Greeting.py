password = "DEV@2023"
attempts = 3
while attempts > 0:
    user_input = input("Enter the password: ")    
    if user_input == password:
        print("Hello")
        break
    else:
        attempts -= 1
if attempts == 0:
    secret_question = input("Enter the name of your favorite movie: ")
    if secret_question.lower() == "her":
        print("Hello")
    else:
        print("Access denied.")
