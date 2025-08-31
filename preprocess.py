import os
import pandas as pd

# Path to your dataset
TRAIN_DIR = "dataset/TRAIN"
TEST_DIR = "dataset/TEST"

# Collect image paths and labels
data = []
for folder in ["TRAIN", "TEST"]:
    folder_path = os.path.join("dataset", folder)
    for label in os.listdir(folder_path):
        label_path = os.path.join(folder_path, label)
        if os.path.isdir(label_path):
            for file in os.listdir(label_path):
                if file.lower().endswith(('.jpg', '.png', '.jpeg')):
                    data.append({
                        "folder": folder,
                        "label": label,
                        "file_name": file,
                        "file_path": os.path.join(label_path, file)
                    })

# Create DataFrame
df = pd.DataFrame(data)

# Show first few rows
print(df.head())

# Equivalent to .info()
print("\nDataset Info:")
print(df.info())

# Equivalent to .describe()
print("\nDataset Description:")
print(df.describe(include="all"))

# Equivalent to .isnull().sum()
print("\nMissing Values:")
print(df.isnull().sum())

# Distribution of classes
print("\nClass Distribution (per folder):")
print(df.groupby(["folder", "label"]).size())