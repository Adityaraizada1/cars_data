import kagglehub
import os
import zipfile
import pandas as pd

# Step 1: Download dataset
download_path = kagglehub.dataset_download("tawfikelmetwally/automobile-dataset")
print("✅ Dataset downloaded to:", download_path)

# Step 2: List files in the dataset folder
files = os.listdir(download_path)
print("📂 Files in dataset folder:", files)

# Step 3: If there's a ZIP file, extract it
for file in files:
    if file.endswith(".zip"):
        zip_path = os.path.join(download_path, file)
        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(download_path)
        print("✅ Extracted ZIP:", file)
        files = os.listdir(download_path)  # refresh file list
        print("📂 Files after extraction:", files)

# Step 4: Find the CSV file automatically
csv_files = [f for f in files if f.endswith(".csv")]
if not csv_files:
    raise FileNotFoundError("❌ No CSV file found in the dataset folder!")

csv_path = os.path.join(download_path, csv_files[0])
print("✅ Using CSV file:", csv_path)

# Step 5: Load dataset into pandas
df = pd.read_csv(csv_path)
print("✅ First 5 records:")
print(df.head())
