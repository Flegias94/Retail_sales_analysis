# Retail Sales EDA (Sales + Features + Stores)

Exploratory analysis of a retail dataset by merging **sales**, **features**, and **stores** tables.  
Focus: KPIs, holiday effects, markdown usage, store size relationships, and time trends.

## Datasets
Place CSVs in `data/`:
- `sales data-set.csv` — columns: Store, Dept, Date, Weekly_Sales, IsHoliday
- `Features data set.csv` — Store, Date, CPI, Fuel_Price, Temperature, Unemployment, MarkDown1..5, IsHoliday
- `stores data-set.csv` — Store, Type, Size

> Dates are parsed day-first (DD/MM/YYYY).

## What’s included
- Merge on `Store` and `Store+Date`; date parsing and `Year` feature
- KPIs: total sales per year, avg weekly sales per store, total sales by department
- Weekly sales with 4-week moving average
- Holiday vs non-holiday comparison
- Store type comparison (if `Type` exists)
- Markdown analysis: `MarkdownTotal`, `HasMarkdown`, `%WeeksMarkdown` per store
- Relationships:
  - Size vs Avg Weekly Sales (correlation and scatter)
  - Avg Weekly Sales vs % Weeks with Markdown (dependence on markdowns)
- Auto-saving of charts to `charts/` and tables to `outputs/`

## Tech stack
Python, pandas, matplotlib, Jupyter.

## Repository structure
```
analysis.ipynb # main notebook
data/
sales data-set.csv
Features data set.csv
stores data-set.csv
charts/ # saved figures (created on run)
outputs/ # saved tables (created on run)
requirements.txt
```


## Quickstart
```bash
git clone https://github.com/Flegias94/retail-sales-eda.git
cd retail-sales-eda
pip install -r requirements.txt
# Open the notebook on GitHub or run locally:
jupyter notebook analysis.ipynb
```
### Notebook guide
```
1. Load and merge datasets; create Year, markdown features
2. KPIs: per year, per store, per department
3. Weekly trend + MA(4)
4. Holiday vs non-holiday average sales
5. By store Type (if present)
6. Size ↔ Avg Weekly Sales; %WeeksMarkdown per store
7. Avg Weekly Sales ↔ %WeeksMarkdown scatter (insight on weaker stores)
8. Save charts to charts/ and tables to outputs/
```
## Requirements
```
pandas
matplotlib
jupyter
```

## Insights

- Correlation between sales and store size
- Holiday uplift: Holiday weeks generate higher average sales than non-holiday weeks
- Markdown effect: Weeks with markdowns show a sales lift vs weeks without markdowns
