import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import os

sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (8,5)

os.makedirs("visualizations", exist_ok=True)

df = pd.read_csv("sales_data.csv")
df.columns = df.columns.str.strip()

print("Columns in dataset:", df.columns)

col_category = df.columns[2]
col_region = df.columns[3]
col_sales = df.columns[-1]
col_date = df.columns[1]

df[col_date] = pd.to_datetime(df[col_date], errors='coerce')

print("\nCreating Box Plot...")
plt.figure()
sns.boxplot(x=col_category, y=col_sales, data=df)
plt.title("Box Plot - Sales Distribution by Category")
plt.savefig("visualizations/boxplot.png")
plt.close()

print("Creating Violin Plot...")
plt.figure()
sns.violinplot(x=col_region, y=col_sales, data=df)
plt.title("Violin Plot - Sales Distribution by Region")
plt.savefig("visualizations/violinplot.png")
plt.close()

print("Creating Heatmap...")
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Heatmap - Correlation Matrix")
plt.savefig("visualizations/heatmap.png")
plt.close()

print("Creating Line Plot...")
plt.figure()
sns.lineplot(x=col_date, y=col_sales, data=df)
plt.title("Line Plot - Sales Trend Over Time")
plt.savefig("visualizations/lineplot.png")
plt.close()

print("Creating Bar Plot...")
plt.figure()
sns.barplot(x=col_category, y=col_sales, data=df)
plt.title("Bar Plot - Average Sales by Category")
plt.savefig("visualizations/barplot.png")
plt.close()

print("Creating Dashboard (Subplots)...")
fig, axes = plt.subplots(2, 2, figsize=(12,10))

sns.boxplot(x=col_category, y=col_sales, data=df, ax=axes[0,0])
axes[0,0].set_title("Box Plot")

sns.violinplot(x=col_region, y=col_sales, data=df, ax=axes[0,1])
axes[0,1].set_title("Violin Plot")

sns.barplot(x=col_category, y=col_sales, data=df, ax=axes[1,0])
axes[1,0].set_title("Bar Plot")

sns.lineplot(x=col_date, y=col_sales, data=df, ax=axes[1,1])
axes[1,1].set_title("Line Plot")

plt.tight_layout()
plt.savefig("visualizations/dashboard.png")
plt.close()

print("Creating Interactive Chart...")
fig = px.line(df, x=col_date, y=col_sales, color=col_category,
              title="Interactive Sales Trend")
fig.write_html("visualizations/interactive.html")

print("\nAll graphs created successfully!")
print("Check 'visualizations' folder.")