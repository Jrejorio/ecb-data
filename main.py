from src import agregate, clean, fetch, visualize
import pandas as pd

START_DATE = "2004-10"
END_DATE = "2019-10"

dic = {'HICP' : ['ICP', 'M.U2.N.000000.4.ANR'],
        'BOP' : ['BP6', 'M.Y.I8.W1.S1.S1.T.B.CA._Z._Z._Z.EUR._T._X.N'],
        'DFR' : ['FM', 'D.U2.EUR.4F.KR.DFR.LEV'],
        'MRR' : ['FM', 'D.U2.EUR.4F.KR.MRR_FR.LEV'],
        'MLFR' : ['FM', 'D.U2.EUR.4F.KR.MLFR.LEV']
}

DFS = []

for value in dic.values():
    flow, key = value[0], value[1]
    url = fetch.build_url(flow, key, START_DATE, END_DATE)
    df = fetch.fetch_series(url)
    df_obs = fetch.extract_observations(df)
    df_clean = clean.clean_series(df_obs)
    DFS.append(df_clean)

df_combined = agregate.combine_series(DFS)

visualize.plot(df_combined)