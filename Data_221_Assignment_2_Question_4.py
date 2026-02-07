import pandas as pd

#Loading the data from the csv file, using the pandas.read_csv method
with open("csv_and_txt_files/student.csv", "r") as csv_file:
    students_data = pd.DataFrame(pd.read_csv(csv_file))

#Filtering the data. The & operator means 'AND' in this case, so it takes all conditions into consideration
#Filtering by study time, internet time and number of absences
high_engagement_students = students_data[
    (students_data["studytime"] >= 3) &
    (students_data["internet"] == 1) &
    (students_data["absences"] <= 5)
]

#Saving the data into a new csv file
high_engagement_students.to_csv("csv_and_txt_files/high_engagement.csv")

#Getting the number of rows in the filtered data frame
number_of_high_engagement_students = len(high_engagement_students)

#Printing the data
print("Number of highly engaged students: ", number_of_high_engagement_students)
print("Average of their grades: ", high_engagement_students.grade.sum() / number_of_high_engagement_students)