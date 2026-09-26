import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("covid.csv")

df.head()

df.shape

df.info()

df.describe()

df.isnull().sum()

df.duplicated().sum()

df["Date"] = pd.to_datetime(df["Date"])

df["Active_Cases"] = df["Confirmed"] - df["Recovered"] - df["Deaths"]

df["Recovery_Rate"] = (df["Recovered"] / df["Confirmed"]) * 100

df["Death_Rate"] = (df["Deaths"] / df["Confirmed"]) * 100

total_confirmed = df["Confirmed"].sum()

total_recovered = df["Recovered"].sum()

total_deaths = df["Deaths"].sum()

total_active = df["Active_Cases"].sum()

print("Total Confirmed Cases:", total_confirmed)
print("Total Recovered Cases:", total_recovered)
print("Total Deaths:", total_deaths)
print("Total Active Cases:", total_active)

print("Average Confirmed Cases:", np.mean(df["Confirmed"]))

print("Maximum Confirmed Cases:", np.max(df["Confirmed"]))

print("Maximum Deaths:", np.max(df["Deaths"]))

print("Average Recovery Rate:", np.mean(df["Recovery_Rate"]))

print("Average Death Rate:", np.mean(df["Death_Rate"]))

daily_cases = df.groupby("Date")["Confirmed"].sum()

daily_cases.plot(
    figsize=(12, 6)
)

plt.title("COVID-19 Confirmed Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Confirmed Cases")
plt.tight_layout()
plt.show()

df.groupby("Date")["Deaths"].sum().plot(
    figsize=(12, 6)
)

plt.title("COVID-19 Deaths Over Time")
plt.xlabel("Date")
plt.ylabel("Deaths")
plt.tight_layout()
plt.show()

df.groupby("Date")["Recovered"].sum().plot(
    figsize=(12, 6)
)

plt.title("COVID-19 Recoveries Over Time")
plt.xlabel("Date")
plt.ylabel("Recovered Cases")
plt.tight_layout()
plt.show()

df.groupby("Country")["Confirmed"].sum().sort_values(
    ascending=False
).head(10).plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Top 10 Countries by Confirmed Cases")
plt.xlabel("Country")
plt.ylabel("Confirmed Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.groupby("Country")["Deaths"].sum().sort_values(
    ascending=False
).head(10).plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Top 10 Countries by Deaths")
plt.xlabel("Country")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.groupby("Country")["Recovered"].sum().sort_values(
    ascending=False
).head(10).plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title("Top 10 Countries by Recoveries")
plt.xlabel("Country")
plt.ylabel("Recovered Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

df.groupby("Date")["Active_Cases"].sum().plot(
    figsize=(12, 6)
)

plt.title("Active COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Active Cases")
plt.tight_layout()
plt.show()

print("Highest Confirmed Cases Date:", daily_cases.idxmax())

print("Highest Confirmed Cases:", daily_cases.max())

print("Total Countries:", df["Country"].nunique())

print("Average Recovery Rate:", round(df["Recovery_Rate"].mean(), 2))

print("Average Death Rate:", round(df["Death_Rate"].mean(), 2))