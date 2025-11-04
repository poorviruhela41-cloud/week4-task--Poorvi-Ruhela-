
from models.student import Student
from utils.file_handler import save_to_csv, load_from_csv
from utils.analysis import analyze_data, visualize_data

students = []
df = load_from_csv()

while True:
    print("\n==== Student Dashboard ====")
    print("1. Add Student")
    print("2. Save Data")
    print("3. Analyze Data")
    print("4. Visualize Data")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        roll_no = input("Enter roll no: ")
        scores = {
            "Math": int(input("Math score: ")),
            "Science": int(input("Science score: ")),
            "English": int(input("English score: "))
        }
        students.append(Student(name, roll_no, scores))

    elif choice == "2":
        save_to_csv(students)

    elif choice == "3":
        analyze_data(load_from_csv())

    elif choice == "4":
        visualize_data(load_from_csv())

    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice. Try again.")