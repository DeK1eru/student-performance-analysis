import pandas as pd

def avg_by_subject(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("subject")["total"].mean().reset_index(name="avg_total")

def avg_by_group(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("group")["total"].mean().reset_index(name="avg_total")

def low_performers(df: pd.DataFrame, threshold: float = 50) -> pd.DataFrame:
    return df[df["total"] < threshold].sort_values("total")

def top_students(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    return df.sort_values("total", ascending=False).head(n)