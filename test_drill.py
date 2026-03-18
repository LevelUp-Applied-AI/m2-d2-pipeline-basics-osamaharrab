import pandas as pd
import numpy as np
from drill_functions import clean_column, compute_revenue


def test_clean_column():
    series = pd.Series([10, np.nan, 30])
    cleaned = clean_column(series)

    assert cleaned.isna().sum() == 0
    assert cleaned.iloc[1] == 20


def test_compute_revenue():
    quantity = pd.Series([2, 3, 4])
    price = pd.Series([10, 5, 2])

    revenue = compute_revenue(quantity, price)
    expected = pd.Series([20, 15, 8])

    assert revenue.equals(expected)
    