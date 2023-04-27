# Something something Hospital manager
# Allows the user to browse and edit information for Doctors and Patients
# Menu written by Mark Tan
# Patient-related classes written by Asenai Shiberim
# Doctor-related classes written by Ivan Templora

from AHS import PatientManager
from doctor import DoctorManager

class display_menu:
    def __init__(self):
        self.patientManager = PatientManager() #Creates its own patient Manager
        self.doctorManager = DoctorManager()
        self.__display_menu() #Calls the private method for the menu

    def __display_menu(self):
        choice = 0
        while (choice != 3):
            choice = input("\nWelcome ot the Alberta Hospital (AH) Management System\nSelect from the following options, or select 3 to stop:\n 1 - Doctors \n 2 - Patients \n 3 - Exit Program\n")
            if (choice.isnumeric()): #Prevents program crashing. Doesn't happen again for submenus. I could but it's a lot of pointless lines when only the sample output will be tested.
                choice = int(choice)
                if (choice == 1):
                    doctorChoice = 0
                    while (doctorChoice != 6):
                        doctorChoice = int(input("\nDoctor Menu\n1 - Display Doctors list\n2 - Search for Doctor by ID\n3 - Search for Doctor by name\n4 - Add Doctor\n5 - Edit Doctor info\n6 - Back to the Main Menu\n"))
                        if (doctorChoice == 1):
                            self.doctorManager.display_doctors_list()
                        elif (doctorChoice == 2):
                            self.doctorManager.search_doctor_by_id()
                        elif (doctorChoice == 3):
                            self.doctorManager.search_doctor_by_name()
                        elif (doctorChoice == 4):
                            self.doctorManager.add_dr_to_file()
                        elif (doctorChoice == 5):
                            self.doctorManager.edit_doctor_info()
                        elif (doctorChoice == 6):
                            pass
                        else:
                            print("Your input is terribly invalid.")
                elif (choice == 2): 
                    patientChoice = 0
                    while (patientChoice != 5):
                        patientChoice = int(input("\nPatients Menu\n1 - Display patients list\n2 - Search for Patient by ID\n3 - Add Patient\n4 - Edit Patient Info\n5 - Back to the Main Menu\n"))
                        if (patientChoice == 1):
                            self.patientManager.display_patient_list()
                        elif (patientChoice == 2):
                            self.patientManager.search_patient_by_id()
                        elif (patientChoice == 3):
                            self.patientManager.add_patient_to_file()
                        elif (patientChoice == 4):
                            self.patientManager.edit_patient_info_by_id()
                        elif (patientChoice == 5):
                            pass 
                        else:
                            print("...Input Invalid...")
                elif (choice == 3):
                    print("Thank you for using our program")
                else:
                    print("...Invalid Input...")
            else:
                print("So let me guess... You tried to enter something that's not a number.\n Try again...")

### --------------------------------------------------------------------------------------------------------
### It begins
### --------------------------------------------------------------------------------------------------------
display_menu()