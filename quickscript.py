import pandas as pd

finaltext = ""

col_list = ["web-scraper-order", "web-scraper-start-url","link","link-href"]

df = pd.read_csv("kboges.csv", usecols=col_list)


for link in list(df["link-href"]):
    finaltext = finaltext + " " + str(link)
print(finaltext)