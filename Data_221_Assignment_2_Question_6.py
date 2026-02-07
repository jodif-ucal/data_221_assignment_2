import pandas as pd

#Loading data from csv file
crime_data_frame = pd.read_csv("csv_and_txt_files/crime.csv")

#Creating a new column called risk, and having the filed equal to HighCrime if violent crimes per
# population was equal or greater than 0.5%, and equal to LowCrime if otherwise
crime_data_frame.loc[crime_data_frame["ViolentCrimesPerPop"] >= 0.5, "risk"] = "HighCrime"
crime_data_frame.loc[crime_data_frame["ViolentCrimesPerPop"] < 0.5, "risk"] = "LowCrime"

#Calculating the percentage of the average unemployment rate for regions with high crime
average_unemployment_rate_for_high_risk_crime = float(
    crime_data_frame[crime_data_frame["risk"] == "HighCrime"].PctUnemployed.sum() /
    len(crime_data_frame.loc[crime_data_frame["risk"] == "HighCrime"])
) * 100

#Calculating the percentage of the average unemployment rate for regions with low crime
average_unemployment_rate_for_low_risk_crime = float(
    crime_data_frame[crime_data_frame["risk"] == "LowCrime"].PctUnemployed.sum() /
    len(crime_data_frame.loc[crime_data_frame["risk"] == "LowCrime"])
) * 100

#Printing results
print(f"Average unemployment rate for regions with high crime: {average_unemployment_rate_for_high_risk_crime:.2f}%")
print(f"Average unemployment rate for regions with low crime: {average_unemployment_rate_for_low_risk_crime:.2f}%")