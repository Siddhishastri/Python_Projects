# Exploratory Data Analysis on Retail Sales Data

## Project Overview
The goal of this project is to perform Exploratory Data Analysis (EDA) on retail sales data to uncover patterns, trends, and insights that can help the retail business make informed decisions. In addition, a Linear Regression model is built to predict future sales based on the insights derived from the dataset.
Steps Involved in the Project
## Data Loading and Cleaning
+ Objective: Load the dataset into the environment and perform necessary data cleaning.
+ Actions:
  + Read the dataset using pandas and inspect its structure (columns, data types, etc.).
  + Handle missing or inconsistent data (e.g., missing values, outliers).
  + Remove any duplicates and check for any anomalies in the data.

## Data Preprocessing
+ Objective: Prepare the dataset for analysis and modeling.
+ Actions:
  + Convert the Date column to datetime format for better handling of time-series data.
  + Create new columns such as Year, Month, and Day to analyze sales trends over time.

## Exploratory Data Analysis (EDA)

1. Which Gender Spends More Money?
+ Objective: Analyze which gender contributes the most to the overall sales revenue.
+ Actions:
  + Create visualizations to compare total spending between male and female customers.
Calculate and compare the total spending by gender.

2. Which Product Has the Most Sales?
Objective: Identify the best-selling products and analyze the overall product performance.
+ Actions:
  + Count the number of units sold per product category.
Visualize the most popular product categories.

## Data Modeling
1. Train a Linear Regression Model
+ Objective: Use Linear Regression to predict future sales based on features such as Gender, Product_Category, and Month.
+ Actions:
  + Select relevant features and target variables (Amount as target).
  + Split the dataset into training and test sets.
  + Train a Linear Regression model using the training data.
2. Prediction on the Test Set
+ Objective: Evaluate the model's performance on the test set.
+ Actions:
  + Predict sales values for the test set and calculate the Mean Squared Error (MSE) to evaluate performance.

## Key Insights and Conclusions
1. Gender Spending Analysis: After analyzing the sales data by gender, it was observed that [Gender with the highest spending] spends more money overall. This insight can be used to target marketing strategies.

2. Top-Selling Products: The product categories that saw the highest number of orders are [Product Category Names]. Focusing on these categories can increase overall sales.

3. Sales Predictions: The Linear Regression model helps predict future sales based on factors like gender, product category, and month. The model’s MSE score indicates its accuracy, which can be improved by further tuning or using more advanced algorithms.

## Technologies and Tools Used
+ Python: Core language used for data manipulation and analysis.
+ Pandas: For data cleaning and preprocessing.
+ Seaborn & Matplotlib: For data visualization.
+ Scikit-learn: For building and evaluating the Linear Regression model.
