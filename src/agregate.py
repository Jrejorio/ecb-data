import pandas as pd

def combine_series(dfs: list[pd.DataFrame]) -> pd.DataFrame:
    n = len(dfs)
    df = pd.merge(dfs[0], dfs[1], how='inner', on='TIME_PERIOD')
    if n > 2 :
        for i in range(2, n):
            df = pd.merge(df, dfs[i], how='inner', on='TIME_PERIOD')
    return df