# 💳 Financial Inclusion in Africa

> Mapping the gap between financial account ownership and actual credit access across African economies — and asking why having a bank account doesn't always mean access to finance.

---

## Overview

Africa has made real progress on financial inclusion, largely driven by mobile money platforms like M-Pesa and MTN MoMo. But account ownership and genuine financial access aren't the same thing. Across much of the continent, people may hold a mobile wallet yet still have no path to formal credit, savings products, or insurance.

This project uses World Bank Global Findex data to compare financial account ownership, mobile money penetration, and formal borrowing rates across 12 African countries, benchmarked against India and Brazil.

---

## Objective

- Visualise the **financial inclusion gap** by country — who is banked and who isn't
- Compare **account ownership** against **formal borrowing rates** to surface the credit access gap
- Highlight the role of **mobile money** as an alternative inclusion pathway

---

## Tools

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| pandas | Data manipulation |
| matplotlib | Visualisation |

---

## Data Sources

**World Bank – Global Findex Database 2021**
- Account ownership, formal borrowing, mobile money usage
- Download: [databank.worldbank.org/source/global-financial-inclusion](https://databank.worldbank.org/source/global-financial-inclusion)
- Documentation: [worldbank.org/en/publication/globalfindex](https://www.worldbank.org/en/publication/globalfindex)

Data compiled directly in the script for reproducibility.

---

## How to Run

```bash
pip install pandas matplotlib
python analysis.py
```

Chart is saved to `outputs/financial_inclusion_analysis.png`.

---

## Key Findings

- **Rwanda leads the continent at 93%** account ownership — almost entirely mobile money-driven — showing what targeted policy and digital infrastructure can achieve
- **Niger and Mali** remain severely excluded, with fewer than 35% of adults holding any financial account
- Even in **Kenya (79% banked)**, only 11% borrowed formally — suggesting accounts are used for payments, not as gateways to credit
- Mobile money has been the dominant inclusion engine in East Africa, while West and Central African markets still lag on both measures

---

## Why This Matters for Development Finance

Financial inclusion sits at the heart of the **AfDB's financial sector strategy** and the work of institutions like **CGAP** and **IFC**. The Findex data used here is the same dataset that DFI analysts rely on when assessing market gaps, designing SME lending facilities, or making the investment case for digital financial infrastructure. The gap between account ownership and credit access is exactly the structural problem that development finance is meant to address.

---

## Output

![Financial Inclusion Chart](outputs/financial_inclusion_analysis.png)

---

*Part of a four-project portfolio analysing Africa's development challenges, aligned with the African Development Bank's Four Cardinal Points.*
