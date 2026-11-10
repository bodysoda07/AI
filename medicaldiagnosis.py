
def medical_diagnosis():

    while True:

        print("\n--- MEDICAL DIAGNOSIS SYSTEM ---")

        fever = input("Do you have fever? (yes/no): ")
        cough = input("Do you have cough? (yes/no): ")
        headache = input("Do you have headache? (yes/no): ")
        sneezing = input("Do you have sneezing? (yes/no): ")
        bodypain = input("Do you have body pain? (yes/no): ")

        if fever == "yes" and cough == "yes" and bodypain == "yes":
            print("\nClosest Match: Flu")
            print("Description: A viral infection causing fever, cough and body pain.")
            print("Recommended Care: Take rest, drink fluids and consult a doctor.")

        elif sneezing == "yes" and cough == "yes":
            print("\nClosest Match: Common Cold")
            print("Description: A viral infection affecting the nose and throat.")
            print("Recommended Care: Take rest and drink plenty of fluids.")

        elif fever == "yes" and headache == "yes":
            print("\nClosest Match: Possible Malaria")
            print("Description: A mosquito-borne disease that can cause fever and headache.")
            print("Recommended Care: Consult a doctor for testing and appropriate treatment.")

        elif sneezing == "yes":
            print("\nClosest Match: Possible Allergy")
            print("Description: An immune reaction to substances like dust or pollen.")
            print("Recommended Care: Avoid allergens and consult a healthcare professional.")

        else:
            print("\nNo matching disease found.")
            print("Please consult a doctor.")

        choice = input("\nWould you like to diagnose another case? (yes/no): ")

        if choice.lower() != "yes":
            break

    print("\nThank you for using the Medical Diagnosis System!")


medical_diagnosis()
