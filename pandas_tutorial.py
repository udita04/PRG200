import pandas as pd
df = pd.DataFrame(
    {
        "Name":[
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth",
        ],
        "Age": [22, 25, 58],
        "Sex": ["Male", "Male", "Female"],
    }
)
print(df["Age"])

ages = pd.Series([22, 35, 58], name="Age")
print(df["Age"])

print(df["Age"].max())

print(df.describe())