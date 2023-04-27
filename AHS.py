class Patient:
    def __init__(self,pid, name, disease, gender, age ):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age
        

    #getters
    def get_pid(self):
        return self.pid
    
    def get_name(self):
        return self.name
    
    def get_disease(self):
        return self.disease
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age
    
    #setters
    def set_pid(self,new_pid):
        self.pid = new_pid
    
    def set_name(self,new_name):
        self.name = new_name
    
    def set_disease(self,new_disease):
        self.disease = new_disease

    def set_gender(self,new_gender):
        self.gender = new_gender
    
    def set_age(self,new_age):
        self.age = new_age

    #__str__()
    def __str__(self):
       return f'{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}' 
    

 
class PatientManager:
    #constructor
    def __init__(self):
        self.patients = []
        self.__read_patients_file() 

    #format_patient_Info_for_file
    def format_patient_Info_for_file(self,patient):
        return f"{patient.get_pid()}_{patient.get_name()}_{patient.get_disease()}_{patient.get_gender()}_{patient.get_age()}"
    
    #enter patient info
    def enter_patient_info(self):
        pid = input('Enter patient pid: ')
        name = input('Enter patient name: ')
        disease = input('Enter patient disease: ')
        gender = input('Enter patient gender: ')
        age = input('Enter patient age: ')
        patient  = Patient(pid,name,disease,gender,age)
        self.patients.append(patient)
    
    #read_patients_file
    def __read_patients_file(self):
        f = open('patients.txt','r')
        file_content = f.readlines()
        f.close()
        for line in file_content:
            patient_fields = line.strip('\n').split('_')
            patient = Patient(patient_fields[0],patient_fields[1],patient_fields[2],patient_fields[3],patient_fields[4])
            self.patients.append(patient) 
                
    


    # search patient info
    def search_patient_by_id(self):
        found = False
        id = input('Enter patient id: ')
        print("{:<10}{:<20}{:<10}{:<10}{:<10}".format('ID','Name','Disease','Gender', 'Age'))
        print()
        for patient in self.patients:
            if patient.get_pid() == id:
                found = True
                print("{:<10}{:<20}{:<10}{:<10}{:<10}".format(patient.get_pid(),patient.get_name(),patient.get_disease(),patient.get_gender(),patient.get_age()))
                print()
                break
        if not found:
            print('patient', id, 'isn\'t in the system')
    

    #edit patient info
    def edit_patient_info_by_id(self):
        found = False
        patient_id = input('Enter the id of the patient you wish to change: ')
        for patient in self.patients:
            if patient.get_pid() == patient_id:
                found = True
                break
        if found:
                new_name = input('Enter new name: ')
                new_disease = input('Enter new disease: ')
                new_gender = input('Enter new gender: ')
                new_age = input('Enter new age: ')

                patient.name = new_name
                patient.disease = new_disease
                patient.gender = new_gender
                patient.age = new_age
                print("Patient updated!")
                print(patient)
        else:
            print('Patient was not found')

    #display patient info       
       
    def display_patient_list(self):
        print("{:<10}{:<20}{:<10}{:<10}{:<10}".format('','','','', ''))
        for patient in self.patients:
            print("{:<10}{:<20}{:<10}{:<10}{:<10}".format(patient.get_pid(),patient.get_name(),patient.get_disease(),patient.get_gender(),patient.get_age()))
            print()
    
     #add_patient_to_file
    def add_patient_to_file(self):
       patient = self.enter_patient_info()
       self.patients.append(patient)
       self.write_list_of_patients_to_file()

    
    #write_list_of_patients_to_file
    def write_list_of_patients_to_file(self):
        file = open('patients.txt', 'w')
        for patient in self.patients:
            file.write(patient.__str__() + '\n')
        file.close()
    
    def enter_patient_info(self):
        print('Enter ID: ')
        id = input()
        print('Enter name: ')
        name = input()
        print('Enter disease: ')
        disease = input()
        print('Enter gender: ')
        gender = input()
        print('Enter age: ')
        age = input()
        patient = Patient(id,name, disease,gender,age)
        return patient
        


    
  


