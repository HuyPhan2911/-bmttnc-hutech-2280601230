from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while (True):
    print("\nSTUDENT MANAGEMENT PROGRAM")
    print("*******************************")
    print("** 1. Add students. **")
    print("** 2. Update student information by ID. **")
    print("** 3. Delete student ID. **")
    print("** 4. Search for students by name. **")
    print("** 5. Arrange students according to average score. **")
    print("** 6. Arrange students by major name. **")
    print("** 7. Display student list. **")
    print("** 0. Exit **")
    print("*******************************")

    key = int(input("Enter options: "))

    if (key == 1):
        print("\n1. Add students.")
        qlsv.nhapSinhVien()
        print("\nAdded students successfully!")

    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Update student information. ")
            print("\nEnter ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nStudent check in!")

    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Delete student.")
            print("\nEnter ID: ")
            ID = int(input())
            if (qlsv.deleteById(ID)):
                print("\nStudent with id = ", ID, " has been deleted.")
            else:
                print("\nThe student has id=", ID, " does not exist.")
        else:
            print("\nStudent check in!")

    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Search students by name.")
            print("\nEnter name to search: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nStudent check in!")

    elif(key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sort students by average score (GPA). ")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nStudent check in!")

    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sort students by name.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nStudent check in!")

    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Display the list of students.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nStudent check in!")

    elif (key == 0):
        print("\nYou have chosen to exit the program!")
        break

    else:
        print("\nNo luck!")
        print("\nPlease select the function in the menu box.")