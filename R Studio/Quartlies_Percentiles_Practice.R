install.packages("tidyverse")
install.packages("readxl")
install.packages("dpylr")

library(tidyverse)
library(readxl)
library(dplyr)

# Filter observations to include only play sessions and not initial purchases.
filtered_data = filter(steam_200k,session_type == "play")

# Filter data to include only game play sessions that are at least 5 minutes long.
filtered_data = filter(steam_200k,time_played > 1)

# Sort our filtered data into ascending order by playtime.
filtered_data <- filtered_data %>% arrange(time_played)

# Determine Q1 and Q3 time_played observations.
quarterlies = quantile(filtered_data$time_played, probs=c(0.25, 0.75))

# Filter data to include only time_played observations to the right (great than) Q1
# and to the left (less than) Q3 to reduce outliers.
filtered_data <- filter(filtered_data ,time_played > quarterlies[1][["25%"]] & time_played < quarterlies[2][["75%"]])
filtered_data <- filtered_data %>% arrange(time_played)

# Combine all observations of the same game_name and total of their time_played
summary_data <- filtered_data %>% group_by(game_name) %>% summarize(time_played)
summary_data = aggregate(time_played~.,summary_data,FUN=sum)

# Organize results in descending order, put games with the most time_played at the top
summary_data <- summary_data %>% arrange(desc(time_played))