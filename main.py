import pandas as pd
import requests
from bs4 import BeautifulSoup
from transform import *

# Defining of the dataframe
df = pd.DataFrame(
    columns=[
        "Date_played",
        "Rank",
        "Tournament_tier",
        "Tournament_name",
        "Team_name",
        "Money_Won",
    ]
)


def extract_data(name_to_fetch):
    global df
    print(name_to_fetch)

    URL = "https://liquipedia.net/pubgmobile/" + name_to_fetch + "/Results"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    table = soup.find("table", attrs={"class": "wikitable"})
    table_body = table.find("tbody")

    rows = table_body.find_all("tr")

    for row in rows:
        cols = row.find_all("td")
        if cols != []:
            cols = [ele.text.strip() for ele in cols]
            if len(cols) > 1:
                date_played = cols[0]
                Rank = cols[1]
                Tournament_tier = cols[2]
                Tournament_name = cols[3]
                Team_name = cols[5]
                Money_Won = cols[6]
                df = df.append(
                    {
                        "Date_played": date_played,
                        "Rank": Rank,
                        "Tournament_tier": Tournament_tier,
                        "Tournament_name": Tournament_name,
                        "Team_name": Team_name,
                        "Money_Won": Money_Won,
                    },
                    ignore_index=True,
                )
    df.to_csv("file1.csv")
    df.to_excel("file1.xlsx")
    transform("file1.csv")


def main():
    extract_data("JONATHAN")


main()
