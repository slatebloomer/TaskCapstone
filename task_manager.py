#=====importing libraries===========
'''This is the section where you will import libraries'''
# I didn't find I needed any libraries for this task!

# Declaring the variables I'll need
username_list = ""
password_list = ""
username_position = ""
password_position = ""
unlock = False
admin_unlock = False
task_count = 0
user_count = 0

#====Login Section====

#This reads the user.txt doc and creates a list of the usernames and passwords
with open('user.txt', 'r') as userf:
    for line in userf:
        line = line.split()
        username_list += line[0]
        username_list = username_list.replace(",", " ")
        password_list += " " + line[1]
        password_list = password_list.strip()
username_list = username_list.split()
password_list = password_list.split()

#This section asks the user for their username and checks whether it's valid. If it is, it asks for password
while True:
    username = input("Please enter your username: ")
    if username in username_list:
        password = input("Please enter your password: ")

# Finding out what position the username and password hold and whether they match.
        for n in range(len(username_list)):
            if username == username_list[n]:
                username_position = n
        for n in range(len(password_list)):
            if password == password_list[n]:
                password_position = n
        if password_position == username_position:
            if username == "admin":
                admin_unlock = True
                break
            else:
                unlock = True
                break
        else:
            print("You have entered your password or username incorrectly. Please try again")
    else:
        print("You have entered an invalid username. Please try again")

# This section is for when the admin is logged in. The admin has different permissions so sees a different menu
while admin_unlock:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    menu = input('''\nSelect one of the following options:
    r -  Register a user
    a -  Add a task
    va - View all tasks
    vm - View my tasks
    s -  Display statistics
    e -  Exit
    : ''').lower()

    # Admin-only user input menu
    if menu == 'r':
        new_user = input("Please enter a username: ")
        #checking that the username isn't taken
        while new_user in username_list:
            new_user = input("That username is already in use. Please choose another one: ")
        else:
            new_pass = input("Please enter a password: ")
            check_pass = input("Re-enter the password: ")
            while new_pass != check_pass:
                new_pass = input("The passwords do not match. Please try again. \nPlease enter a password: ")
                check_pass = input("Re-enter the password: ")
            else:
                ofile = open("user.txt", "a")
                ofile.write(f"\n{new_user}, {new_pass}")
                ofile.close()
                # I added the below so that you can add several users in a row (ie without quitting and restarting the
                # program) and it will still recognise if a username is already in use. Otherwise it didn't recognise
                # it because it hadn't read from the user.txt file since the program was started. This is also
                # relevant later in the program
                username_list.append(new_user)
                print(f"Thank you! The user '{new_user}' has been registered.")

# Admin task input menu. It writes tasks entered by the user to tasks.txt
    elif menu == 'a':
        task_username = input("Enter the username of the person to whom the task is assigned: ")
        # this while loop checks whether the user has entered a valid username (there would be no point assigning a task
        # to a user who does not exist". The username_list.append(new_user) above is also important here
        while task_username not in username_list:
            task_username = input('''That username is not recognised. Try again!
Enter the username of the person to whom the task is assigned: ''')
        task_title = input("Enter the title of the task: ")
        task_description = input("And a description: ")
        task_due_date = input("When is the task due? Please use the format 10 Jan 2020: ")
        today_date = input("Enter today's date: ")
        ofile = open("tasks.txt", "a")
        ofile.write(f"\n{task_username}, {task_title}, {task_description}, {task_due_date}, {today_date}, No")
        ofile.close()
        print("Thank you; your task has been saved")

# Admin task view menu. It prints all the tasks to the console, formatted in a way that's easy to read
    elif menu == 'va':
        with open('tasks.txt', 'r') as f:
            for line in f:
                line = line.split(', ')
                print(f"Task:                   {line[1]}\n"
                      f"Assigned to:            {line[0]}\n"
                      f"Date assigned:          {line[3]}\n"
                      f"Due date:               {line[4]}\n"
                      f"Task complete?          {line[5].strip()}\n"
                      f"Task description:       {line[2]}\n")

# Admin user task view menu. It reads tasks.txt and presents the user's tasks formatted in a readable manner
    elif menu == 'vm':
        with open('tasks.txt', 'r') as f:
            for line in f:
                line = line.split(', ')
                if line[0] == username:
                    print(f"\nTask:                   {line[1]}\n"
                          f"Assigned to:            {line[0]}\n"
                          f"Date assigned:          {line[3]}\n"
                          f"Due date:               {line[4]}\n"
                          f"Task complete?          {line[5].strip()}\n"
                          f"Task description:       {line[2]}\n")

# Exit menu. I added the username into the message for a bit of personalisation
    elif menu == 'e':
        print(f'Goodbye, {username}! Have a nice day.')
        exit()

# Admin-only statistics menu. It just reads task.txt and user.txt and presents statistics about the number of
# tasks and users in a readable format
    elif menu == 's':
        with open('tasks.txt', 'r') as f:
            for line in f:
                task_count += 1
        with open('user.txt', 'r') as f:
            for line in f:
                user_count += 1
        print(f"Tasks: {task_count}\n"
              f"Users: {user_count}")

# Else statement to catch users who type the wrong letter
    else:
        print("You have made a wrong choice. Please try again")

# This section is for non-admin users
while unlock:
    #presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''\nSelect one of the following options:
a -  Add a task
va - View all tasks
vm - View my tasks
e -  Exit
: ''').lower()

# Task input menu. It writes tasks entered by the user to tasks.txt
    if menu == 'a':
        task_username = input("Enter the username of the person to whom the task is assigned: ")
# this while loop checks whether the user has entered a valid username (there would be no point assigning a task
# to a user who does not exist)
        while task_username not in username_list:
            task_username = input('''That username is not recognised. Try again!
Enter the username of the person to whom the task is assigned: ''')
        task_title = input("Enter the title of the task: ")
        task_description = input("And a description: ")
        task_due_date = input("When is the task due? Please use the format 10 Jan 2020: ")
        today_date = input("Enter today's date: ")
        ofile = open("tasks.txt", "a")
        ofile.write(f"\n{task_username}, {task_title}, {task_description}, {task_due_date}, {today_date}, No")
        ofile.close()
        print("Thank you; your task has been saved")

# Task view menu. It reads tasks.txt and presents the tasks formatted in a readable manner
    elif menu == 'va':
        with open('tasks.txt', 'r') as f:
            for line in f:
                line = line.split(', ')
                print(f"Task:                   {line[1]}\n"
                      f"Assigned to:            {line[0]}\n"
                      f"Date assigned:          {line[3]}\n"
                      f"Due date:               {line[4]}\n"
                      f"Task complete?          {line[5].strip()}\n"
                      f"Task description:       {line[2]}\n")

# Task view menu. It shows the user their own tasks
    elif menu == 'vm':
        with open('tasks.txt', 'r') as f:
            for line in f:
                line = line.split(', ')
                if line[0] == username:
                    print(f"\nTask:                   {line[1]}\n"
                          f"Assigned to:            {line[0]}\n"
                          f"Date assigned:          {line[3]}\n"
                          f"Due date:               {line[4]}\n"
                          f"Task complete?          {line[5].strip()}\n"
                          f"Task description:       {line[2]}\n")

# Exit menu. I added the username into the message for a bit of personalisation
    elif menu == 'e':
        print(f'Goodbye, {username}! Have a nice day.')
        exit()

# Else statement to catch users who type the wrong letter
    else:
        print("You have made a wrong choice. Please try again")