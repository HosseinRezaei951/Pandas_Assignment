# Google Play Data Analysis with Pandas

## Project Overview

This project involves the analysis of the Google Play Store dataset using the Pandas library in Python. The dataset contains information about more than 600,000 applications available on the Google Play Store, and the goal of this project is to clean the data and analyze it to answer specific business questions related to app popularity and user demographics.

## Dataset

The Google Play Store Dataset includes 23 attributes for each application, such as:
- App Name
- App Id
- Category
- Rating
- Rating Count
- Installs
- Minimum Installs
- Maximum Installs
- Free (Boolean)
- Price
- Currency
- Size
- Minimum Android Version
- Developer Id
- Developer Website
- Developer Email
- Release Date
- Privacy Policy
- Last Updated
- Content Rating
- Ad Supported (Boolean)
- In-App Purchases (Boolean)
- Editor's Choice (Boolean)

## Tasks

### 1. Data Cleaning

The first step in this project involves cleaning the dataset:
- **Duplicate Removal**: Identify and remove duplicate rows, both full duplicates and duplicates based on the `App Id` column.
- **Handling Missing Values**: Drop rows with missing values in non-critical columns and replace missing values in critical columns (like `Rating`, `Rating Count`, `Installs`, and `Minimum Installs`) with their mean values.

### 2. Data Analysis

After cleaning the data, we analyze it to answer the following questions:

#### 2.1. Which Category of Ad-Supported Apps is the Most Popular?

To determine the most popular category of ad-supported apps:
- A new column `WRI` (Weighted Rating Index) is created by multiplying `Rating`, `Rating Count`, and `Maximum Installs`.
- The apps are grouped by `Category`, and the average `WRI` is calculated for each group.
- The results are then sorted and visualized using a horizontal bar plot to identify the most popular categories.

#### 2.2. Which Attributes Affect the `Rating` and `Installs` for Ad-Supported Apps?

To identify the attributes that most affect `Rating` and `Installs`:
- The `Installs` column is converted to a numeric format.
- The Pearson correlation coefficient is calculated between all numerical columns, and a heatmap is generated to visualize the relationships between different attributes.

#### 2.3. What Age Group Would You Target?

To determine the ideal age group to target:
- The data is grouped by the `Content Rating` column, which represents different age groups.
- The average `WRI` is calculated for each age group, and the results are visualized using a horizontal bar plot to identify the most promising age group for targeting.

## How to Run the Project

1. **Prerequisites**: Ensure you have Python installed with the following libraries:
   - numpy
   - pandas
   - matplotlib
   - seaborn
   - os (default Python library)

2. **Setup**: Place the `Google-Playstore.csv` file in the same directory as the `main.py` script.

3. **Execution**:
   - Run the `main.py` script using the command: 
     ```bash
     python main.py
     ```
   - Follow the on-screen prompts to see the results of the analysis.

## Conclusion

This project demonstrates how to effectively clean and analyze a large dataset using Pandas. The analysis provides insights into the popularity of app categories, factors affecting app ratings and installs, and the best age group to target for ad-supported apps. Visualization tools like Matplotlib and Seaborn are used to make the data-driven decisions more interpretable and actionable.
