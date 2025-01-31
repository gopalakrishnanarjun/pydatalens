import seaborn as sns
import matplotlib.pyplot as plt

def plot_histogram(df, column):
    """
    Plots a histogram for a column.
    """
    print(f"Generating histogram for {column}...")
    sns.histplot(df[column], kde=True)
    plt.title(f"Histogram of {column}")
    plt.show()

def correlation_heatmap(df):
    """
    Plots a heatmap of the correlation matrix.
    """
    print("Generating correlation heatmap...")
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()
