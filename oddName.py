__author__ = 'Tom Stanley'
"""Tom Stanley"""
finished = False
user_name = str(input("Please enter your name:").strip(" "))
name_length = len(user_name)
while user_name == "":
        user_name = str(input("Your name cant be nothing.Please enter your name:").strip())
for i in range(1, name_length, 2):
    print(user_name[i])


