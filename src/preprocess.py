"""
Preprocessing utilities for groundwater level data analysis.
"""

import pandas as pd
import numpy as np


def load_dataset(file_path: str) -> pd.DataFrame:
    """Load raw dataset from CSV or Excel file."""
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith(('.xls', '.xlsx')):
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean dataset by handling missing values and duplicates."""
    df_clean = df.drop_duplicates().copy()
    # Fill or drop missing values according to preprocessing rules
    df_clean = df_clean.ffill().bfill()
    return df_clean


if __name__ == "__main__":
    print("Preprocessing module initialized.")
