def save_report(avg_subj, avg_group, low_df, top_df, out_path: str):
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("STUDENT PERFORMANCE REPORT\n\n")

        f.write("1) Average by subject:\n")
        f.write(avg_subj.to_string(index=False))
        f.write("\n\n")

        f.write("2) Average by group:\n")
        f.write(avg_group.to_string(index=False))
        f.write("\n\n")

        f.write("3) Low performers:\n")
        f.write(low_df.to_string(index=False))
        f.write("\n\n")

        f.write("4) Top students:\n")
        f.write(top_df.to_string(index=False))
        f.write("\n")