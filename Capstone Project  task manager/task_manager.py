def reg_user():# registers users

    if user == "admin":# makes sure only admin cand add users
        users_file = open("user.txt", "r+")#opens file
        ensure = False# if ensure turns true it will end the loop

        while ensure == False:# loop till ensure is true
            name_test = False# used to test if name has been used before
            # user inputs info is stored
            new_user = input("Enter new user: ")
            new_password = input("Enter password: ")
            test_new_password = input("Enter password again: ")

            # line in  file  breaks down into info to be used
            for line in users_file :
                admin, password, = line.split(", ")
                if new_user == admin:
                    name_test = True

            # if turned true prints out name has been add it before
            if name_test == True:
                print("user name has already been used try another.\n")
                users_file.seek(0)
            # else  if password match and user name is new it will ad user
            elif new_password == test_new_password:
                ensure = True
                print("Your user has been saved")
                # writes info into file
                users_file.write(f"\n{new_user}, {new_password}")
            # if passwords dont match it prints
            else:print("Passwords do not match please try again. \n")
            users_file.seek(0) # ensure loop strats at the start of the file

    # prints only admin can add user to non admin
    else:print("Only admin can register users.\n")
    users_file.close()#closes flie

def gen_reports():# creates a report
    task_file = open("tasks.txt", "r")#opens file

    # each variable is used as a counter
    num = 0
    comp_num = 0
    incomp_num = 0
    incomp_over_due = 0
    over_due = 0

    for line in task_file:
        from datetime import date, time, datetime# imports module

        tasks_assigned, tasks, details, start_date, due_date, complete, = line.split(", ")
        num += 1 # adds 1 to num

        # check if task is overdue
        stripped_comp = complete.strip()
        comp_low =  stripped_comp.lower()
        due_date.strip()
        dates = datetime.strptime(due_date,"%d %b %Y")
        today = datetime.today()

        if dates < today:
            over_due+= 1 # adds 1 to over_due
            if comp_low == "no":
                incomp_over_due+= 1 # adds 1 to incomp_over_due



        if comp_low == "no":
            incomp_num += 1 # adds 1 to incomp_num
        if comp_low == "yes":
            comp_num += 1 # adds 1 to comp_num
    # creates % info of tasks
    incomp = incomp_num / num *100
    over_due_perc = over_due / num * 100

    # creates and file and writes in all the info
    task_overview_file = open("task_overview.txt","w")
    task_overview_file.write(f"""The total number of tasks: {num}
The total number of completed tasks: {comp_num}
The total number of uncompleted tasks: {incomp_num}
The total number of tasks incompleted and overdue: {incomp_over_due}
The percentage of tasks that are incomplete: {incomp}%
The percentage of tasks that are overdue: {over_due_perc}%""")
    task_overview_file.close()# closes file

    users_file = open("user.txt", "r")# opens file
    user_num= 0# stores info

    for line in users_file:# counts amount of users
        admins, passwords, = line.split(", ")
        user_num += 1

    task_file.seek(0)# start to read file from start

    usertask_dict = {}#saves user details in a dictionary
    for line in task_file:
        tasks_assigned, tasks, details, start_date, due_date, complete, = line.strip().split(", ")

        if tasks_assigned in usertask_dict :
            usertask_dict[tasks_assigned] += 1
        else:
            usertask_dict[tasks_assigned] = 1


    task_file.seek(0)

    #stores diffrent info in dictonaries
    taskdone_dict = {}
    overdue_dict = {}
    task_notdone_dict = {}
    total_tasks =0# stores info


    for line in task_file:
        total_tasks += 1# counts amount of tasks
        tasks_assigned, tasks, details, start_date, due_date, complete = line.strip().split(", ")
        date_check = datetime.strptime(due_date,"%d %b %Y")

        # add user tasks that are completed and stores user task that are overdue
        if tasks_assigned in usertask_dict and complete.lower() == "no":
            if date_check < today:
                if tasks_assigned in overdue_dict:
                    overdue_dict[tasks_assigned] += 1
                else:
                    overdue_dict[tasks_assigned] = 1
        else:
            taskdone_dict[tasks_assigned] = 1

        # add user tasks that are not completed
        if  complete.lower() == "no":
            if tasks_assigned in task_notdone_dict:
                task_notdone_dict[tasks_assigned] += 1
            else:
                task_notdone_dict[tasks_assigned] = 1


    user_overview_file = open("user_overview.txt", "w")# creates file

# writes all info to file
    user_overview_file.write(f"""The total number of users : {user_num}
The total number of tasks: {num}""")

    for x, y in usertask_dict.items():
        pertask = y / total_tasks * 100# works out percentage
        user_overview_file.write(f"""
\nUser name: {x}
Total number of tasks assigned:{y}""")
        for a,b in  taskdone_dict. items():
            if a == x:
                per_done = b / y * 100
            for e, r in task_notdone_dict.items():
                if e == x:
                    per_notdone = r / y * 100
            for i, o in overdue_dict.items():
                if i == x:
                    per_ov = o / y * 100

            user_overview_file.write(f"""
Percentage of the total number of tasks:{pertask}%
Percentage of the total number of tasks completed{per_done}%
Percentage of the total number of tasks not completed {per_notdone}%
Percentage of the total number of tasks not completed and overdue{per_ov}""")
    user_overview_file.close()  # closes file
    print( "\nReport has been generated.")

