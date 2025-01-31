import pandas as pd

def summarize(df):
    """
    Summarizes the given DataFrame.
    """
    print("Generating data summary...")
    summary = {
        "Columns": df.columns.tolist(),
        "Data Types": df.dtypes.tolist(),
        "Missing Values": df.isnull().sum().tolist(),
        "Unique Values": df.nunique().tolist(),
    }
    return pd.DataFrame(summary)

def correlation(df):
    """
    Generates a correlation matrix.
    """
    print("Calculating correlation matrix...")
    return df.corr()
