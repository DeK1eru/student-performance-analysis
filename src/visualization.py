import matplotlib.pyplot as plt
import pandas as pd

def plot_grade_distribution(df: pd.DataFrame, out_path: str):
    plt.figure()
    plt.hist(df["total"], bins=10)
    plt.title("Total score distribution")
    plt.xlabel("Total")
    plt.ylabel("Count")
    plt.savefig(out_path)
    plt.close()

def plot_avg_by_subject(df_avg: pd.DataFrame, out_path: str):
    plt.figure()
    plt.bar(df_avg["subject"], df_avg["avg_total"])
    plt.title("Average total by subject")
    plt.xlabel("Subject")
    plt.ylabel("Avg total")
    plt.savefig(out_path)
    plt.close()

def plot_avg_by_group(df_avg: pd.DataFrame, out_path: str):
    plt.figure()
    plt.bar(df_avg["group"], df_avg["avg_total"])
    plt.title("Average total by group")
    plt.xlabel("Group")
    plt.ylabel("Avg total")
    plt.savefig(out_path)
    plt.close()