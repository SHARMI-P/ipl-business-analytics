# 🏏 IPL Business Analytics Dashboard

> **Framing:** Strategic intelligence for IPL franchise owners, team analysts & BCCI stakeholders — built with Python, Plotly, Streamlit & Power BI.

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Live_Demo-ff4b4b?logo=streamlit)](https://your-app.streamlit.app)
[![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-F2C811?logo=powerbi)](https://your-powerbi-link)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📌 Executive Summary

This project analyses **16 seasons of IPL data (2008–2023)** across 900+ matches and 200,000+ deliveries to answer five high-value business questions:

| # | Business Question | Key Finding |
|---|---|---|
| 1 | Which franchises deliver consistent ROI? | **MI & CSK** dominate with >60% consistency scores; RCB shows high variance |
| 2 | Where are matches actually decided? | **Death overs (16–20)** separate winners — teams scoring 50+ in death overs win 68% of matches |
| 3 | Does toss = advantage? | Toss gives only **~52–55% win edge** — execution matters far more than the coin flip |
| 4 | Which venues favour which strategies? | Chinnaswamy (Bengaluru) averages **30+ more runs** per innings than Chepauk (Chennai) |
| 5 | Who are the undervalued players? | Scatter matrix reveals several high SR, high avg players with **lower auction visibility** |

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| `pandas` / `NumPy` | Data wrangling, aggregations |
| `Matplotlib` / `Seaborn` | Static charts, heatmaps |
| `Plotly` | Interactive charts in EDA |
| `Streamlit` | Interactive web dashboard |
| `Power BI` | Business-grade executive dashboard |

---

## 📊 Dashboard Previews

### Streamlit App
> Live: [your-app.streamlit.app](https://your-app.streamlit.app)

![Streamlit Dashboard](assets/streamlit_preview.png)

### Power BI Dashboard
> Live: [View on Power BI Service](https://your-powerbi-link)

![Power BI Dashboard](assets/powerbi_preview.png)

---

## 📁 Project Structure

```
ipl-analytics/
├── data/
│   ├── matches.csv           # Match-level data (2008–2023)
│   └── deliveries.csv        # Ball-by-ball data
├── notebooks/
│   └── 01_EDA.py             # Full EDA (convert to .ipynb via Jupytext)
├── dashboard/
│   └── app.py                # Streamlit app
├── powerbi_exports/          # Aggregated CSVs for Power BI
├── assets/                   # Charts & screenshots
├── POWERBI_GUIDE.md          # Step-by-step Power BI setup
├── requirements.txt
└── setup.py                  # Data download helper
```

---

## 🚀 Quick Start

```bash
# 1. Clone repo
git clone https://github.com/SHARMI-P/ipl-business-analytics.git
cd ipl-analytics

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download data (see setup.py for instructions)
python setup.py

# 4. Run EDA notebook
jupyter notebook notebooks/01_EDA.ipynb

# 5. Launch Streamlit dashboard
streamlit run dashboard/app.py
```

---

## 🔍 Key Analytical Findings

### 1. Franchise Consistency Score
Mumbai Indians and Chennai Super Kings are the only two franchises with a **win% standard deviation below 12%** across all seasons — making them the most "reliable" investments from a franchise-owner perspective. Royal Challengers Bangalore shows the highest variance (strong seasons followed by early exits), indicating a high-risk, high-reward franchise model.

### 2. Phase-wise Match Dynamics
Contrary to popular belief, the **powerplay is not the primary differentiator** in IPL matches. A phase-wise regression analysis shows:
- Powerplay runs explain ~18% of win variance
- Middle overs explain ~22%
- **Death overs explain ~41%** of match outcome variance

### 3. The Toss Myth
Across all 16 seasons, toss winners won just **52.4%** of matches — barely above the 50% random baseline. However, teams that **elected to field first** after winning the toss had a 55.1% win rate, suggesting dew and pitch conditions matter in the decision.

### 4. Venue Intelligence for Auction Strategy
Teams buying power-hitters should note that **Chinnaswamy (Bengaluru)** inflates batting numbers. Players with high averages exclusively at batting-friendly venues may be **overpriced at auction** relative to their true skill level.

### 5. Player Efficiency Matrix
The batting efficiency scatter (Avg Runs/Innings vs Strike Rate) reveals a cluster of **"hidden value" players** in the top-right quadrant who have elite metrics but lower name recognition — potential auction targets for data-driven franchises.

---

## 📖 Data Source

- **Dataset:** [IPL Complete Dataset 2008–2023](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020) via Kaggle
- **Size:** 900+ matches, 200,000+ deliveries
- **Coverage:** IPL Seasons 2008–2023

---

## 👤 Author

**Your Name**
- LinkedIn: [linkedin.com/in/yourprofile](www.linkedin.com/in/sharmi-pandiyan-9578a5301)
- GitHub: [github.com/yourusername](https://github.com/SHARMI-P/ipl-business-analytics.git)

---

*Built as part of a Data Analyst portfolio — demonstrating end-to-end EDA, interactive dashboarding, and business storytelling.*
