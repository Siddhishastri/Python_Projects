# Insurance Data Analysis

## Project Overview

This project focuses on exploratory data analysis (EDA) for a healthcare insurance dataset. The dataset contains information about policyholders and their medical costs. The goal of the project is to analyze how various factors—such as age, BMI, smoking status, and region—affect medical insurance costs.

## Problem Statement

ABC Insurance, an insurance agency, has a large dataset containing information about their policyholders and claims. They want to analyze the factors that influence the cost of medical insurance premiums. For example, a smoker's insurance premium is usually higher than a non-smoker's due to the increased risk of chronic diseases. The agency is looking for insights from this dataset to help make better business decisions.

## Objective
The objective of this project is to analyze the insurance dataset based on several factors including:

+ Age
+ BMI
+ Number of children
+ Smoking status
+ Region

By doing so, we aim to uncover trends and patterns in the dataset.

## Dataset
The dataset contains the following columns:

* Age: Age of the policyholder.
* Sex: Gender of the policyholder.
* BMI: Body Mass Index, a measure of body fat based on height and weight.
* Children: Number of children covered by the insurance.
* Smoker: Whether the policyholder is a smoker or not (yes or no).
* Region: The region where the policyholder resides (northwest, southwest, northeast, southeast).
* Charges: Medical insurance premium billed by the insurance company.

## Project Steps
1. Data Cleaning
+ Checked for missing values.
+ Removed or imputed missing data (if any).
+ Ensured that all data types were appropriate (e.g., charges as numeric, region as categorical).
2. Data Preprocessing
+ Encoded categorical variables like sex, smoker, and region.
+ Scaled the numerical features (if necessary) to ensure consistency for model building.
+ Split the data into training and testing sets for model evaluation.
3. Data Manipulation
+ Performed feature selection and feature engineering to understand the most impactful variables.
+ Analyzed and transformed variables for better model performance.
4. Exploratory Data Analysis (EDA)
+ Histograms: Plotted histograms for age, charges, BMI, and children to visualize the distribution of key variables.
![histogram](https://github.com/user-attachments/assets/162f0fde-16c8-4f75-b0b2-87af9b96a3f0)
+ Scatter Plot: Created scatter plots to examine relationships between variables, specifically:
+ BMI vs Charges: Observed that BMI has a normal distribution and a moderate positive correlation with charges.
![scatterplot](https://github.com/user-attachments/assets/d320ef44-3f3d-4189-950b-1aeb52dab905)
+ Pairplot: Used sns.pairplot() to visualize the pairwise relationships between numerical variables, with smoker as the hue to highlight differences between smokers and non-smokers.
![pairplot](https://github.com/user-attachments/assets/fc4cd36d-8782-4553-8463-d0ee430f7149)
5. Visualizing Distribution by Sex and Region
+ Pie Chart by Region: Created a pie chart to visualize the distribution of policyholders by region.
![piechart1](https://github.com/user-attachments/assets/7c58d79b-2f94-4f8b-ab4b-8045fc3490c8)
+ Pie Chart by Smoking Status: Created another pie chart to understand the proportion of smokers and non-smokers in the dataset.
![piechart2](https://github.com/user-attachments/assets/8a1449f4-694f-497d-98ce-073cf586db75)
6. Correlation Analysis
Calculated the correlation matrix to identify the relationships between different variables, especially between charges and other variables like age, BMI, and smoker.
## Results
+ Age and charges have the strongest relationship, followed by BMI and charges.
+ Smokers are charged significantly more than non-smokers due to their higher health risks.
+ The Northwest and Southeast regions have more policyholders than other regions.
+ Policyholders with higher BMI tend to have higher insurance premiums.
+ The number of children covered by the policy has a smaller impact on the premium compared to other variables.
