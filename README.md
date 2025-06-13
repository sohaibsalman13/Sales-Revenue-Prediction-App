# Sales & Revenue Prediction App

This project is a complete machine learning pipeline built to predict **Total Revenue per Order**,**Total Order Revenue per Day** and **Late Delivery Indicator** using real-world sales data. It combines SQL-based data transformation, in-depth exploratory data analysis (EDA), supervised ML models using Python and a prediction app using Streamlit. 

**Fully Functioning App can be accessed here: https://revenue-app.streamlit.app/**

## Features

**Data**: The raw input dataset for the models is the real world supermarket data from Brazil (2016-2018).

**Integration**: Amazon S3 is used for raw data storage and connected with Amazon Redshift to store and query sales data efficiently.

**Data Cleaning & Transformation**: Used PostgreSQL queries for imputing missing values, generating new features, and cleaning raw data in Redshift. The code can be found in the folder `SQL scripts`.
  
**Exploratory Data Analysis (EDA)**:
  - Univariate and bivariate analysis
  - Cramér's V for categorical relationships
  - KDE plots, scatter plots, heatmaps
    
**Feature Engineering**:
  - Scaled numerical features and one-hot encoded categoricals using `scikit-learn`
    
**Model Training & Evaluation**:
  - Regression: Trained `XGBoostRegressor` and `RandomForestRegressor` for predicting `Total Revenue per Order`
  - Classification: Used `RandomForestClassifier` to predict `Late Delivery Indicator`
  - Regression: Used `RandomForestRegressor` for predicting `Total Revenue per Day`
  - Evaluated models with metrics such as MSE, R², ROC AUC, and confusion matrix

**Web App**: Integrated the models with a web application using StreamLit where business users can input order features and obtain real-time predictions for revenue and late delivery likelihood. The screenshot of the app are added below.
![Screenshot 2025-06-12 at 12 13 53 AM](https://github.com/user-attachments/assets/dc93cfac-922e-4d63-8a39-95e25b57b95b)
![Screenshot 2025-06-12 at 12 14 22 AM](https://github.com/user-attachments/assets/9dd9f63a-eece-40c8-a915-b2172cc951b9)


##  Tech Stack

- **Languages**: Python, SQL
- **Libraries**: Pandas, NumPy, Seaborn, Scikit-learn, XGBoost, Matplotlib, StreamLit
- **Cloud**: AWS Redshift, S3, Boto3
- **Tools**: Jupyter Notebook, Git



