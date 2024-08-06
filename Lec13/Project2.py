import students_lib as st_lib

while True:
    print("\n1- Enter new student\n2- Print all students\n3- Search for a student\n4- Remove a student\n5- Update a student\n6- Sort\n7- Exit")
    opt = input("Enter your choice: ").lower()
    if opt == "7":
        break
    ###########################################################
    elif opt == "1":
        name = ""
        while(name != "done"):
            name = st_lib.Enter_Student()
            if name == "wrong" or name == "done":
                continue
            else:
                st_lib.Write_Student(name)
    ###########################################################
    elif opt == "2":
        students = st_lib.Read_Student()
        st_lib.Print_All(students)
    ###########################################################
    elif opt == "3":
        students = st_lib.Read_Student()
        ID = input("Enter ID number to search for student: ")
        name = st_lib.Search(ID, students)       #return actual name or return "not found"
        print("Name who you search for is:", name)
    ###########################################################
    elif opt == "4":
        students = st_lib.Read_Student()
        ID = input("\nEnter ID number to remove student: ")
        st_lib.Remove(ID, students)
    ###########################################################
    elif opt == "5":
        students = st_lib.Read_Student()
        ID = input("\nEnter ID number to update student: ")
        st_lib.Update(ID, students)
    ###########################################################
    elif opt == "6":
        st_lib.Sort(students)




# sherif said 5 3.4 1234
# ahmed hossam 2 3.1 54321
# wael mohamed 9 3.9 6789
# ahmed kamal 1 2.8 68758

