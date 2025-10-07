import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


df_sales = pd.read_csv("data/sales data-set.csv")
df_feat = pd.read_csv("data/Features data set.csv")
df_stores = pd.read_csv("data/stores data-set.csv")
pd.set_option("display.float_format", "{:,.2f}".format)

# print(df_sales.head(10))
# print(df_feat.head(10))
# print(df_stores.head(10))

# print(df_sales.info())
# print(df_feat.info())
# print(df_stores.info())


df_sales_copy = df_sales.copy()
df_feat_copy = df_feat.copy()
df_stores_copy = df_stores.copy()

df_sale_store = df_stores_copy.merge(df_sales_copy, on="Store")
df_sale_tot = df_sale_store.merge(df_feat_copy, on=["Store", "Date"])


# total sales per year
df_sale_tot["Date"] = pd.to_datetime(df_sale_tot["Date"], dayfirst=True)
df_sale_tot["Year"] = df_sale_tot["Date"].dt.year

total_sales_per_year = df_sale_tot.groupby("Year")["Weekly_Sales"].sum()
# print(total_sales_per_year)

# Average sales per store
avg_sales_per_store = df_sale_tot.groupby("Store")["Weekly_Sales"].mean()
# print(avg_sales_per_store.head(15))

# Total sales per department
total_sales_by_dept = df_sale_tot.groupby("Dept")["Weekly_Sales"].sum()
# print(total_sales_by_dept.head(15))
# keep the one from sales, drop the other
df_sale_tot = df_sale_tot.drop(columns=["IsHoliday_y"])
df_sale_tot = df_sale_tot.rename(columns={"IsHoliday_x": "IsHoliday"})


# pivot_dept = pd.pivot_table(
#     df_sale_tot, values="Weekly_Sales", index="Dept", aggfunc="sum"
# )
# print(pivot_dept.sort_values("Weekly_Sales", ascending=False).head(15))

# pivot_holiday = pd.pivot_table(
#     df_sale_tot, values="Weekly_Sales", index="IsHoliday", aggfunc="mean"
# )
# print(pivot_holiday)


# pivot_store_type = pd.pivot_table(
#     df_sale_tot, values="Weekly_Sales", index="Type", aggfunc="mean"
# )
# print(pivot_store_type)

# # Get top 10 departments
# dept_sales = (
#     df_sale_tot.groupby("Dept")["Weekly_Sales"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(10)
# )

# plt.figure(figsize=(10, 6))
# dept_sales.plot(kind="bar")
# plt.title("Top 10 Departments by Total Sales")
# plt.ylabel("Total Sales")
# plt.xlabel("Department")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# holiday_sales = df_sale_tot.groupby("IsHoliday")["Weekly_Sales"].mean()

# plt.figure(figsize=(6, 5))
# holiday_sales.plot(kind="bar", color=["skyblue", "orange"])
# plt.title("Average Weekly Sales: Holiday vs Non-Holiday")
# plt.ylabel("Average Sales")
# plt.xticks([0, 1], ["Non-Holiday", "Holiday"], rotation=0)
# plt.tight_layout()
# plt.show()

# store_type_sales = (
#     df_sale_tot.groupby("Type")["Weekly_Sales"].mean().sort_values(ascending=False)
# )

# plt.figure(figsize=(6, 5))
# store_type_sales.plot(kind="bar", color="green")
# plt.title("Average Weekly Sales by Store Type")
# plt.ylabel("Average Sales")
# plt.xlabel("Store Type")
# plt.xticks(rotation=0)
# plt.tight_layout()
# plt.show()

# weekly_sales = df_sale_tot.groupby("Date")["Weekly_Sales"].sum()

# plt.figure(figsize=(12, 6))
# weekly_sales.plot()
# plt.title("Total Weekly Sales Over Time")
# plt.ylabel("Total Sales")
# plt.xlabel("Date")
# plt.tight_layout()
# plt.show()


# # ensure datetime + Year/Month columns exist
# df_sale_tot["Date"] = pd.to_datetime(df_sale_tot["Date"], dayfirst=True)
# df_sale_tot["Year"] = df_sale_tot["Date"].dt.year
# df_sale_tot["Month"] = df_sale_tot["Date"].dt.to_period("M").astype(str)

# # Weekly total sales (sorted index)
# weekly = df_sale_tot.groupby("Date")["Weekly_Sales"].sum().sort_index()

# # Simple moving average (4-week)
# weekly_ma4 = weekly.rolling(window=4, min_periods=1).mean()

# plt.figure(figsize=(12, 5))
# weekly.plot()
# weekly_ma4.plot()
# plt.title("Total Weekly Sales + 4-week Moving Average")
# plt.xlabel("Week")
# plt.ylabel("Sales")
# plt.tight_layout()
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e6:.1f}"))
# plt.ylabel("Sales (millions)")
# plt.show()

# # Mark holiday weeks on the weekly series (True if ANY store-week is holiday)
# holiday_flag_by_week = (
#     df_sale_tot.groupby("Date")["IsHoliday"].max().reindex(weekly.index).fillna(False)
# )
# plt.figure(figsize=(12, 5))
# weekly.plot()
# plt.scatter(weekly.index[holiday_flag_by_week], weekly[holiday_flag_by_week])
# plt.title("Total Weekly Sales with Holiday Weeks Highlighted")
# plt.xlabel("Week")
# plt.ylabel("Sales")
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e6:.1f}"))
# plt.ylabel("Sales (millions)")
# plt.tight_layout()
# plt.show()

