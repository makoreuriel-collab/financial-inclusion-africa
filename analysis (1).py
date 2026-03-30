# ============================================================
# Project: Financial Inclusion in Africa
# Data:    World Bank Global Findex Database 2021
# Charts:  1. Banked vs unbanked population by country
#          2. Account ownership vs formal borrowing scatter
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

# ── DATA ────────────────────────────────────────────────────
# Source: World Bank Global Findex 2021
# account           — % adults with bank or mobile money account
# formal_borrowing  — % adults who borrowed from a formal institution (past year)
# mobile_money      — % adults with a mobile money account

data = {
    "Country": [
        "Kenya", "South Africa", "Ghana", "Nigeria", "Rwanda",
        "Tanzania", "Senegal", "Côte d'Ivoire", "Ethiopia", "Mozambique",
        "Mali", "Niger",
        "India", "Brazil"                               # benchmarks
    ],
    "Subregion": [
        "East Africa", "Southern Africa", "West Africa", "West Africa", "East Africa",
        "East Africa", "West Africa", "West Africa", "East Africa", "Southern Africa",
        "West Africa", "West Africa",
        "Benchmark", "Benchmark"
    ],
    "Account_pct": [
        79.0, 85.0, 58.0, 45.0, 93.0,
        72.0, 56.0, 41.0, 46.0, 42.0,
        35.0, 22.0,
        78.0, 84.0
    ],
    "Formal_Borrowing_pct": [
        11.0, 13.0, 9.5, 3.8, 12.0,
        5.5,  5.0,  4.2, 4.0, 3.5,
        3.0,  2.5,
        11.5, 17.0
    ],
    "Mobile_Money_pct": [
        72.0, 14.0, 44.0, 34.0, 89.0,
        65.0, 36.0, 30.0, 38.0, 28.0,
        24.0, 16.0,
        35.0, 20.0
    ]
}

df = pd.DataFrame(data)
df["Unbanked_pct"] = 100 - df["Account_pct"]

africa     = df[df["Subregion"] != "Benchmark"].copy()
benchmarks = df[df["Subregion"] == "Benchmark"].copy()

# Sort for chart 1
africa_sorted = africa.sort_values("Account_pct", ascending=True)

# ── CHART 1: Stacked bar — banked vs unbanked ────────────────
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle("Financial Inclusion in Africa", fontsize=14, fontweight="bold")

ax1 = axes[0]
ax1.barh(africa_sorted["Country"], africa_sorted["Account_pct"],
         color="#1a6e5c", label="Has Account", edgecolor="white")
ax1.barh(africa_sorted["Country"], africa_sorted["Unbanked_pct"],
         left=africa_sorted["Account_pct"], color="#dddddd", label="No Account", edgecolor="white")

# Benchmark reference lines
ax1.axvline(78, color="#4455aa", linestyle="--", linewidth=1.1, label="India (78%)")
ax1.axvline(84, color="#aa4455", linestyle=":",  linewidth=1.1, label="Brazil (84%)")

# Label the banked share on each bar
for i, (_, row) in enumerate(africa_sorted.iterrows()):
    ax1.text(row["Account_pct"] - 3, i, f"{row['Account_pct']:.0f}%",
             va="center", ha="right", fontsize=7, color="white", fontweight="bold")

ax1.set_xlabel("% of Adults (15+)")
ax1.set_title("Financial Account Ownership\n(Bank or Mobile Money)", fontweight="bold")
ax1.set_xlim(0, 110)
ax1.legend(fontsize=8, loc="lower right")
ax1.spines[["top", "right"]].set_visible(False)

# ── CHART 2: Account ownership vs formal borrowing ──────────
ax2 = axes[1]

# Colour points by subregion
region_colors = {
    "East Africa":     "#1a6e5c",
    "West Africa":     "#e8a838",
    "Southern Africa": "#4455aa"
}

for _, row in africa.iterrows():
    color = region_colors.get(row["Subregion"], "#888888")
    ax2.scatter(row["Account_pct"], row["Formal_Borrowing_pct"],
                color=color, s=80, zorder=3)
    ax2.annotate(row["Country"], (row["Account_pct"], row["Formal_Borrowing_pct"]),
                 textcoords="offset points", xytext=(5, 3), fontsize=7, color=color)

for _, row in benchmarks.iterrows():
    ax2.scatter(row["Account_pct"], row["Formal_Borrowing_pct"],
                color="#aaaaaa", s=80, marker="D", zorder=3)
    ax2.annotate(row["Country"], (row["Account_pct"], row["Formal_Borrowing_pct"]),
                 textcoords="offset points", xytext=(5, 3), fontsize=7, color="#888888")

ax2.set_xlabel("Account Ownership (%)")
ax2.set_ylabel("Formal Borrowing (%)")
ax2.set_title("Account Ownership vs.\nFormal Credit Access", fontweight="bold")
ax2.spines[["top", "right"]].set_visible(False)

# Legend for subregions
patches = [mpatches.Patch(color=c, label=r) for r, c in region_colors.items()]
patches.append(mpatches.Patch(color="#aaaaaa", label="Benchmarks"))
ax2.legend(handles=patches, fontsize=8)

plt.tight_layout()

# ── SAVE ────────────────────────────────────────────────────
os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/financial_inclusion_analysis.png", dpi=150, bbox_inches="tight")
print("Saved: outputs/financial_inclusion_analysis.png")
plt.show()

# ── SUMMARY ─────────────────────────────────────────────────
print("\n── Key Numbers ─────────────────────────────────────")
print(f"Avg account ownership (Africa):   {africa['Account_pct'].mean():.1f}%")
print(f"Avg formal borrowing  (Africa):   {africa['Formal_Borrowing_pct'].mean():.1f}%")
print(f"Avg mobile money      (Africa):   {africa['Mobile_Money_pct'].mean():.1f}%")
unbanked = africa[africa["Account_pct"] < 40][["Country", "Account_pct"]]
print(f"\nCountries below 40% account ownership:\n{unbanked.to_string(index=False)}")
