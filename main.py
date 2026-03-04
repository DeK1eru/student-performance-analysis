from src.data_loader import load_csv
from src.cleaning import clean_data
from src.analysis import avg_by_subject, avg_by_group, low_performers, top_students
from src.visualization import plot_grade_distribution, plot_avg_by_subject, plot_avg_by_group
from src.report import save_report

def main():
    df = load_csv("data/students.csv")
    df = clean_data(df)

    avg_subj = avg_by_subject(df)
    avg_grp = avg_by_group(df)
    low_df = low_performers(df, threshold=50)
    top_df = top_students(df, n=5)

    plot_grade_distribution(df, "outputs/total_distribution.png")
    plot_avg_by_subject(avg_subj, "outputs/avg_by_subject.png")
    plot_avg_by_group(avg_grp, "outputs/avg_by_group.png")

    save_report(avg_subj, avg_grp, low_df, top_df, "outputs/report.txt")
    print("Done! Check outputs/ folder.")

if __name__ == "__main__":
    main()