# # Monthly totals
# monthly = df_sale_tot.groupby(pd.Grouper(key="Date", freq="MS"))["Weekly_Sales"].sum()
# plt.figure(figsize=(12, 5))
# monthly.plot()
# plt.title("Total Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x/1e6:.1f}"))
# plt.ylabel("Sales (millions)")
# plt.tight_layout()
# plt.show()


# # --- Stores: average weekly sales per store (rank) ---
# store_avg = (
#     df_sale_tot.groupby("Store")["Weekly_Sales"].mean().sort_values(ascending=False)
# )

# print("Top 10 stores by avg weekly sales:")
# print(store_avg.head(10))

# plt.figure(figsize=(8, 5))
# store_avg.head(10).plot(kind="bar")
# plt.title("Top 10 Stores by Avg Weekly Sales")
# plt.ylabel("Avg Weekly Sales")
# plt.xlabel("Store")
# plt.tight_layout()
# plt.show()

# # Size relationship (per store)
# per_store = df_sale_tot.groupby("Store").agg(
#     AvgWeeklySales=("Weekly_Sales", "mean"),
#     Size=("Size", "first"),
#     Type=("Type", "first"),
# )

# print(
#     "Correlation (AvgWeeklySales vs Size):",
#     per_store["AvgWeeklySales"].corr(per_store["Size"]),
# )

# plt.figure(figsize=(6, 5))
# plt.scatter(per_store["Size"], per_store["AvgWeeklySales"])
# plt.title("Store Size vs Avg Weekly Sales (per store)")
# plt.xlabel("Size")
# plt.ylabel("Avg Weekly Sales")
# plt.tight_layout()
# plt.show()

# # --- Departments: total sales (rank) ---
# dept_total = (
#     df_sale_tot.groupby("Dept")["Weekly_Sales"].sum().sort_values(ascending=False)
# )

# print("Top 10 departments by total sales:")
# print(dept_total.head(10))

# plt.figure(figsize=(8, 5))
# dept_total.head(10).plot(kind="bar")
# plt.title("Top 10 Departments by Total Sales")
# plt.ylabel("Total Sales")
# plt.xlabel("Department")
# plt.tight_layout()
# plt.show()

# # Bottom 10 departments
# print("Bottom 10 departments by total sales:")
# print(dept_total.tail(10))

# columns that hold markdown dollars
md_cols = ["MarkDown1", "MarkDown2", "MarkDown3", "MarkDown4", "MarkDown5"]
md_cols = [c for c in md_cols if c in df_sale_tot.columns]  # keep only those that exist

# treat missing markdowns as 0 and sum them
df_sale_tot[md_cols] = df_sale_tot[md_cols].fillna(0)
df_sale_tot["MarkdownTotal"] = df_sale_tot[md_cols].sum(axis=1)

# quick sanity check (optional)
# print(df_sale_tot["MarkdownTotal"].describe())
# print(df_sale_tot[md_cols + ["MarkdownTotal"]].head(3))

# sales_by_md = df_sale_tot.groupby(df_sale_tot["MarkdownTotal"] > 0)[
#     "Weekly_Sales"
# ].mean()
# # print(sales_by_md)

# sales_by_store_md = (
#     df_sale_tot.groupby(["Store", df_sale_tot["MarkdownTotal"] > 0])["Weekly_Sales"]
#     .mean()
#     .unstack()
# )
# print(sales_by_store_md.head(10))

# markdown_events = df_sale_tot[df_sale_tot["MarkdownTotal"] > 0][
#     ["Store", "Dept", "Date", "MarkdownTotal", "Weekly_Sales"]
# ]
# print(markdown_events.head(20))

df_sale_tot["HasMarkdown"] = df_sale_tot["MarkdownTotal"] > 0

# markdown_stats = (
#     df_sale_tot.groupby("Store")["HasMarkdown"]
#     .agg(["sum", "count"])  # sum = number of True, count = total rows
#     .rename(columns={"sum": "WeeksWithMarkdown", "count": "TotalWeeks"})
# )
# markdown_stats["PctWeeksMarkdown"] = (
#     markdown_stats["WeeksWithMarkdown"] / markdown_stats["TotalWeeks"] * 100
# )

# print(markdown_stats.head(10))


# median_pct = markdown_stats["PctWeeksMarkdown"].median()

# # label stores
# markdown_stats["Group"] = markdown_stats["PctWeeksMarkdown"].apply(
#     lambda x: "High-markdown" if x > median_pct else "Low-markdown"
# )

# # merge group info back into main df
# df_sale_tot = df_sale_tot.merge(
#     markdown_stats["Group"], left_on="Store", right_index=True
# )

# # compare average sales
# group_sales = df_sale_tot.groupby("Group")["Weekly_Sales"].mean()
# print(group_sales)


summary = df_sale_tot.groupby("Store").agg(
    WeeksWithMarkdown=("HasMarkdown", "sum"), TotalWeeks=("HasMarkdown", "count")
)
summary["PctWeeksMarkdown"] = 100 * summary["WeeksWithMarkdown"] / summary["TotalWeeks"]

# Merge size and type info into the summary
summary = summary.merge(df_stores[["Store", "Size", "Type"]], on="Store", how="left")
print(summary.head(10))


# import matplotlib.pyplot as plt

# plt.figure(figsize=(8, 5))
# plt.scatter(summary["Size"], summary["PctWeeksMarkdown"])
# plt.xlabel("Store Size (sq ft)")
# plt.ylabel("% Weeks with Markdown")
# plt.title("Markdown Usage vs Store Size")
# plt.show()


# corr = summary["Size"].corr(summary["PctWeeksMarkdown"])
# print("Correlation between store size and markdown frequency:", corr)
n = int(input())

for i in range(n):
    print(i + 1)
