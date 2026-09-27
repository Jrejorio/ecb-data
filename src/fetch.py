import requests
import pandas as pd
import io

BASE_URL = "https://data-api.ecb.europa.eu/service/data/"

def build_url(flow: str, key : str,  start_date: str | None = None, end_date: str | None = None) -> str:
    url = BASE_URL + f"{flow}/{key}?format=csvdata"
    if end_date:
        url += f"&endPeriod={end_date}"
    if start_date:
        url += f"&startPeriod={start_date}"
    return url

def fetch_series(url :str) -> pd.DataFrame:
    response = requests.get(url)
    csv = response.text
    df = pd.read_csv(io.StringIO(csv))
    return df

def extract_observations(df : pd.DataFrame) -> pd.DataFrame:
    title = df['TITLE'][0]
    if df['KEY'][0] == "ICP.M.U2.N.000000.4.ANR":
        df = df[['TIME_PERIOD', 'OBS_VALUE']]
        df = df.rename(columns={'OBS_VALUE':'HICP'})
        csv = df.to_csv("data/HICP_raw.csv")
    elif df['KEY'][0] == "BP6.M.Y.I8.W1.S1.S1.T.B.CA._Z._Z._Z.EUR._T._X.N":
        df = df[['TIME_PERIOD', 'OBS_VALUE']]
        df = df.rename(columns={'OBS_VALUE':'BOP'})
        csv = df.to_csv("data/BOP_raw.csv")
    elif df['KEY'][0] == "FM.D.U2.EUR.4F.KR.DFR.LEV":
        df = df[['TIME_PERIOD', 'OBS_VALUE']]
        df = df.rename(columns={'OBS_VALUE':'DFR'})
        csv = df.to_csv("data/DFR_raw.csv")
    elif df['KEY'][0] == "FM.D.U2.EUR.4F.KR.MRR_FR.LEV":
        df = df[['TIME_PERIOD', 'OBS_VALUE']]
        df = df.rename(columns={'OBS_VALUE':'MRR'})
        csv = df.to_csv("data/MRR_raw.csv")
    elif df['KEY'][0] == "FM.D.U2.EUR.4F.KR.MLFR.LEV":
        df = df[['TIME_PERIOD', 'OBS_VALUE']]
        df = df.rename(columns={'OBS_VALUE':'MLFR'})
        csv = df.to_csv("data/MLFR_raw.csv")
    return df

