from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA = PROJECT_ROOT / "data" / "raw" / "expression_samples.csv"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
FIGURE_DIR = PROJECT_ROOT / "results" / "figures"
SUMMARY_CSV = PROCESSED_DIR / "expression_summary.csv"
FIGURE_PNG = FIGURE_DIR / "expression_raw_points.png"


def load_raw_data() -> pd.DataFrame:
    return pd.read_csv(RAW_DATA)


def make_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("condition")["expression"]
        .agg(["count", "mean", "std", "min", "max"])
        .reset_index()
    )
    return summary


def save_raw_point_plot(df: pd.DataFrame) -> None:
    fig, ax = plt.subplots(figsize=(5, 4))
    positions = {"control": 0, "treated": 1}

    for condition, group in df.groupby("condition"):
        x = [positions[condition]] * len(group)
        ax.scatter(x, group["expression"], label=condition, s=70)

    ax.set_xticks(list(positions.values()), list(positions.keys()))
    ax.set_ylabel("expression")
    ax.set_title("Expression by condition")
    ax.legend(title="condition")
    fig.tight_layout()
    fig.savefig(FIGURE_PNG, dpi=150)
    plt.close(fig)


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)

    df = load_raw_data()
    summary = make_summary(df)
    summary.to_csv(SUMMARY_CSV, index=False)
    save_raw_point_plot(df)

    print(f"Input: {RAW_DATA}")
    print(f"Output: {SUMMARY_CSV}")
    print(f"Output: {FIGURE_PNG}")


if __name__ == "__main__":
    main()