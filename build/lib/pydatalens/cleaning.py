def handle_missing(df, strategy="mean"):
    """
    Fills missing values in the DataFrame.
    Args:
        strategy: mean, median, or mode.
    """
    print(f"Handling missing values using {strategy} strategy...")
    for column in df.select_dtypes(include=["float", "int"]).columns:
        if strategy == "mean":
            df[column] = df[column].fillna(df[column].mean())
        elif strategy == "median":
            df[column] = df[column].fillna(df[column].median())
        elif strategy == "mode":
            df[column] = df[column].fillna(df[column].mode()[0])
    return df

def drop_duplicates(df):
    """
    Drops duplicate rows.
    """
    print("Dropping duplicate rows...")
    return df.drop_duplicates()
