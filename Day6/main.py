def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

user_name = input("Please enter your name: ")
print(greeting(user_name))