def add_task():# adds task
    # opens file and appends to it
    task_file = open("tasks.txt", "a+")

    #user input stored
    admin = input("enter user a signed to task: ")
    tasks = input("enter task title: ")
    details = input("enter details about task: ")
    start_date = input("enter start date: ")
    due_date = input("enter due date: ")
    complete = input("is task complete: ")

    #write to file all user stored info
    task_file.write(f"\n{admin}, {tasks}, {details}, {start_date}, {due_date}, {complete}")
    task_file.close() # closes file

def  view_all():# views all info in tasks file

    task_file= open("tasks.txt","r")#opens file to read form it

    # prints out all info in a user friendly way
    for line in task_file:
        admin, tasks, details,  start_date,  due_date, complete, = line.split(", ")
        print(f"""
        name:{admin}
        task:{tasks}
        details:{details}
        date start:{start_date}
        date end:{due_date}
        complete?:{complete}""")
    task_file.close()  # closes file

def view_mine():
    # print out all user task  with a number
    task_file = open("tasks.txt", "r")
    for x, line in enumerate(task_file):
        print(x, line)

    # makes a list of file info to be edited
    task_file = open("tasks.txt", "r+")
    task_list = []
    for line in task_file:
        task_list.append(line)

    # user picks which  task user would like to edit
    task_choice = int(input("\nChoose which task you would like to edit or type -1 to return to menu.: "))

    if task_choice == -1:
        # starts by opening file to be read from
        users_file = open("user.txt", "r+")
        login = False  # used tocreate a loop

        while login == False:  # loop till login turns true
            # gets user input
            user = input("Enter user name here: ")
            password = input("Enter password here: ")

            # turns login true if password and user match
            for line in users_file:
                valid_user, valid_password = line.strip().split(", ")
                if user == valid_user and password == valid_password:
                    login = True

            # if false loop from the start
            if login == False:
                print("user name or password is incorrect please try again \n")
                users_file.seek(0)

        # option menu just for admin to pick from
        if user == "admin":
            choice = input("""\n
            please select one of the following options:
            r - register user
            a - add task
            va - view all tasks
            vm - view my tasks
            e - exit
            gr - generate reports
            dis - display statistics
            choose:""")

        # option menu for user to pick from
        else:
            choice = input("""\nplease select one of the following options:
        r - register user
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
        choose:""")

        # runs a defined function depending on the choice
        if choice == "r":
            reg_user()
        if choice == "a":
            add_task()
        if choice == "va":
            view_all()
        if choice == "vm":
            view_mine()
        if choice == "gr":
            gen_reports()

        # Displays number of users and number of tasks
        if choice == "dis":

            # reads files
            tasks_file = open("tasks.txt", "r")
            users_file = open("user.txt", "r")

            # stores total
            num_users = 0
            num_task = 0

            # counts users and tasks
            for line in tasks_file:
                num_task += 1
            for line in users_file:
                num_users += 1

            # prints info in a user friendly way
            print(f"""
            current number of users: {num_users}
            current number of tasks: {num_task}""")

            # closes files
            users_file.close()
            tasks_file.close()


# print options for user to edit
    else:print("""
    0: change assigned user
    1:  change tasks
    2:  change details
    3:  change start date
    4:  change due date
    5:  change complete
    """)

    task_edit = task_list[task_choice]
    linex= task_edit.split(", ")

    # user chosses what user would like to edit
    edit_choice = int(input("\nChoose what you would like to edit: "))

    # each option will print out what user will edit
    if edit_choice == 0 :
        linex[0] = input("edit user: ")
    if edit_choice == 1:
        linex[1] = input("edit task: ")
    if edit_choice == 2:
        linex[2] = input("edit task details: ")
    if edit_choice == 3:
        linex[3] = input("edit start date: ")
    if edit_choice == 4:
        linex[4] = input("edit due date: ")
    if edit_choice == 5:
        linex[5] = input("edit complete value: ")


  # joins all info into full data
    full_data = ""
    full_data += ", ".join(linex)
    task_list[task_choice] = full_data

   # clear old info
    task_file.seek(0)
    task_file.truncate(0)

   # write new info into the file
    task_file.seek(0)
    for line in task_list:
        str = ""
        line.join(str)
        str = "".join(line)
        print(str)
        task_file.write(str)


# starts by opening file to be read from
users_file = open("user.txt" ,"r+")
login = False# used tocreate a loop

while login == False:# loop till login turns true
    # gets user input
    user = input("Enter user name here: ")
    password = input("Enter password here: ")

    # turns login true if password and user match
    for line in users_file:
        valid_user, valid_password = line.strip().split(", ")
        if user == valid_user and password == valid_password:
            login = True

    # if false loop from the start
    if login == False:
      print("user name or password is incorrect please try again \n")
      users_file.seek(0)

# option menu just for admin to pick from
if user == "admin":
    choice = input("""\n
    please select one of the following options:
    r - register user
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    gr - generate reports
    dis - display statistics
    choose:""")

# option menu for user to pick from
else :
    choice = input("""\nplease select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my tasks
e - exit
choose:""")


# runs a defined function depending on the choice
if choice == "r":
    reg_user()
if choice == "a":
    add_task()
if choice == "va":
    view_all()
if choice == "vm":
    view_mine()
if choice == "gr": gen_reports()
# Displays number of users and number of tasks
if choice == "dis":
    # reads files
    tasks_file = open("task_overview.txt", "r")
    users_file = open("user_overview.txt", "r")

    # prints all info
    print(" ")
    print(tasks_file .read())
    print(" ")
    print(users_file.read())

    #closes files
    users_file.close()
    tasks_file.close()
