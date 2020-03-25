"""
Overview:
    Creates graphs from COVID-19 data
Dependencies:
    packages: pandas, matplotlib 
    data files: time_series_covid19_confirmed_global.csv
"""

import pandas as pd
import matplotlib.pyplot as plt

CONFIRMED_FILE_NAME = "time_series_covid19_confirmed_global.csv"

# Create dataframe from csv
confirmed = pd.read_csv(CONFIRMED_FILE_NAME, parse_dates=True)

# Get rid of location columns and sum cases across each country's provinces
country = confirmed.drop(['Lat','Long'], axis=1).groupby("Country/Region").sum()

# sort countries by most confirmed cases on most recent date
country.sort_values(by=country.iloc[:,-1].name, ascending=False, inplace=True)

# Transpose to make Data the index vs country
country = country.T

# Line graph of Top 5 countries with most confirmed cases
country.iloc[:, 0:5].plot()
plt.title('Top 5 Confirmed Countries')
plt.savefig('top_5_countries_confirmed.png')
plt.show()
