import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col='date', parse_dates=True)

# Clean data
low = df["value"].quantile(0.025)
high = df["value"].quantile(0.975)
df = df[(df["value"]>=low) & (df["value"]<=high)]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.strftime('%B')  # Use %B for full month names
    monthly_avg = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()
    monthly_avg_pivot = monthly_avg.pivot(index='year', columns='month', values='value')
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    monthly_avg_pivot = monthly_avg_pivot.reindex(columns=month_order)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    monthly_avg_pivot.plot(kind='bar', ax=ax, width=0.8)
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]  # Use %b for abbreviated month names
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')
    ax1.set_ylim(0, 200000)
    ax1.set_yticks(range(0, 220000, 20000))
    
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']  # Abbreviated month names
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2, order=month_order)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')
    ax2.set_ylim(0, 200000)
    ax2.set_yticks(range(0, 220000, 20000))
    
    fig.savefig('box_plot.png')
    plt.tight_layout()
    return fig
