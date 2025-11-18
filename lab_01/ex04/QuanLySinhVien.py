from SinhVien import SinhVien

class QuanLySinhVien:
    listStudents = []

    def generateID(self):
        maxId = 1
        if (self.soLuongSinhVien() > 0):
            maxId = self.listStudents[0]._id
            for sv in self.listStudents:
                if (maxId < sv._id):
                    maxId = sv._id
            maxId = maxId + 1
        return maxId

    def soLuongSinhVien(self):
        return len(self.listStudents)

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Enter student name: ")
        sex = input("Enter student gender: ")
        major = input("Enter student's major: ")
        diemTB = float(input("Enter student score: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.listStudents.append(sv)

    def updateSinhVien(self, ID):
        sv: SinhVien = self.findByID(ID)
        if (sv != None):
            name = input("Enter student name: ")
            sex = input("Enter student gender: ")
            major = input("Enter student's major: ")
            diemTB = float(input("Enter student score: "))
            
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            
            self.xepLoaiHocLuc(sv)
        else:
            print("Student with ID {} does not exist.".format(ID))

    def sortByID(self):
        self.listStudents.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listStudents.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listStudents.sort(key=lambda x: x._diemTB, reverse=False)

    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listStudents:
                if (sv._id == ID):
                    searchResult = sv
                    break
        return searchResult

    def findByName(self, keyword):
        listSV = []
        if (self.soLuongSinhVien() > 0):
            for sv in self.listStudents:
                if (keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listStudents.remove(sv)
            isDeleted = True
        return isDeleted

    def xepLoaiHocLuc(self, sv: SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Average"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))

        if (len(listSV) > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
            print("\n")

    def getListSinhVien(self):
        return self.listStudents