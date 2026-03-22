# 🏎️ Car Price Predictor (V2.0)

This project provides a complete solution for scraping, analyzing, and predicting used car prices in the Czech Republic using data from sauto.cz. It features a robust data pipeline and a high-performance Gradient Boosting model.

## 📊 Performance (V2.0)
* **R2 Score:** 0.7984 (Honest result with 79.84% accuracy)
* **MAE:** 109,083 CZK CZK (Mean Absolute Error)
* Dataset Size: 27,000+ unique car listings.


🛠 Tech Stack
Language: Python
Data Collection: requests, re (Regex), json
Storage: SQLite3 (Relational database for raw data)
Processing: Pandas, NumPy
Visualization: Matplotlib, Seaborn (Correlation matrices, distribution plots, outlier detection)
Machine Learning: CatBoost (Gradient Boosting on Decision Trees), Scikit-Learn

⚙️ How It Works
1. Data Acquisition (The Scraper)
   Automated script that bypasses basic blocks using custom headers and random delays.
   Collects data for 20+ top car brands (Skoda, VW, BMW, etc.).
   Uses INSERT OR IGNORE logic in SQLite to prevent duplicate entries across multiple runs.

2. Data Cleaning & Engineering
Outlier Removal: Filtered extreme price points (under 30k and over 5M CZK).
Smart Imputation: Missing engine power values were recovered using a multi-level median approach (by Brand + Trim -> by Brand -> Global Median).
Feature Extraction: Used Regex to mine "hidden" features from raw text descriptions: is_4x4, is_automatic, is_sport (RS/AMG/M-packet), has_led.
Clustering: Implemented K-Means to segment cars into 5 price/quality categories based on mileage, power, and age.


3. Machine Learning Pipeline
Pre-processing: Applied log1p transformation to the target variable (price) to handle the right-skewed distribution of car prices.
Training: Used CatBoostRegressor, leveraging its native support for categorical features (brand, fuel, gearbox).
Feature Importance: The model automatically identified that Car Age and Engine Power are the primary price drivers in the Czech market.


📈 Key Insights
Negative Correlation: Car Age and Mileage show a strong -0.74 correlation, confirming data consistency.
Power Impact: Each additional kW significantly increases the resale value, especially in the premium segment (>150kW).
Market Segments: The most liquid part of the market sits between 110kW and 150kW (standard VAG engines).

🚀 Installation & Usage
Clone the repo: git clone https://github.com/kuzetshy/autoProject.git
Install dependencies: pip install -r requirements.txt
Train & Analyze: Open 02_car_price_predict.ipynb in Jupyter or VS Code.
   

📩 Contact
Developed by [Abilkhaiyr Albet/kuzetshy] — Data Science Enthusiast & Python Developer.
Feel free to reach out if you have questions or suggestions!
