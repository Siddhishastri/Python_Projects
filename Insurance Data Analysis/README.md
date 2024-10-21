# Insurance EDA & Medical Cost Prediction Project

## Project Overview

This project focuses on exploratory data analysis (EDA) and predictive modeling for a healthcare insurance dataset. The dataset contains information about policyholders and their medical costs. The goal of the project is to analyze how various factors—such as age, BMI, smoking status, and region—affect medical insurance costs and to build a model that can predict the insurance premium based on these factors.

## Domain
+ Industry: Healthcare and Insurance
+ Problem Type: Regression
+ Goal: To create a model that predicts the medical insurance premium cost based on various features such as age, BMI, number of children, smoking habits, and region.

## Problem Statement

ABC Insurance, an insurance agency, has a large dataset containing information about their policyholders and claims. They want to analyze the factors that influence the cost of medical insurance premiums. For example, a smoker's insurance premium is usually higher than a non-smoker's due to the increased risk of chronic diseases. The agency is looking for insights from this dataset to help make better business decisions and predict healthcare premiums for future policyholders based on input features.

## Objective
The objective of this project is to analyze the insurance dataset and create a predictive model to estimate the cost of medical insurance based on several factors including:

+ Age
+ BMI
+ Number of children
+ Smoking status
+ Region

By doing so, we aim to uncover trends and patterns in the dataset and predict insurance costs more accurately.

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
+ Scatter Plot: Created scatter plots to examine relationships between variables, specifically:
+ BMI vs Charges: Observed that BMI has a normal distribution and a moderate positive correlation with charges.
+ Pairplot: Used sns.pairplot() to visualize the pairwise relationships between numerical variables, with smoker as the hue to highlight differences between smokers and non-smokers.
5. Visualizing Distribution by Sex and Region
+ Pie Chart by Region: Created a pie chart to visualize the distribution of policyholders by region.
+ Pie Chart by Smoking Status: Created another pie chart to understand the proportion of smokers and non-smokers in the dataset.
6. Correlation Analysis
Calculated the correlation matrix to identify the relationships between different variables, especially between charges and other variables like age, BMI, and smoker.
7. Model Creation (Optional)
Trained a regression model (e.g., Linear Regression) to predict charges based on the input features.

## Results
+ Age and charges have the strongest relationship, followed by BMI and charges.
+ Smokers are charged significantly more than non-smokers due to their higher health risks.
+ The Northwest and Southeast regions have more policyholders than other regions.
+ Policyholders with higher BMI tend to have higher insurance premiums.
+ The number of children covered by the policy has a smaller impact on the premium compared to other variables.
