from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


project_root = Path(__file__).resolve().parents[1]
output_dir = project_root / "04_Data_Analysis"
summary_path = output_dir / "day10_expression_summary.csv"
plot_path = output_dir / "day10_expression_raw_points.png"


df = pd.DataFrame(
    {
        "sample": ["S1", "S2", "S3", "S4", "S5", "S6"],
        "condition": ["control", "control", "control", "treated", "treated", "treated"],
        "expression": [5.0, 5.4, 5.2, 7.2, 8.1, 8.1],
    }
)

summary = df.groupby("condition")["expression"].agg(["count", "mean", "std", "min", "max"])
summary.to_csv(summary_path)

print("Day 10 - expression summary")
print()
print("Original DataFrame")
print(df)
print()
print("Summary by condition")
print(summary)
print()

mean_difference = summary.loc["treated", "mean"] - summary.loc["control", "mean"]
print("Interpretation")
print(f"treated mean - control mean = {mean_difference:.1f}")
print(
    "In this example dataset, the treated group has a higher observed mean "
    "expression than the control group."
)
print(
    "Because each group has only 3 samples, this result should not be "
    "generalized without more data and additional statistical analysis."
)
print()

plt.figure(figsize=(6, 4))
for condition, group_df in df.groupby("condition"):
    plt.scatter(
        [condition] * len(group_df),
        group_df["expression"],
        label=condition,
        s=80,
        alpha=0.85,
    )

plt.xlabel("Condition")
plt.ylabel("Expression")
plt.title("Expression by Condition")
plt.legend(title="Condition")
plt.tight_layout()
plt.savefig(plot_path, dpi=150)
plt.close()

print("Saved summary:")
print(summary_path)
print("Saved plot:")
print(plot_path)
