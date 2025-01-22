import pandas as pd
from pydatalens import eda, cleaning, visualizations

# Example dataset
data = {"ColumnA": [1, None, 3, 4], "ColumnB": [10, 20, 30, 40]}
df = pd.DataFrame(data)

# Summarize
print(eda.summarize(df))

# Clean
df = cleaning.handle_missing(df, strategy="mean")
df = cleaning.drop_duplicates(df)

# Visualize
visualizations.plot_histogram(df, "ColumnA")
visualizations.correlation_heatmap(df)
