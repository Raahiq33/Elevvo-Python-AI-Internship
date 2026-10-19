
# Elevvo Internship - Task 2
# Student Grade Processor
# Author: Mohamed Raahiq

from grades import (
    calculate_average,
    highest_mark,
    lowest_mark,
    get_result,
)

students = [
    {"name": "Raahiq", "marks": [85, 90, 78]},
    {"name": "Ahmed", "marks": [60, 75, 80]},
    {"name": "Kamal", "marks": [30, 40, 35]},
]

print("===== STUDENT GRADE PROCESSOR =====")

for student in students:
    name = student["name"]
    marks = student["marks"]

    try:
        print(f"\nStudent Name: {name}")
        print(f"Marks: {marks}")
        print(f"Average: {calculate_average(marks):.2f}")
        print(f"Highest Mark: {highest_mark(marks)}")
        print(f"Lowest Mark: {lowest_mark(marks)}")
        print(f"Result: {get_result(marks)}")
        print("-----------------------------")

    except ValueError as error:
        print(f"Error for {name}: {error}")
