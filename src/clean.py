import pandas as pd

def parse_period(date: str) -> pd.Timestamp:
    return pd.Timestamp (date)


def clean_series(df : pd.DataFrame) -> pd.DataFrame:
    df = df.dropna()
    df["TIME_PERIOD"] = df["TIME_PERIOD"].apply(parse_period)
    df = df.drop_duplicates(subset='TIME_PERIOD', keep='last')
    csv = df.to_csv(f"data/{df.columns[1]}_clean.csv")
    return df

