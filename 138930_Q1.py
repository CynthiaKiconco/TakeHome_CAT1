#A method to add patients
def add_patient(patients_list):
    name = input("Enter patient's name: ")
    age = input("Enter patient's age: ")
    illness = input("Enter patient's illness: ")
    patient = {'name': name, 'age': age, 'illness': illness}  #dictionary
    patients_list.append(patient)
    print(f'Patient {name} added.\n')

#method to list patients
def display_patients(patients_list):
    if patients_list:
        print("List of Patients:")
        for patient in patients_list:
            print(f"Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}")
    else:
        print("No patients found.\n")

#method to search for a patient
def search_patient(patients_list):
    name = input("Enter patient's name to search: ")
    for patient in patients_list:
        if patient['name'].lower() == name.lower():
            print(f"Patient found: Name: {patient['name']}, Age: {patient['age']}, Illness: {patient['illness']}\n")
            return
    print("Patient not found.\n")

#method to remove a patient 
def remove_patient(patients_list):
    name = input("Enter patient's name to remove: ")
    for patient in patients_list:
        if patient['name'].lower() == name.lower():
            patients_list.remove(patient)
            print(f"Patient {name} removed.\n")
            return
    print("Patient not found.\n")
 
 #method to invoke input from user
def main():
    patients_list = []
    while True:
        print("1. Add a new patient")
        print("2. Display all patients")
        print("3. Search for a patient by name")
        print("4. Remove a patient by name")
        print("5. Exit")
        choice = input("Enter your choice: ")
#loop
        if choice == '1':
            add_patient(patients_list)
        elif choice == '2':
            display_patients(patients_list)
        elif choice == '3':
            search_patient(patients_list)
        elif choice == '4':
            remove_patient(patients_list)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()