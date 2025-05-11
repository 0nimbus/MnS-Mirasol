import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
data = pd.read_csv("Japan_life_expectancy.csv")

# Basic histogram with matplotlib
plt.figure(figsize=(10, 6))
plt.hist(data["Life_expectancy"], bins=10, color="skyblue", edgecolor="black")
plt.title("Distribution of Life Expectancy in Japanese Prefectures")
plt.xlabel("Life Expectancy (years)")
plt.ylabel("Number of Prefectures")
plt.grid(axis="y", alpha=0.75)
plt.savefig("life_expectancy_histogram_matplotlib.png")
plt.show()

# More advanced histogram with seaborn
plt.figure(figsize=(10, 6))
sns.histplot(data=data, x="Life_expectancy", kde=True, color="skyblue", bins=10)
plt.title("Distribution of Life Expectancy in Japanese Prefectures")
plt.xlabel("Life Expectancy (years)")
plt.ylabel("Number of Prefectures")
plt.savefig("life_expectancy_histogram_seaborn.png")
plt.show()