# 🏎️ Used Car Price Predictor (V2.0)

This project uses Machine Learning to predict the market value of used cars in the Czech Republic based on data scraped from sauto.cz.

## 📊 Performance (V2.0)
* **R2 Score:** 0.8098 (Honest result with 81% accuracy)
* **MAE:** 106,000 CZK (Mean Absolute Error)

## 🛠️ Key Features
* **Smart Power Imputation:** Instead of using mean values, the model calculates the median engine power for each specific car brand to fill missing data.
* **Feature Engineering:** * Extracted technical specs (4x4, Automatic Gearbox, LED lights, Sport trim) from raw text descriptions.
    * Calculated `car_age` based on the manufacturing year.
* **Unsupervised Learning:** Applied **K-Means Clustering** to segment cars into 5 price/spec categories for better model understanding.
* **Log-Transformation:** Used `np.log1p` on the price target to stabilize variance and improve predictions for premium vehicles.

## 🧪 Tech Stack
* **Python:** Pandas, NumPy, Scikit-learn.
* **Model:** CatBoostRegressor (Gradient Boosting on Decision Trees).
* **Data:** SQLite3 (Scraping) -> CSV (Cleaned).

## 🚀 How to use
1. Load `car_price_model_FINAL.cbm` using CatBoost.
2. Input car features (Brand, Year, Mileage, etc.).
3. Get a fair market price in CZK.
