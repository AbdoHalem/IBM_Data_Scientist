# This is a helper function to check a string is a number or not
def is_number(string):
    try:
        float(string)  # Attempt to convert the string to a float
        return True
    except ValueError:
        return False

# List to save the students data
students = []
while True:
    print("\n1- Enter new student\n2- Print all students\n3- Search\n4- Remove\n5- Update\n6- Sort\n7- Exit")
    opt = input("Enter your choice: ")
    if opt == "7":
        break
    ##########################################################
    elif opt == "1":
        name = ""
        while (True):
            name = input("\nEnter FN LN TERM GPA REG_NU (Enter done to return back): ").lower()#"wael mohamed"
            if(name == "done"):
                break
            if (len(name.split()) == 5) and (name.split()[0].isdigit() != 1) and (name.split()[1].isdigit() != 1)\
                and (name.split()[2].isdigit() == 1) and (is_number(name.split()[3]) == 1) and (name.split()[4].isdigit() == 1):
                students.append(name)
            else:
                print("You entered data in wrong format !\nPlease enter the data in 5 elements FN LN TERM GPA REG_NU.")
    ##########################################################
    elif opt == "2":
        for name in students:   #students=["sherif said 5 3.4 1234","ahmed hossam 2 3.1 54321"]
            name = name.split() #name=["sherif","said","5","3.4","1234"]
            print("\nFirst name:", name[0], "Last name:", name[1], "Term:", name[2],"GPA:", name[3], "REG_NU:", name[4])
    ##########################################################
    elif opt == "3":
        ID = input("\nEnter REG_NU to search for: ")
        for name in students:
            if(ID == name.split()[4]):
                print(name); break
        else:
            print("Student with REG_NU =", ID, "is not found !")
    ##########################################################
    elif opt == "4":
        ID = input("\nEnter REG_NU to remove: ")
        for name in students:
            if(ID == name.split()[4]):
                print(name, "is removed...")
                students.remove(name); break
        else:
            print("Student with REG_NU =", ID, "is not found !")
    ##########################################################
    elif opt == "5":
        ID = input("\nEnter REG_NU to update: ")
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
                students[index] = " ".join(name);
                print(students[index], "is updated..."); break
            else:
                index += 1
        else:
            print("Student with REG_NU =", ID, "is not found !")
    ##########################################################
    elif(opt == "6"):   # Sort the list without print it as it may be too large
        print("1- Ascendingly\n2- Descendingly")
        opt = input("Enter your choice: ")
        if(opt == "1"):
            students = sorted(students)
        elif(opt == "2"):
            students = sorted(students, reverse=True)
        else:
            print("Invalid option !")
    ##########################################################
    else:
        print("Invalid option ! Please enter number from 1 to 7")