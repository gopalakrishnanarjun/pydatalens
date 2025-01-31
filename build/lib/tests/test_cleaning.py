import pandas as pd
from pydatalens import cleaning

def test_handle_missing():
    data = {"A": [1, None, 3]}
    df = pd.DataFrame(data)
    cleaned_df = cleaning.handle_missing(df, strategy="mean")
    assert cleaned_df.isnull().sum().sum() == 0
    print("Handle missing test passed.")

def test_drop_duplicates():
    data = {"A": [1, 1, 2]}
    df = pd.DataFrame(data)
    cleaned_df = cleaning.drop_duplicates(df)
    assert cleaned_df.shape[0] == 2
    print("Drop duplicates test passed.")
