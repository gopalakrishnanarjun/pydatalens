
# pydatalens Usage Guide

pydatalens is a Python package designed to simplify exploratory data analysis (EDA), data cleaning, and visualization. This guide provides examples of how to use the package effectively.

## Installation

Ensure you have the required dependencies installed. You can install pydatalens using the following steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/gopalakrishnanarjun/pydatalens.git
   cd pydatalens
   ```

2. Install the package:

   ```bash
   pip install -e .
   ```

## Getting Started

### Importing the Package

```python
from pydatalens import eda, cleaning, visualizations
```

### Loading Data

You can load your dataset using Pandas:

```python
import pandas as pd

# Load your dataset
df = pd.read_csv("data.csv")
```

## Features

### 1. Summarizing Data

Get an overview of your dataset using the `summarize` function.

```python
summary = eda.summarize(df)
print(summary)
```

### 2. Correlation Analysis

Calculate and display a correlation matrix.

```python
correlation_matrix = eda.correlation(df)
print(correlation_matrix)
```

### 3. Handling Missing Values

Handle missing values in the dataset using `mean`, `median`, or `mode` strategies.

```python
df_cleaned = cleaning.handle_missing(df, strategy="mean")
```

### 4. Dropping Duplicates

Remove duplicate rows from the dataset.

```python
df_unique = cleaning.drop_duplicates(df)
```

### 5. Visualizations

#### Histogram

Generate a histogram for a specific column.

```python
visualizations.plot_histogram(df, column="age")
```

#### Correlation Heatmap

Generate a heatmap to visualize correlations.

```python
visualizations.correlation_heatmap(df)
```

## Advanced Features

### Generating an EDA Report

Future versions will include a feature to generate an HTML or PDF EDA report.

## Example Usage

Here’s a complete example of using pydatalens:

```python
import pandas as pd
from pydatalens import eda, cleaning, visualizations

# Load your dataset
data = {"ColumnA": [1, None, 3, 4], "ColumnB": [10, 20, 30, 40]}
df = pd.DataFrame(data)

# Summarize the dataset
summary = eda.summarize(df)
print(summary)

# Handle missing values
df_cleaned = cleaning.handle_missing(df, strategy="mean")

# Drop duplicates
df_unique = cleaning.drop_duplicates(df_cleaned)

# Visualize data
visualizations.plot_histogram(df_unique, "ColumnA")
visualizations.correlation_heatmap(df_unique)
```

## Support

If you encounter any issues, feel free to open an issue on GitHub or contact the package maintainer.

---

Happy analyzing with pydatalens!
