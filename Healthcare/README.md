# 🏥 Cardiovascular Disease Prediction and Analysis
This project analyzes cardiovascular health data to identify factors contributing to heart attacks and builds a predictive model to assess the likelihood of cardiovascular disease (CVD). It includes data preprocessing, exploratory data analysis (EDA), statistical modeling, and visualization through an interactive dashboard.

## 📝 Project Summary
Cardiovascular diseases are among the leading causes of death globally. To address this issue, this project focuses on analyzing a dataset containing 14 attributes and over 4,000 records to derive meaningful insights and create a predictive model. Here's what was accomplished:

1. Data Preprocessing:
* Performed initial data inspection to identify missing values and duplicates.
* Cleaned the dataset by handling missing values appropriately and removing duplicates to ensure data quality.

2. Exploratory Data Analysis (EDA):
* Explored the distribution of cardiovascular disease (CVD) occurrences across different age groups and genders.
* Analyzed key factors, such as cholesterol levels, resting blood pressure, and heart rate, to understand their relationship with CVD risk.
* Investigated how chest pain types and thalassemia impact heart health.
* Visualized data using count plots, pair plots, and correlation matrices to uncover patterns and relationships.

3. Statistical Modeling:
* Built a Logistic Regression model to predict the likelihood of cardiovascular disease.
* Evaluated model performance using metrics like accuracy, precision, recall, and a confusion matrix.

4. Visualization:
* Developed an interactive Tableau dashboard to compare attributes of healthy vs. diseased individuals.
* Highlighted key relationships and visualized trends to aid in understanding the critical factors influencing CVD risk.

## 📂 Dataset Overview
Attributes:
* age: Age in years.
* sex: Gender (1 = male, 0 = female).
* cp: Type of chest pain (categorical).
* trestbps: Resting blood pressure (mm Hg).
* chol: Serum cholesterol (mg/dl).
* fbs: Fasting blood sugar (>120 mg/dl; 1 = true, 0 = false).
* restecg: Resting electrocardiographic results.
* thalach: Maximum heart rate achieved.
* exang: Exercise-induced angina (1 = yes, 0 = no).
* oldpeak: ST depression induced by exercise relative to rest.
* slope: Slope of the peak exercise ST segment.
* ca: Number of major vessels (0-3) colored by fluoroscopy.
* thal: 3 = normal, 6 = fixed defect, 7 = reversible defect.
* target: 1 = Heart disease present, 0 = No heart disease.

## 🛠️ Tools & Techniques Used
* Data Cleaning & Analysis: Python (pandas, numpy, seaborn, matplotlib).
* Modeling: Logistic Regression with scikit-learn.
* Performance Evaluation: Confusion matrix, accuracy, precision, recall.
* Visualization: Tableau for dashboards and storytelling.
* Statistical Methods: Central tendencies, spread analysis, pair plots, and correlation analysis.

## 🔮 Key Insights
1. Age and Gender:
* Higher CVD risk was observed in older individuals.
* Males were more likely to experience CVD than females.
2. Cholesterol and Blood Pressure:
* Elevated cholesterol levels and higher resting blood pressure significantly correlated with increased CVD risk.
3. Thalassemia and Heart Rate:
* Abnormal thalassemia results and lower maximum heart rates were strong indicators of heart disease.
4. Chest Pain Types:
* Certain chest pain types were closely associated with higher probabilities of heart attacks.

## 📊 Visualization Summary
An interactive Tableau dashboard was created to:
* Compare healthy individuals with those at risk of heart disease.
* Highlight key attributes like cholesterol, resting blood pressure, and thalassemia.
* Provide actionable insights into the factors affecting cardiovascular health.
