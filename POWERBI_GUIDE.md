# 📊 Power BI Dashboard Setup Guide

## Step 1: Generate the CSVs
Run the EDA notebook fully — it exports these files to `/powerbi_exports/`:
- `franchise_season_stats.csv`
- `phase_runs_by_team.csv`
- `toss_win_by_season.csv`
- `venue_avg_scores.csv`
- `batsmen_efficiency.csv`
- `bowlers_efficiency.csv`

---

## Step 2: Open Power BI Desktop
Download free from: https://powerbi.microsoft.com/desktop/

---

## Step 3: Load Data
1. Home → Get Data → Text/CSV
2. Load all 6 CSVs above
3. Name them clearly: `FranchiseStats`, `PhaseRuns`, `TossData`, `VenueData`, `Batsmen`, `Bowlers`

---

## Step 4: Build This Dashboard (1 Page, 6 Visuals)

### Layout Plan:
```
┌─────────────────────────────────────────────────┐
│   TITLE: IPL Business Analytics Dashboard       │
│   Slicer: Season | Slicer: Team                 │
├──────────────┬──────────────┬───────────────────┤
│  KPI Card    │  KPI Card    │   KPI Card        │
│  Total Wins  │  Avg Win%    │  Toss Edge        │
├──────────────┴──────────────┴───────────────────┤
│  Line Chart: Win % Trend by Franchise (Season)  │
├────────────────────┬────────────────────────────┤
│  Bar: Phase Runs   │  Bar: Venue Avg Scores     │
├────────────────────┴────────────────────────────┤
│  Scatter: Batting Efficiency Matrix             │
└─────────────────────────────────────────────────┘
```

### Visual Recommendations:
| Visual | Type | Fields |
|--------|------|--------|
| Win % Trend | Line Chart | season (X), win_pct (Y), team (Legend) |
| All-Time Wins | Bar Chart | team (Axis), wins (Value) |
| Phase Runs | Clustered Bar | batting_team (Axis), total_runs (Value), phase (Legend) |
| Venue Scores | Bar Chart | venue (Axis), avg_score (Value) |
| Toss Trend | Line Chart | season (X), win_pct (Y) |
| Player Matrix | Scatter | avg_per_innings (X), strike_rate (Y), total_runs (Size) |

---

## Step 5: Styling Tips (Dark Theme)
1. View → Themes → Import Theme → paste this JSON:

```json
{
  "name": "IPL Dark",
  "dataColors": ["#58a6ff", "#3fb950", "#f85149", "#f0883e", "#a371f7", "#79c0ff"],
  "background": "#0d1117",
  "foreground": "#c9d1d9",
  "tableAccent": "#1f6feb"
}
```

2. Canvas Settings → Canvas background → #0d1117
3. All card backgrounds → #161b22
4. Font: Segoe UI, white

---

## Step 6: Export
1. File → Export → Export to PDF (for GitHub README image)
2. File → Publish → Power BI Service (free account — makes it shareable via link)
3. Screenshot the dashboard and save as `assets/powerbi_preview.png`

---

## Step 7: Embed in README
Add this to your README:
```markdown
## 📊 Power BI Dashboard
[🔗 View Live Dashboard](your-powerbi-link)
![Dashboard Preview](assets/powerbi_preview.png)
```
