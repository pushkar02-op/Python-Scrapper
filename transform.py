import pandas as pd


def transform(name):

    data = pd.read_csv(name)

    data.fillna(0, inplace=True)
    data["Rank"] = data["Rank"].str.extract("(\d+)", expand=False)
    data["Tournament_tier"] = data["Tournament_tier"].str[2:]
    data["Tournament_tier"] = data["Tournament_tier"].str.replace("-Tier", "")
    print(data)

    data.to_csv(name, index=False)
    data.to_excel("File_folder/file1.xlsx", index=False)
