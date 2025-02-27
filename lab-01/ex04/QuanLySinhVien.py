from sinhvien import Student

class StudentManager:
    listStudent = []
    def generateID(self):
        maxID = 1
        if (self.StudentNumber() > 0):
            maxID = self.listStudent[0]._id 
            for student in self.listStudent:
                if student._id > maxID:
                    maxID = student._id
            maxID += 1
        return maxID
    def StudentNumber(self):
        return self.listStudent.__len__()
    def addStudent(self):
        studentID = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh: ")
        major = input("Nhap nganh hoc: ")
        avgScore = float(input("Nhap diem trung binh: "))
        student = Student(studentID, name, sex, major, avgScore)
        self.listStudent.append(student)
    
    def updateStudent(self, ID):
        stdnt:Student = self.findByID(ID)
        if stdnt != None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh: ")
            major = input("Nhap nganh hoc: ")
            avgScore = float(input("Nhap diem trung binh: "))
            stdnt._name = name
            stdnt.sex = sex
            stdnt.major = major
            stdnt.avgScore = avgScore
            self.RankingEducation(stdnt)
        else:
            print("Sinh vien co ID = {} khong ton tai".format(ID))
            
    def sortByID(self):
        self.listStudent.sort(key=lambda x: x._id, reverse=False)
        
    def sortByName(self):
        self.listStudent.sort(key=lambda x: x._name, reverse=False)
        
    def sortByAvgScore(self):
        self.listStudent.sort(key=lambda x: x._avgScore, reverse=False)
        
    def findByID(self, ID):
        serchResult = None
        if self.StudentNumber() > 0:
            for student in self.listStudent:
                if student._id == ID:
                    serchResult = student
                    break
        return serchResult
    
    def deleteByID(self, ID):
        isDeleted = False
        stdnt = self.findByID(ID)
        if stdnt != None:
            self.listStudent.remove(stdnt)
            isDeleted = True
        return isDeleted
    
    def RankingEducation(self, student:Student):
        if student.avgScore >= 8:
            student.__academicPerformance = "Gioi"
        elif student.avgScore >= 6.5:
            student._academicPerformance = "Kha"
        elif student.avgScore >= 5:
            student._academicPerformance = "Trung Binh"
        else:
            student._academicPerformance = "Yeu"
    def showAllStudent(self):
        print("{:<5} {:<20} {:<10} {:<20} {:<10} {:<10}".format("ID", "Ten", "Gioi Tinh", "Nganh Hoc", "Diem TB", "Hoc Luc"))
        for student in self.listStudent:
            print("{:<5} {:<20} {:<10} {:<20} {:<10} {:<10}".format(student._id, student._name, student._sex, student._major, student._avgScore, student._academicPerformance))    
    def getListStudent(self):
        return self.listStudent