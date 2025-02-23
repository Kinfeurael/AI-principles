# Credit Score Analysis

## Overview
This project analyzes credit risk using a dataset of 250,000 borrowers, focusing on predicting the likelihood of a borrower experiencing severe delinquency.

## Data
- **Training Set**: 150,000 entries, 12 features, includes the target variable (`SeriousDlqin2yrs`).
- **Test Set**: 101,503 entries, missing target variable.
- **Key Features**:
  - Demographics (Age, Number of Dependents)
  - Financial History (Monthly Income, Debt Ratio)
  - Loan & Credit Data (Number of Open Credit Lines, Delinquency History)

## Data Preprocessing
- **Missing Values**: Handled using median (Monthly Income) and mode (Number of Dependents).
- **Feature Scaling**: MinMax normalization applied to standardize ranges.
- **Exploratory Data Analysis (EDA)**:
  - Younger borrowers and lower-income groups show higher default risk.
  - Number of past delinquencies is a strong predictor of default.
  - Debt ratio and revolving utilization have skewed distributions.

## Model Training
- **Algorithms Used**:
  - Logistic Regression (Baseline)
  - Random Forest
  - Gradient Boosting (Best Performance)
- **Evaluation Metrics**:
  - Accuracy, ROC-AUC, Precision, Recall, F1-score
  - Gradient Boosting achieved highest ROC-AUC (0.87).

## Explainability & Fairness
- **SHAP Analysis**: Age, delinquency history, and income are key predictors.
- **Bias Considerations**:
  - Class imbalance handled with stratified splitting.
  - Potential bias in income data and delinquency history examined.

## Future Improvements
- Advanced feature engineering (interaction terms, outlier handling).
- Model calibration for fairness and transparency.
- Consider alternative models to improve interpretability.

## Usage
1. Load and preprocess the dataset.
2. Train and evaluate models using provided scripts.
3. Analyze feature importance and fairness metrics.

## Authors
- **Kinfeurael Wubishet - GSR/8436/17**
- **Yetemegn Telaye - GSR/8087/17**

