import pandas as pd

#Loading data
with open("csv_and_txt_files/student.csv", "r") as csv_file:
    students_data = pd.DataFrame(pd.read_csv(csv_file))

#Creating the new grade_band column and setting the values for each student based on their grade
students_data.loc[students_data["grade"] <= 9, "grade_band"] = "low"
students_data.loc[(students_data["grade"] < 15) & (students_data["grade"] > 9), "grade_band"] = "medium"
students_data.loc[students_data["grade"] >= 15, "grade_band"] = "high"

#Creating the dictionaries that will be used as columns with their data for the final DataFrame

#The dictionary for the low grade band
low_category = {
    "number of students": len(students_data.loc[students_data["grade_band"] == "low"]),
    "average absences": float(
        students_data[students_data["grade_band"] == "low"].absences.sum() /
        len(students_data.loc[students_data["grade_band"] == "low"])
    ),
    "percentage of students with internet access": float(
        students_data[students_data["grade_band"] == "low"].internet.sum() /
        len(students_data.loc[students_data["grade_band"] == "low"])
    ) * 100
}

#The dictionary for the medium grade band
medium_category = {
    "number of students": len(students_data.loc[students_data["grade_band"] == "medium"]),
    "average absences": float(
        students_data[students_data["grade_band"] == "medium"].absences.sum() /
        len(students_data.loc[students_data["grade_band"] == "medium"])
    ),
    "percentage of students with internet access": float(
        students_data[students_data["grade_band"] == "medium"].internet.sum() /
        len(students_data.loc[students_data["grade_band"] == "medium"])
    ) * 100
}

#The dictionary for the high grade band
high_category = {
    "number of students": len(students_data.loc[students_data["grade_band"] == "high"]),
    "average absences": float(
        students_data[students_data["grade_band"] == "high"].absences.sum() /
        len(students_data.loc[students_data["grade_band"] == "high"])
    ),
    "percentage of students with internet access": float(
        students_data[students_data["grade_band"] == "high"].internet.sum() /
        len(students_data.loc[students_data["grade_band"] == "high"])
    ) * 100
}

# Saving all the previous dictionaries into the final DataFrame
student_bands_data_frame = pd.DataFrame(
    [low_category, medium_category, high_category],
    index=["Low grade band", "Medium grade band", "High grade band"]
)

#Saving the data frame into the csv file
student_bands_data_frame.to_csv("csv_and_txt_files/student_bands.csv")