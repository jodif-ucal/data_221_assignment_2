import pandas as pd

with open("csv_and_txt_files/student.csv", "r") as csv_file:
    students_data = pd.DataFrame(pd.read_csv(csv_file))

students_data.loc[students_data["grade"] <= 9, "grade_band"] = "low"
students_data.loc[(students_data["grade"] < 15) & (students_data["grade"] > 9), "grade_band"] = "medium"
students_data.loc[students_data["grade"] >= 15, "grade_band"] = "high"


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

student_bands_data_frame = pd.DataFrame(
    {
        "Low grade bound": low_category,
        "Medium grade bound": medium_category,
        "High grade bound": high_category
    }
)

student_bands_data_frame.to_csv("csv_and_txt_files/student_bands.csv")