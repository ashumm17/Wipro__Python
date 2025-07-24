student_records = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("Enter a name: ")

if name in student_records:
    marks = student_records[name]
    average = sum(marks) / len(marks)
    print(f"Average percentage mark: {average}")
else:
    print("Student not found.")
