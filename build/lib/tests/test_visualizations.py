import pandas as pd
from pydatalens import visualizations

def test_plot_histogram():
    data = {"A": [1, 2, 3, 4, 5]}
    df = pd.DataFrame(data)
    visualizations.plot_histogram(df, column="A")
    print("Histogram test passed.")

def test_correlation_heatmap():
    data = {"A": [1, 2, 3], "B": [4, 5, 6]}
    df = pd.DataFrame(data)
    visualizations.correlation_heatmap(df)
    print("Correlation heatmap test passed.")
