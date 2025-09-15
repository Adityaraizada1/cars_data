import kagglehub
import os
import zipfile
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------
# Step 1: Download dataset
# -------------------------
download_path = kagglehub.dataset_download("tawfikelmetwally/automobile-dataset")
print("✅ Dataset downloaded to:", download_path)

# Step 2: List files
files = os.listdir(download_path)
print("📂 Files in dataset folder:", files)

# Step 3: Extract ZIP if present
for file in files:
    if file.endswith(".zip"):
        zip_path = os.path.join(download_path, file)
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(download_path)
        print("✅ Extracted ZIP:", file)
        files = os.listdir(download_path)

# Step 4: Find CSV
csv_files = [f for f in files if f.endswith(".csv")]
if not csv_files:
    raise FileNotFoundError("❌ No CSV file found!")

csv_path = os.path.join(download_path, csv_files[0])
print("✅ Using CSV file:", csv_path)

# Step 5: Load dataset
df = pd.read_csv(csv_path)
print("✅ First 5 records:")
print(df.head())

# -------------------------
# Step 6: Data Cleaning
# -------------------------
print("\n🔹 Shape before removing duplicates:", df.shape)
df = df.drop_duplicates()
print("🔹 Shape after removing duplicates:", df.shape)

print("\n🔹 Missing values per column:")
print(df.isnull().sum())

# Fill missing numerical values with median
for col in df.select_dtypes(include=[np.number]).columns:
    df[col] = df[col].fillna(df[col].median())

print("✅ Missing values treated")

# -------------------------
# Step 7: Outlier Treatment (IQR)
# -------------------------
def treat_outliers(col):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = np.where(df[col] < lower, lower, df[col])
    df[col] = np.where(df[col] > upper, upper, df[col])

for col in df.select_dtypes(include=[np.number]).columns:
    treat_outliers(col)

print("✅ Outliers treated (IQR method)")

# -------------------------
# Step 8: Normalization & Scaling
# -------------------------
scaler = StandardScaler()
num_cols = df.select_dtypes(include=[np.number]).columns
df[num_cols] = scaler.fit_transform(df[num_cols])
print("✅ Normalization & scaling applied")

# -------------------------
# Step 9: Encode Categorical Variables
# -------------------------
df = pd.get_dummies(df, drop_first=True)
print("✅ Categorical variables encoded")
print("🔹 Shape after encoding:", df.shape)

# -------------------------
# Step 10: Univariate Analysis
# -------------------------
print("\n📊 Univariate Analysis")
plt.figure(figsize=(10, 6))
sns.histplot(df["mpg"], bins=30, kde=True)
plt.title("Distribution of MPG (Miles per Gallon)")
plt.xlabel("MPG")
plt.ylabel("Count")
plt.show()

# -------------------------
# Step 11: Bivariate Analysis
# -------------------------
print("\n📊 Bivariate Analysis")
plt.figure(figsize=(10, 6))
sns.scatterplot(x="horsepower", y="mpg", data=df)
plt.title("Horsepower vs MPG")
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x="origin_usa", y="mpg", data=df)  # example categorical encoding
plt.title("MPG by Origin (USA vs Others)")
plt.xlabel("Origin (USA=1, Others=0)")
plt.ylabel("MPG")
plt.show()

# -------------------------
# Step 12: Correlation Heatmap
# -------------------------
print("\n📊 Correlation Heatmap")
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), cmap="coolwarm", annot=False)
plt.title("Correlation Heatmap of Features")
plt.show()
