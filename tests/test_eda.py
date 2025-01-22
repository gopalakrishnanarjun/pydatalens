import pandas as pd
from pydatalens import eda

def test_summarize():
    data = {"A": [1, 2, None], "B": [4, None, 6]}
    df = pd.DataFrame(data)
    summary = eda.summarize(df)
    assert "Columns" in summary.columns
    print("Summarize test passed.")

def test_correlation():
    data = {"A": [1, 2, 3], "B": [4, 5, 6]}
    df = pd.DataFrame(data)
    corr = eda.correlation(df)
    assert corr.shape[0] == corr.shape[1]
    print("Correlation test passed.")
