# Hospital Patient Management System

patients = []


def add_patient():
    patient = {}

    pid = int(input("Enter Patient ID: "))

    for p in patients:
        if p["PatientId"] == pid:
            print("Patient ID already exists.")
            return

    patient["PatientId"] = pid
    patient["PatientName"] = input("Enter Patient Name: ")

    age = int(input("Enter Age: "))
    if age <= 0:
        print("Age must be greater than zero.")
        return
    patient["Age"] = age

    patient["City"] = input("Enter City: ")
    patient["Visits"] = []

    patients.append(patient)
    print("Patient added successfully.")


def add_visit():
    pid = int(input("Enter Patient ID: "))
    found = False

    for patient in patients:
        if patient["PatientId"] == pid:
            found = True

            vid = int(input("Enter Visit ID: "))

            for visit in patient["Visits"]:
                if visit["VisitId"] == vid:
                    print("Visit ID already exists.")
                    return

            visit = {}

            visit["VisitId"] = vid
            visit["DoctorName"] = input("Enter Doctor Name: ")
            visit["Department"] = input("Enter Department: ")

            fee = float(input("Enter Consultation Fee: "))
            if fee < 0:
                print("Consultation Fee cannot be negative.")
                return
            visit["ConsultationFee"] = fee

            cost = float(input("Enter Medicines Cost: "))
            if cost < 0:
                print("Medicines Cost cannot be negative.")
                return
            visit["MedicinesCost"] = cost

            visit["Status"] = input("Enter Status: ")

            patient["Visits"].append(visit)
            print("Visit added successfully.")
            return

    if found == False:
        print("Patient not found.")


def view_patients():
    if len(patients) == 0:
        print("No patient records found.")
        return

    for patient in patients:

        print("\nPatient ID :", patient["PatientId"])
        print("Patient Name :", patient["PatientName"])
        print("Age :", patient["Age"])
        print("City :", patient["City"])

        if len(patient["Visits"]) == 0:
            print("No Visits.")
        else:

            for visit in patient["Visits"]:

                print("\nVisit ID :", visit["VisitId"])
                print("Doctor Name :", visit["DoctorName"])
                print("Department :", visit["Department"])
                print("Consultation Fee :", visit["ConsultationFee"])
                print("Medicines Cost :", visit["MedicinesCost"])
                print("Status :", visit["Status"])

        print("----------------------------------------")


def search_patient():
    pid = int(input("Enter Patient ID: "))

    for patient in patients:

        if patient["PatientId"] == pid:

            print("\nPatient ID :", patient["PatientId"])
            print("Patient Name :", patient["PatientName"])
            print("Age :", patient["Age"])
            print("City :", patient["City"])
            print("Total Visits :", len(patient["Visits"]))

            for visit in patient["Visits"]:

                print("\nVisit ID :", visit["VisitId"])
                print("Doctor Name :", visit["DoctorName"])
                print("Department :", visit["Department"])
                print("Consultation Fee :", visit["ConsultationFee"])
                print("Medicines Cost :", visit["MedicinesCost"])
                print("Status :", visit["Status"])

            return

    print("Patient not found.")
    
def update_visit_status():
    pid = int(input("Enter Patient ID: "))
    vid = int(input("Enter Visit ID: "))

    for patient in patients:
        if patient["PatientId"] == pid:

            for visit in patient["Visits"]:
                if visit["VisitId"] == vid:

                    status = input("Enter New Status: ")
                    visit["Status"] = status

                    print("Visit status updated successfully.")
                    return

            print("Visit not found.")
            return

    print("Patient not found.")


def total_medical_bill():
    pid = int(input("Enter Patient ID: "))

    for patient in patients:

        if patient["PatientId"] == pid:

            total = 0

            for visit in patient["Visits"]:

                bill = visit["ConsultationFee"] + visit["MedicinesCost"]

                print("Visit", visit["VisitId"], "Bill :", bill)

                total = total + bill

            print("-----------------------")
            print("Total Bill :", total)

            return

    print("Patient not found.")


def multiple_visits():
    found = False

    for patient in patients:

        if len(patient["Visits"]) > 2:

            print("\nPatient ID :", patient["PatientId"])
            print("Patient Name :", patient["PatientName"])
            print("Number of Visits :", len(patient["Visits"]))

            found = True

    if found == False:
        print("No patients found with more than two visits.")


def department_visit_count():

    if len(patients) == 0:
        print("No patient records found.")
        return

    departments = []

    for patient in patients:
        for visit in patient["Visits"]:
            if visit["Department"] not in departments:
                departments.append(visit["Department"])

    for dept in departments:

        count = 0

        for patient in patients:
            for visit in patient["Visits"]:
                if visit["Department"] == dept:
                    count += 1

        print(dept, ":", count)


def highest_medical_bill():

    if len(patients) == 0:
        print("No patient records found.")
        return

    highest_patient = None
    highest_bill = 0

    for patient in patients:

        total = 0

        for visit in patient["Visits"]:
            total = total + visit["ConsultationFee"] + visit["MedicinesCost"]

        if total > highest_bill:
            highest_bill = total
            highest_patient = patient

    if highest_patient != None:

        print("\nPatient with Highest Medical Bill")
        print("Patient ID :", highest_patient["PatientId"])
        print("Patient Name :", highest_patient["PatientName"])
        print("Total Bill :", highest_bill)
        
def remove_visit():
    pid = int(input("Enter Patient ID: "))
    vid = int(input("Enter Visit ID: "))

    for patient in patients:

        if patient["PatientId"] == pid:

            for visit in patient["Visits"]:

                if visit["VisitId"] == vid:
                    patient["Visits"].remove(visit)
                    print("Visit removed successfully.")
                    return

            print("Visit not found.")
            return

    print("Patient not found.")


while True:

    print("\n========== Hospital Patient Management System ==========")
    print("1. Add New Patient")
    print("2. Add Medical Visit")
    print("3. View All Patients")
    print("4. Search Patient by ID")
    print("5. Update Visit Status")
    print("6. Calculate Total Medical Bill")
    print("7. Display Patients with Multiple Visits")
    print("8. Display Department-wise Visit Count")
    print("9. Find Patient with Highest Medical Bill")
    print("10. Remove Visit Record")
    print("11. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_patient()

    elif choice == 2:
        add_visit()

    elif choice == 3:
        view_patients()

    elif choice == 4:
        search_patient()

    elif choice == 5:
        update_visit_status()

    elif choice == 6:
        total_medical_bill()

    elif choice == 7:
        multiple_visits()

    elif choice == 8:
        department_visit_count()

    elif choice == 9:
        highest_medical_bill()

    elif choice == 10:
        remove_visit()

    elif choice == 11:
        print("Thank you for using Hospital Patient Management System.")
        break

    else:
        print("Invalid Choice. Please try again.")