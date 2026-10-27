\# Student Grade Calculator



\## 1. Project Overview and Objectives



The Student Grade Calculator is a command-line application developed using Python as part of Week 2 of the Developers Arena Python Internship tasks.



The application accepts a student's name and marks, determines the corresponding grade, and displays the result along with a performance-based feedback message.



\### Objectives



\* Develop a simple Python application using fundamental programming concepts.

\* Accept and process user input.

\* Implement conditional statements for grade calculation.

\* Display student results in a clear and readable format.

\* Practice writing, executing, testing, and documenting Python code.



\## 2. Features



\* Accepts the student's name.

\* Accepts marks between 0 and 100.

\* Calculates the grade based on the marks obtained.

\* Displays the student's name, marks, and grade.

\* Provides feedback corresponding to the student's performance.

\* Uses a simple command-line interface.



\## 3. Technologies Used



\* \*\*Programming Language:\*\* Python 3

\* \*\*Interface:\*\* Command Line

\* \*\*Development Tools:\*\* Python-compatible editor and Command Prompt

\* \*\*Version Control:\*\* Git

\* \*\*Repository Hosting:\*\* GitHub



\## 4. Setup and Installation Instructions



\### Prerequisites



Install Python 3 on your computer.



Verify the installation by running:



```bash

python --version

```



Git is required if you want to clone the repository.



\### Clone the Repository



```bash

git clone https://github.com/Sankarshancn-lab/developers-arena-python-tasks.git

```



\### Navigate to the Project Directory



```bash

cd developers-arena-python-tasks/Week-2

```



\### Run the Application



Execute the following command:



```bash

python grade\_calculator.py

```



Enter the student's name and marks when prompted. The application will calculate the grade and display the result.



\## 5. Code Structure Explanation



\### `grade\_calculator.py`



This is the main Python program.



It is responsible for:



1\. Accepting the student's name.

2\. Reading the student's marks.

3\. Evaluating the marks using conditional statements.

4\. Assigning the appropriate grade.

5\. Displaying the result and performance feedback.



\### `test\_cases.txt`



This file contains test cases for checking the application's behavior with different marks and inputs.



The test cases help verify whether the program produces the expected grades for the inputs provided.



\### `screenshots/`



This directory stores screenshots demonstrating the application's execution and output.



\## 6. Grading System



The application uses the following grading ranges, as implemented in the program:



| Marks  | Grade |

| ------ | ----- |

| 90–100 | A     |

| 80–89  | B     |

| 70–79  | C     |

| 60–69  | D     |

| 0–59   | F     |



\## 7. Sample Execution



The following example demonstrates a successful execution of the application.



```text

Enter student name: sanku

Enter marks (0-100): 80



\--- Student Result ---

Student Name: sanku

Marks: 80/100

Grade: B

Very Good! Keep it up!

```



The application accepts the input, calculates the grade, and displays the corresponding feedback.



\## 8. Screenshots of the Working Application



Screenshots demonstrating the program's execution are stored in the `screenshots/` directory.



Recommended screenshots include:



\* \*\*Successful Execution:\*\* Shows the student name, marks, calculated grade, and feedback.

\* \*\*Grade Verification:\*\* Shows the output for different marks and their corresponding grades.

\* \*\*Input Validation:\*\* Shows how the application responds to invalid inputs, if input validation is implemented.



All screenshots should represent actual program executions.



\## 9. Technical Requirements and Implementation



\### User Input and Output



The program accepts the student's name and marks through the command line and displays the calculated result.



\### Conditional Statements



Conditional statements are used to compare the marks against the grading ranges and determine the appropriate grade.



\### Grade Calculation



The program maps the marks entered by the user to the corresponding grade according to the defined grading system.



\### Performance Feedback



The program displays a feedback message based on the grade obtained by the student.



\### Testing



The `test\_cases.txt` file documents test cases used to verify the application's behavior.



\### Python Programming Fundamentals



The project demonstrates fundamental Python concepts, including variables, user input, conditional logic, and formatted output. Any additional concepts should be documented according to their actual implementation in the source code.



\## 10. Project Directory Structure



```text

Week-2/

├── README.md

├── grade\_calculator.py

├── test\_cases.txt

└── screenshots/

&#x20;   ├── successful\_execution.png

&#x20;   └── grade\_verification.png

```



The screenshot filenames above are examples. Replace them with the actual filenames of your screenshots.



\## 11. Author



\*\*Sankarshan CN\*\*



Developers Arena Python Internship — Week 2



