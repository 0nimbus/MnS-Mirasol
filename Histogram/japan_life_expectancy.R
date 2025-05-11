# Load necessary libraries
library(ggplot2)

# Read the CSV file
data <- read.csv("Japan_life_expectancy.csv")

# Basic histogram with base R
hist(data$Life_expectancy, 
     main = "Distribution of Life Expectancy in Japanese Prefectures",
     xlab = "Life Expectancy (years)",
     ylab = "Number of Prefectures",
     col = "lightblue",
     border = "black")

# More advanced histogram with ggplot2
ggplot(data, aes(x = Life_expectancy)) +
  geom_histogram(binwidth = 0.5, fill = "skyblue", color = "black") +
  labs(title = "Distribution of Life Expectancy in Japanese Prefectures",
       x = "Life Expectancy (years)",
       y = "Number of Prefectures") +
  theme_minimal()

# Save the plot
ggsave("life_expectancy_histogram_r.png")