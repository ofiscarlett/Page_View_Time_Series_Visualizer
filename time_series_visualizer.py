import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
#Use Pandas to import the data from "fcc-forum-pageviews.csv". Set the index to the date column.
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
#Clean the data by filtering out days when the page views 
# were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

#Create a draw_line_plot function that uses Matplotlib to draw a line chart 
# similar to "examples/Figure_1.png". The title should be Daily 
# freeCodeCamp Forum Page Views 5/2016-12/2019. The label on the x axis should be Date and the label on the y axis should be Page Views.
def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
# Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.strftime('%B')  # Full month name
    
    # Calculate the mean for each year and month
    df_bar = df_bar.groupby(['year', 'month']).mean().reset_index()
    
    # Create a list of all months in order to ensure correct display in the plot
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                    'July', 'August', 'September', 'October', 'November', 'December']
    
    # Draw the bar plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='year', y='value', hue='month', data=df_bar, hue_order=months_order, ax=ax)
    
    # Setting labels and title
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_title('Monthly Average Page Views for Each Year')
    
    # Adjust legend
    ax.legend(title='Months', loc='upper left', bbox_to_anchor=(1, 1))

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    #df_box['year'] = [d.year for d in df_box.date]
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')

    #order by monthly
    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=month_order, ordered=True)
    fig, axes = plt.subplots(1, 2, figsize=(20, 10))

    # Draw box plots (using Seaborn)
    # Draw bar plot 繪製箱線圖
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    #save month order
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')  # 設置標題
    axes[1].set_xlabel('Month')  # x軸標籤
    axes[1].set_ylabel('Page Views')  # y軸標籤

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
