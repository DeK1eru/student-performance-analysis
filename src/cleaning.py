import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.drop_duplicates()

    numeric_cols = ["midterm", "final", "attendance"]
    for c in numeric_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")
        df[c] = df[c].fillna(df[c].mean())

    # Жалпы балл: midterm 40% + final 60%
    df["total"] = df["midterm"] * 0.4 + df["final"] * 0.6
    return df