class Doctor:
    def __init__(self, DocID, Name, Spec, WorkTime, Qual, RoomNum):
        self.DocID = DocID
        self.Name = Name
        self.Spec = Spec
        self.WorkTime = WorkTime
        self.Qual = Qual
        self.RoomNum = RoomNum
    
    #Getters
    def getDocID(self):
        return self.DocID
    def getName(self):
        return self.Name
    def getSpec(self):
        return self.Spec
    def getWorkTime(self):
        return self.WorkTime
    def getQual(self):
        return self.Qual
    def getRoomNum(self):
        return self.RoomNum
    
    #Setters
    def setDocID(self, newDocID):
        self.DocID = newDocID
    def setName(self, newName):
        self.Name = newName
    def setSpec(self, newSpec):
        self.Spec = newSpec
    def setWorkTime(self, newWorkTime):
        self.WorkTime = newWorkTime
    def setQual(self, newQual):
        self.Qual = newQual
    def setRoomNum(self, newRoomNum):
        self.RoomNum = newRoomNum
    
    def __str__(self) -> str:
        return f'{self.DocID}_{self.Name}_{self.Spec}_{self.WorkTime}_{self.Qual}_{self.RoomNum}'
    
class DoctorManager:
    def __init__(self):
        self.DocList = []
        self.read_doctors_file()
    
    def format_dr_info(self, Doctor):
        return f'{Doctor.getDocID()}_{Doctor.getName()}_{Doctor.getSpec()}_{Doctor.getWorkTime()}_{Doctor.getQual()}_{Doctor.getRoomNum()}'
    
    def enter_dr_info(self):
        DocID = input("Enter the doctor's ID: \n")
        Name = input("Enter the doctor's Name: \n")
        Spec = input("Enter the doctor's specialty: \n")
        WorkTime = input("Enter the doctor's timing (e.g., 7am-10pm): \n")
        Qual = input("Enter the doctor's qualification: \n")
        RoomNum = input("Enter the doctor's room number: \n")

        print(f'Doctor whose ID is {DocID} had been added\n')

        doctor = Doctor(DocID, Name, Spec, WorkTime, Qual, RoomNum)
        return doctor
    
    def read_doctors_file(self):
        x = open("doctors.txt", "r")
        doctorsTXT = x.readlines()
        for line in doctorsTXT:
            lineList = line.split("_")
            doctor = Doctor(lineList[0],lineList[1],lineList[2],lineList[3],lineList[4],lineList[5])
            self.DocList.append(doctor)
        x.close()

    def search_doctor_by_id(self):
        DoctorID = input("Enter the doctor Id: \n")
        found = False
        for i in self.DocList:
            if i.getDocID() == DoctorID:
                print(f'Id   Name                   Speciality      Timing          Qualification   Room Number')
                print(f'{i.DocID:<6}{i.Name:23}{i.Spec:<16}{i.WorkTime:<18}{i.Qual:<16}{i.RoomNum}') # Do a formatting here
                found = True
                break
        if not found:
            print("Can't find the doctor with the same ID on the system\n")
    
    def search_doctor_by_name(self):
        DocName = input("Enter the doctor name: \n")
        found = False
        for i in self.DocList:
            if i.getName() == DocName:
                print(f'Id   Name                   Speciality      Timing          Qualification   Room Number')
                print(f'{i.DocID:<6}{i.Name:23}{i.Spec:<16}{i.WorkTime:<18}{i.Qual:<16}{i.RoomNum}')
                found = True
                break
        if not found:
                print("Can't find the doctor with the same name on the system\n")
    
    def display_doctor_info(self):
        for i in self.DocList:
            print(self.format_dr_info(self.DocList[i]))
    
    def edit_doctor_info(self):
        DoctorID = input("Please enter the id of the doctor that you want to edit their information: \n")
        found = False
        for i in self.DocList:
            if i.getDocID() == DoctorID:
                found = True
                i.Name = input("Enter new Name: \n")
                i.Spec = input("Enter new Specilist in: \n")
                i.WorkTime = input("Enter new Timing: \n")
                i.Qual = input("Enter new Qualification: \n")
                i.RoomNum = input("Enter new Room Number: \n")

                #a = open("doctors.txt", "w")
                #a.write(self.DocList)
                #a.close()

                print(f'Doctor whose ID is {DoctorID} has been edited')
                break
        if not found:
            print("Can't find doctor with the same ID on the system")

    def display_doctors_list(self):
        for i in self.DocList:
            print(f'{i.DocID:<6}{i.Name:<23}{i.Spec:<16}{i.WorkTime:<18}{i.Qual:<16}{i.RoomNum}')
    
    def write_list_of_doctors_to_file(self):
        x = open("doctors.txt", "w")
        newDocList = []
        for i in self.DocList:
            currentDoc = self.DocList[i]
            currentDoc.format_dr_info()
            newDocList.append(currentDoc)
        x.write(newDocList)
        x.close()

    def add_dr_to_file(self):
        x = self.enter_dr_info()
        self.DocList.append(x)
        x = self.format_dr_info(x)
        a = open("doctors.txt", "a")
        a.write(x)
        a.close()
        print("New Doctor has Been added")