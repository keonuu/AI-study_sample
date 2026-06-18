from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def check_qc(rate):
    if rate >= 0.9:
        return "excellent"
    elif rate >= 0.8:
        return "pass"
    else:
        return "fail"


project_root = Path(__file__).resolve().parents[1]
data_path = project_root / "04_Data_Analysis" / "day07_sample_qc.csv"
plot_path = project_root / "04_Data_Analysis" / "day07_mapping_rate_barplot.png"

df = pd.read_csv(data_path)

print("Day 7 - pandas, numpy, and matplotlib")
print()

print("Original DataFrame")
print(df)
print()

print("Column selection: mapping_rate")
print(df["mapping_rate"])
print()

print("Summary statistics")
print("mean:", df["mapping_rate"].mean())
print("max:", df["mapping_rate"].max())
print("min:", df["mapping_rate"].min())
print("std:", np.std(df["mapping_rate"]))
print()

passed = df[df["mapping_rate"] >= 0.8]
failed = df[df["mapping_rate"] < 0.8]

print("Passed samples")
print(passed[["sample_id", "mapping_rate"]])
print()

print("Failed samples")
print(failed[["sample_id", "mapping_rate"]])
print()

df["qc_result"] = df["mapping_rate"].apply(check_qc)

print("DataFrame with QC result")
print(df)
print()

plt.figure(figsize=(7, 4))
plt.bar(df["sample_id"], df["mapping_rate"], color="#4C78A8")
plt.axhline(0.8, color="#E45756", linestyle="--", label="QC threshold")
plt.ylim(0, 1)
plt.xlabel("Sample ID")
plt.ylabel("Mapping rate")
plt.title("Day 7 sample mapping rates")
plt.legend()
plt.tight_layout()
plt.savefig(plot_path)
plt.close()

print("Saved plot:")
print(plot_path)
