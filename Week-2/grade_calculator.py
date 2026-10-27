# Student Grade Calculator

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep it up!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up!"
    elif marks >= 70:
        return "C", "Good effort! Keep improving!"
    elif marks >= 60:
        return "D", "You passed! Keep practising!"
    else:
        return "F", "Don't give up! Keep learning!"


def get_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid marks. Enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    name = input("Enter student name: ").strip()

    while not name:
        print("Name cannot be empty.")
        name = input("Enter student name: ").strip()

    marks = get_marks()
    grade, message = calculate_grade(marks)

    print("\n--- Student Result ---")
    print(f"Student Name: {name}")
    print(f"Marks: {marks:g}/100")
    print(f"Grade: {grade}")
    print(message)


if __name__ == "__main__":
    main()