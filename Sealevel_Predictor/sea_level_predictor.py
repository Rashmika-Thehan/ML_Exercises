import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 8))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.7, s=30)

    # Create first line of best fit
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    years_extended = list(range(df['Year'].min(), 2051))
    sea_levels_predicted = [slope1 * year + intercept1 for year in years_extended]
    plt.plot(years_extended, sea_levels_predicted, 'r', label='Line of Best Fit (All Data)')
    
    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    years_recent = list(range(2000, 2051))
    sea_levels_recent = [slope2 * year + intercept2 for year in years_recent]
    plt.plot(years_recent, sea_levels_recent, 'g', label='Line of Best Fit (2000 onwards)')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    
    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()