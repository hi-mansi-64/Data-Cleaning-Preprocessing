import pandas as pd

# 🧾 Load CSV file
df = pd.read_csv("people-100.csv")

print("📊 Original Data Overview")
print(df.shape)
print(df.info())
print(df.head(), "\n")

# 🧹 Drop 'Index' column
df.drop(columns=["Index"], inplace=True)
print("🧹 'Index' column dropped successfully.\n")

# ✏️ Rename columns
df.rename(columns={
    "User Id": "user_id",
    "First Name": "first_name",
    "Last Name": "last_name",
    "Sex": "gender",
    "Email": "email",
    "Phone": "phone",
    "Date of birth": "dob",
    "Job Title": "job_title"
}, inplace=True)

# 🔁 Deduplication
print("🧾 Duplicate rows before cleaning:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
print("✅ Duplicate rows after cleaning:", df.duplicated().sum(), "\n")

# 🔍 Missing values check
print("🔍 Missing values before cleaning:")
print(df.isnull().sum(), "\n")

# 🧩 Data Type Correction
df["dob"] = pd.to_datetime(df["dob"], errors="coerce")

# ✨ Format Standardization
df["first_name"] = df["first_name"].str.strip().str.title()
df["last_name"] = df["last_name"].str.strip().str.title()
df["gender"] = df["gender"].str.strip().str.capitalize()
df["job_title"] = df["job_title"].str.strip().str.title()
df["phone"] = df["phone"].str.replace(r"[^0-9]", "", regex=True)

# 🧠 Handle any missing values (Future-proof version)
if df["gender"].isnull().sum() > 0:
    df["gender"] = df["gender"].fillna(df["gender"].mode()[0])
if df["job_title"].isnull().sum() > 0:
    df["job_title"] = df["job_title"].fillna(df["job_title"].mode()[0])

# 💾 Save clean data
df.to_csv("cleaned_people_data.csv", index=False)

# ✅ Validation check
assert df.duplicated().sum() == 0
print("✅ Data cleaned and validated successfully!")
print("💾 Cleaned data saved as 'cleaned_people_data.csv'\n")

# 📈 Final Summary
print("📈 Final Dataset Summary:")
print(df.info())
print("\nTotal Rows:", len(df))
print("Columns:", list(df.columns))
print("\n✅ Cleaning completed successfully!")

# 📊 Optional Insight Section (for quick overview)
print("\n📊 Quick Insights:")
print("Gender distribution:\n", df["gender"].value_counts(), "\n")
print("Most common job title:", df["job_title"].mode()[0])
print("Date of Birth Range:", df["dob"].min().date(), "to", df["dob"].max().date())
