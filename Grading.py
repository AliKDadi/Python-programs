# Zetech University Grading System

def calculate_grade(score):
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 40:
        return 'D'
    else:
        return 'E (Fail) - Supplementary Examination Required'

def main():
    try:
        # Get the student's score from input
        score = int(input("Enter the student's score (0-100): "))
        
        # Validate the score range
        if score < 0 or score > 100:
            print("Invalid score! Please enter a score between 0 and 100.")
        else:
            grade = calculate_grade(score)
            print(f"The student's grade is: {grade}")
            
    except ValueError:
        print("Invalid input! Please enter a numeric score.")

# Run the program
if __name__ == "__main__":
    main()
