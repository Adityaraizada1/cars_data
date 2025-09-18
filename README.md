# Automobile Dataset Analysis 🚗📊
This project explores and analyzes the Automobile Dataset to uncover insights about fuel efficiency (MPG), engine performance, and other car characteristics.
The workflow covers data cleaning, preprocessing, and exploratory data analysis (EDA) with meaningful visualizations.
# 📂 Dataset
Source: Automobile Dataset
Format: CSV (Automobile.csv)
Rows: 398
Columns: 9 (including mpg, cylinders, displacement, horsepower, weight, acceleration, model_year, origin, name)
# ⚙️ Data Preprocessing
✅ Removed duplicates (no duplicates found).
✅ Checked for missing values (none found).
✅ Outlier treatment applied (IQR method).
✅ Normalization & scaling applied.
✅ Encoded categorical variables (name, origin).
🔎 Exploratory Data Analysis
1. Correlation Heatmap
A correlation matrix was plotted to understand relationships between features.
However, since categorical features like name were encoded, they dominated the heatmap.
Key takeaway: Numerical features such as horsepower, weight, and displacement show stronger correlations with MPG.
2. MPG by Origin (USA vs Others)
Cars made in the USA tend to have lower MPG compared to non-USA cars.
Non-USA cars show higher fuel efficiency on average.
# 📊 Boxplot Insight: The spread of MPG is wider for USA cars, while foreign cars are generally more fuel-efficient.
3. Horsepower vs MPG
Clear negative correlation:
Higher horsepower cars → lower MPG.
Lower horsepower cars → higher MPG.
This aligns with the tradeoff between power and efficiency.
4. Distribution of MPG
The MPG distribution is slightly right-skewed.
Most cars fall in the average range, with fewer high-efficiency cars.
A few cars with very high MPG stand out as outliers.
# 📊 Visualizations
Correlation Heatmap of Features
Boxplot: MPG by Car Origin (USA vs Others)
Scatter Plot: Horsepower vs MPG
Histogram: Distribution of MPG
# 🚀 Tech Stack
Python 3.13
Libraries:
pandas, numpy → Data handling
matplotlib, seaborn → Visualization
scikit-learn → Preprocessing
# 💡 Key Insights
Fuel efficiency is strongly influenced by horsepower and weight.
American cars from this dataset are generally less fuel-efficient compared to foreign cars.
Cars with smaller engines and lower horsepower tend to be more efficient.
#📌 Next Steps
Build a regression model to predict MPG.
Feature engineering (e.g., engine size per weight).
Compare trends across different model_year values.<img width="1611" height="966" alt="Screenshot 2025-09-16 at 7 38 45 PM" src="https://github.com/user-attachments/assets/d6d6a80a-8a1d-4058-9e8f-1c3ab683ab11" />
<img width="1312" height="976" alt="Screenshot 2025-09-16 at 7 38 24 PM" src="https://github.com/user-attachments/assets/30014913-d9a9-4c39-8a48-0f4a0b738800" />
<img width="1112" height="776" alt="Screenshot 2025-09-16 at 7 38 20 PM" src="https://github.com/user-attachments/assets/98e8e5c6-a34a-4202-a4a4-f6f552990ea6" />
<img width="1112" height="776" alt="Screenshot 2025-09-16 at 7 38 14 PM" src="https://github.com/user-attachments/assets/db969642-a598-4eeb-96dc-457640bbfe20" />
<img width="1112" height="776" alt="Screenshot 2025-09-16 at 7 38 08 PM" src="https://github.com/user-attachments/assets/4fc6a1d4-22c7-4e53-ad4d-3ea0cf4cfffa" />

#✨ This project gives a solid foundation for understanding car efficiency and sets the stage for predictive modeling.
