from QuanLySinhVien import StudentManager

stdmng = StudentManager()
while (1 == 1):
    print("\n CHUONG TRINH QUAN LY SINH VIEN \n")
    print("Menu: ")
    print("1. Them sinh vien")
    print("2. Cap nhat thong tin sinh vien bang ID")
    print("3. Xoa sinh vien bang ID")
    print("4. Tim kiem sinh vien bang ID")
    print("5. Sap xep sinh vien theo diem TB")
    print("6. Sap xep sinh vien theo ten")
    print("7. Hien thi danh sach sinh vien")
    print("8. Thoat chuong trinh")
    print("********************************************")
    choice = int(input("Nhap lua chon cua ban: "))
    if choice == 1:
        stdmng.addStudent()
        print("Them sinh vien thanh cong!")
    elif choice == 2:
        if stdmng.StudentNumber() > 0:
            ID = int(input("Nhap ID sinh vien can cap nhat: "))
            stdmng.updateStudent(ID)
            print("Cap nhat thong tin sinh vien thanh cong!")
        else:
            print("Danh sach sinh vien trong!")
    elif choice == 3:
        if stdmng.StudentNumber() > 0:
            ID = int(input("Nhap ID sinh vien can xoa: "))
            if stdmng.deleteByID(ID):
                print("Xoa sinh vien thanh cong!")
            else:
                print("Sinh vien co ID = {} khong ton tai".format(ID))
        else:
            print("Danh sach sinh vien trong!")
    elif choice == 4:
        if stdmng.StudentNumber() > 0:
            ID = int(input("Nhap ID sinh vien can tim: "))
            student = stdmng.findByID(ID)
            if student != None:
                stdmng.showStudentInfo(student)
            else:
                print("Sinh vien co ID = {} khong ton tai".format(ID))
        else:
            print("Danh sach sinh vien trong!")
    elif choice == 5:
        if stdmng.StudentNumber() > 0:
            stdmng.sortByAvgScore()
            print("Danh sach sinh vien sau khi sap xep theo diem TB:")
            stdmng.showAllStudent()
        else:
            print("Danh sach sinh vien trong!")
    elif choice == 6:
        if stdmng.StudentNumber() > 0:
            stdmng.sortByName()
            print("Danh sach sinh vien sau khi sap xep theo ten:")
            stdmng.showAllStudent()
        else:
            print("Danh sach sinh vien trong!")
    elif choice == 7:
        if stdmng.StudentNumber() > 0:
            stdmng.showAllStudent()
        else:
            print("Danh sach sinh vien trong!")
    elif choice == 8:
        print("Cam on ban da su dung chuong trinh!")
        break
    else:
        print("Lua chon khong hop le! Hay chon chuc nang trong menu!")