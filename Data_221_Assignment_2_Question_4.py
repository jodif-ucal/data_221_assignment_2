import pandas as pd

with open("csv_and_txt_files/student.csv", "r") as csv_file:
    students_data = pd.DataFrame(pd.read_csv(csv_file))

high_engagement_students = students_data[
    (students_data["studytime"] >= 3) &
    (students_data["internet"] == 1) &
    (students_data["absences"] <= 5)
]

high_engagement_students.to_csv("csv_and_txt_files/high_engagement.csv")

number_of_high_engagement_students = len(high_engagement_students)
print("Number of highly engaged students: ", number_of_high_engagement_students)
print("Average of their grades: ", high_engagement_students.grade.sum() / number_of_high_engagement_students)