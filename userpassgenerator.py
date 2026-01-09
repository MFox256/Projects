# Copeland’s Corporate Company has finalized what they want their username and temporary password creation to be and have enlisted your help to build the function to generate them.

def username_generator(first_name, last_name):
  user_name = first_name[:3] + last_name[:4]
  return user_name

user_name = username_generator("Abe", "Simpson")

def password_generator(user_name):
    password = ""
    for i in range(0, len(user_name)):
        password += user_name[i-1]
    return password

print(user_name)
print(password_generator(user_name))
