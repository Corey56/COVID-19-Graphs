"""
Downloads CSV Files from John's Hopkins COVID-19 study at
https://github.com/CSSEGISandData/COVID-19
"""

import urllib.request

# URL of data repository
URL = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_co\
vid_19_data/csse_covid_19_time_series/"

# 3 Files to download from repo
FILENAMES = ['time_series_19-covid-Confirmed.csv'
             , 'time_series_19-covid-Deaths.csv'
             , 'time_series_19-covid-Recovered.csv']

for fn in FILENAMES:
    print(f"Fetching File: {fn}", end='')
    response = urllib.request.urlopen(URL+fn) #fetch file from GitHub
    data = response.read()                    # a `bytes` object
    text = data.decode('utf-8')               # a `str`
    print(" -> Storing Locally")
    with open(fn, 'w', newline='') as fh:
        fh.write(text)                        # store each file locally