# Developer functions
# This is a helper function to check a string is a number or not
def is_number(string):
    try:
        float(string)  # Attempt to convert the string to a float
        return True
    except ValueError:
        return False

# This is a helper function to update the file
def update_file(students):
    Write_Student(students[0], opt="w")
    for i in range(1, len(students)):
        Write_Student(students[i], opt="a")

# User APIs
###########################################################
# This function will enter the data from user to RAM
def Enter_Student():
    name = input("\nEnter FN LN TERM GPA REG_NU (Enter done to return back): ").lower()#"wael mohamed"
    if(name == "done"):
        return "done"
    elif (len(name.split()) == 5) and (name.split()[0].isdigit() != 1) and (name.split()[1].isdigit() != 1)\
        and (name.split()[2].isdigit() == 1) and (is_number(name.split()[3]) == 1) and (name.split()[4].isdigit() == 1):
        return(name)
    else:
        print("You entered data in wrong format !\nPlease enter the data in 5 elements FN LN TERM GPA REG_NU.")
        return("wrong")

###########################################################
# This function to read the students from the file and return them in a list 
def Read_Student():
    hand = open("test.txt","r")
    stds = hand.read()                  # read all the file as one string
    stds = stds.strip().split("\n")     # make the students in a list of strings
    hand.close()
    return(stds)

###########################################################
def Write_Student(name="",opt="a",empty=0):     #name=""   opt="w"   empty=1 
    hand = open("test.txt", opt)                 #w :empty the file
    if empty == 0:#False
        hand.write(name + "\n")
    hand.close()

# This function is to all students in the file
def Print_All(students):
    for name in students:
        name = name.split()
        print("\nFirts Name:", name[0], "Last Name:", name[1], "TERM:" ,name[2], "GPA:", name[3], "ID_NUMBER:", name[4],end="\n")

###########################################################
# This function to search for a student in the file
def Search(ID, students):
    for name in students:
        if ID == name.split()[4]:
            return (name)
    else:
        return("not found")

###########################################################
# This function to remove a student from the file
def Remove(ID, students):
    name = Search(ID, students)
    students.remove(name)
    update_file(students)
    print(name, "is removed...")

###########################################################
# This function to update a student info in the file
def Update(ID, students):
    index = 0
    for name in students:
        if(ID == name.split()[4]):
            name = name.split()
            print("1- Update term\n2- Update GPA\n3- Update both")
            opt = input("Enter your choice: ")
            if(opt == "1"):
                term = input("Enter updated term: ")
                name[2] = term
            elif(opt == "2"):
                gpa = input("Enter updated gpa: ")
                name[3] = gpa
            elif(opt == "3"):
                term = input("Enter updated term: ")
                name[2] = term
                gpa = input("Enter updated gpa: ")
                name[3] = gpa
            else:
                print("Invalid option !")
            # Update the student in the list
            students[index] = " ".join(name);
            print(students[index], "is updated...");
            # Update the student in the file
            update_file(students)
            break
        else:
            index += 1
    else:
        print("Student with ID_NU =", ID, "is not found !")

###########################################################
# This function to sort the students ascendingly or descendingly in the file
def Sort(students):
    print("\n1- Ascendingly\n2- Descendingly")
    opt = input("Enter your choice: ")
    if(opt == "1"):
        students = sorted(students)
        update_file(students)
        print("Students are sorted from a to z")
    elif(opt == "2"):
        students = sorted(students, reverse=True)
        update_file(students)
        print("Students are sorted from z to a")
    else:
        print("Invalid option !")
        
        

