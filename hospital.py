class Hospital:
    def __init__(self, name, location, rating):
        self.name = name
        self.location = location
        self.rating = rating


class MedicalFacility:
    def __init__(self, name, location, rating):
        self.name = name
        self.location = location
        self.rating = rating


class ExpertSystem:
    def __init__(self):
        self.hospitals = []
        self.medical_facilities = []

    def add_hospital(self, name, location, rating):
        hospital = Hospital(name, location, rating)
        self.hospitals.append(hospital)

    def add_medical_facility(self, name, location, rating):
        medical_facility = MedicalFacility(name, location, rating)
        self.medical_facilities.append(medical_facility)

    def find_best_hospital(self, location):
        best_hospital = None
        max_rating = 0

        for hospital in self.hospitals:
            if hospital.location == location and hospital.rating > max_rating:
                best_hospital = hospital
                max_rating = hospital.rating

        return best_hospital

    def find_best_medical_facility(self, location):
        best_medical_facility = None
        max_rating = 0

        for facility in self.medical_facilities:
            if facility.location == location and facility.rating > max_rating:
                best_medical_facility = facility
                max_rating = facility.rating

        return best_medical_facility
    
    def check_disease(self,symptoms):
        if all(symptom in symptoms for symptom in ["headache", "sore_throat", "runny_nose", "sneezing"]):
            print("The disease is cold")
        elif all(symptom in symptoms for symptom in ["headache", "sore_throat", "fever", "body_ache"]):
            print("The disease is jaundice")
        elif all(symptom in symptoms for symptom in ["headache", "sore_throat", "fever", "chills", "body_ache"]):
            print("The disease is typhoid")
        else:
            print("You have no disease")
        
        return 'You need to take rest'

def main():
    expert_system = ExpertSystem()

    # Add hospitals and medical facilities to the expert system
    expert_system.add_hospital("Hospital A", "Pune", 3)
    expert_system.add_hospital("Hospital B", "Pune", 5)
    expert_system.add_hospital("Hospital C", "Pune", 4)
    expert_system.add_hospital("Hospital D", "Nashik", 4)
    expert_system.add_hospital("Hospital E", "Nashik", 5)
    expert_system.add_hospital("Hospital F", "Mumbai", 2)
    expert_system.add_hospital("Hospital G", "Mumbai", 4)
    expert_system.add_hospital("Hospital H", "Mumbai", 3)

    expert_system.add_medical_facility("Medical Facility 1", "Pune", 3)
    expert_system.add_medical_facility("Medical Facility 2", "Mumbai", 3)
    expert_system.add_medical_facility("Medical Facility 3", "Nashik", 4)
    expert_system.add_medical_facility("Medical Facility 4", "Mumbai", 4)
    expert_system.add_medical_facility("Medical Facility 5", "Mumbai", 2)
    expert_system.add_medical_facility("Medical Facility 6", "Pune", 4)
    expert_system.add_medical_facility("Medical Facility 7", "Nashik", 5)
    expert_system.add_medical_facility("Medical Facility 8", "Pune", 5)
    
    run = True
    while run:
        # Prompt the user for their preference and location
        preference = input("Enter your preference (hospital/medical facility/dieases/exit): ").lower()
    

        # Find the best hospital or medical facility based on user preference and location
        if preference == "hospital":
            location = input("Enter your location: ")
            best_option = expert_system.find_best_hospital(location)
            # Display the result
            if best_option is None:
                print("No option found that meets the requirements.")
            else:
                print("Best option is:", best_option.name)

        elif preference == "medical facility":
            location = input("Enter your location: ")
            best_option = expert_system.find_best_medical_facility(location)
            # Display the result
            if best_option is None:
                print("No option found that meets the requirements.")
            else:
                print("Best option is:", best_option.name)

        elif preference == 'dieases':
            symptoms = []
            print("Enter the number of symptoms:")
            # num_symptoms = int(input())
            symptom_list = ["headache", "sore_throat", "runny_nose",
                            "sneezing", "abdominal_pain", "fever", "chills", "body_ache"]
            yes = "y"
            for symptom in symptom_list:
                print("Do you have " + symptom + "? (y/n)")
                choice = input().lower()
                if choice == yes:
                    symptoms.append(symptom)

            best_option = expert_system.check_disease(symptoms)
        elif preference == 'exit':
            run = False
        else:
            print("Invalid preference.")
            return

    

if __name__ == "__main__":
    main()
