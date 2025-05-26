# Sales & Revenue Prediction Model

This project is a complete machine learning pipeline built to predict **Total Price per Order** and classify **Late Delivery Indicator** using real-world sales data. It combines SQL-based data transformation, in-depth exploratory data analysis (EDA), and supervised ML models using Python.

## Features

-  **Data Integration**: Connected Amazon S3 with Amazon Redshift to store and query sales data efficiently.
-  **Data Cleaning & Transformation**: Used complex SQL queries for imputing missing values, generating new features, and cleaning raw data. The code can be found in the folder `SQL scripts`.
  
  **Exploratory Data Analysis (EDA)**:
  - Univariate and bivariate analysis
  - Cramér's V for categorical relationships
  - KDE plots, scatter plots, heatmaps
    
  **Feature Engineering**:
  - Generated features like `freight_ratio`, `avg_price_per_item`, `order_duration_days`
  - Scaled numerical features and one-hot encoded categoricals using `scikit-learn`
    
  **Model Training & Evaluation**:
  - Regression: Trained `XGBoostRegressor` and `RandomForestRegressor` for predicting `Total Price per Order`
  - Classification: Used `RandomForestClassifier` to predict `Late Delivery Indicator`
  - Evaluated models with metrics such as MSE, R², ROC AUC, and confusion matrix


##  Tech Stack

- **Languages**: Python, SQL
- **Libraries**: Pandas, NumPy, Seaborn, Scikit-learn, XGBoost, Matplotlib
- **Cloud**: AWS Redshift, S3, Boto3
- **Tools**: Jupyter Notebook, Git

## Sample Results

- **XGBoost Regression**: R² = 0.98, MSE = 1019.4  
- **Random Forest Classifier**: Accuracy = 91%, ROC AUC = 0.94


