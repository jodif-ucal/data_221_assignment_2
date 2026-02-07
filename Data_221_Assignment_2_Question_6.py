import pandas as pd

crime_data_frame = pd.read_csv("csv_and_txt_files/crime.csv")

crime_data_frame.loc[crime_data_frame["ViolentCrimesPerPop"] >= 0.5, "risk"] = "HighCrime"
crime_data_frame.loc[crime_data_frame["ViolentCrimesPerPop"] < 0.5, "risk"] = "LowCrime"

average_unemployment_rate_for_high_risk_crime = float(
    crime_data_frame[crime_data_frame["risk"] == "HighCrime"].PctUnemployed.sum() /
    len(crime_data_frame.loc[crime_data_frame["risk"] == "HighCrime"])
) * 100

average_unemployment_rate_for_low_risk_crime = float(
    crime_data_frame[crime_data_frame["risk"] == "LowCrime"].PctUnemployed.sum() /
    len(crime_data_frame.loc[crime_data_frame["risk"] == "LowCrime"])
) * 100

print(f"Average unemployment rate for regions with high crime: {average_unemployment_rate_for_high_risk_crime:.2f}%")
print(f"Average unemployment rate for regions with low crime: {average_unemployment_rate_for_low_risk_crime:.2f}%")