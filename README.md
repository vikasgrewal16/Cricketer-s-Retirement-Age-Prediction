# Retirement-Age-Prediction
Developed machine learning model based on LSTM 

## Introduction

Cricket is a sport where individual performances significantly impact match outcomes. Understanding factors influencing a player's retirement age is crucial for effective team management and player selection. This project proposes an LSTM-based approach to predict the retirement age of test batters based on their batting statistics.

## Methodology

### Data Collection

Raw batting statistics of 100 retired test batters were obtained from HowSTAT website, comprising runs scored, balls faced, cumulative runs, and other relevant metrics for each innings.

### Data Preprocessing

1. **Discretization**: Relevant data based on the number of innings played by each player was extracted.
2. **Normalization**: Attributes were normalized for better assessment.
3. **Cleaning**: Missing values were filled to avoid discrepancies.
4. **Integration**: Data files were integrated, and the dataset was split into training and testing sets.

### Feature Extraction

Only relevant data was retained, and new features were created through mathematical operations on existing features, including debut age, longest gap between consecutive innings, time of best and worst moving averages, number of innings, and time of the last score in the top 20% best scores.

The final Features given to the first model are:
1. Current Age (in years)
2. Debut Age (in years)
3. Innings Played till date
4. Cumulative runs scored
5. Number of fifties scored
6. Number of innings in last 3 years
The final features given to the second model are:
1. Debut Age (in years)
2. Total innings predicted from model 1
3. Cumulative runs scored
4. Number of fifties scored

## Conclusion

This project offers an LSTM-based approach for predicting retirement age in cricket, facilitating effective player management. Further analysis of results and future research directions are discussed.
