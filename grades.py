#Task-2-Student-Grade-Processor/grades.py Elevvo Internship - Task 2
# Student Grade Processor
# Author: Mohamed Raahiq


def validate_marks(marks):
    if not marks:
        raise ValueError("Marks list cannot be empty")

    for mark in marks:
        if type(mark) not in (int, float):
            raise ValueError("Marks must be numbers")

        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")


def calculate_average(marks):
    validate_marks(marks)
    return sum(marks) / len(marks)


def highest_mark(marks):
    validate_marks(marks)
    return max(marks)


def lowest_mark(marks):
    validate_marks(marks)
    return min(marks)


def get_result(marks):
    average = calculate_average(marks)

    if average >= 50:
        return "PASS"
    else:
        return "FAIL"
