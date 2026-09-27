# ECB Macro-Financial Data Explorer

A small data pipeline that fetches, cleans, aggregates and visualizes public
macroeconomic and monetary data directly from the ECB Data Portal's SDMX
2.1 REST API, no API key required.

## What it does

```
fetch.py  →  clean.py  →  aggregate.py  →  visualize.py
(SDMX API)  ()  (monthly join)   (charts + dashboard)
```

1. **Fetch** — pulls each series from `data-api.ecb.europa.eu` as SDMX-CSV.
2. **Clean** — parses SDMX time periods (daily/monthly/quarterly), drops
   duplicate observations (common after data revisions), drops missing
   values
3. **Aggregate** — resamples the daily interest-rate series to monthly
   frequency and joins all series into one wide table for comparison.
4. **Visualize** — combined 3-panel dashboard.


## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Run the pipeline

```bash
python main.py 
```

This writes:
- `data/*_raw.csv`, `data/*_clean.csv` — raw and cleaned series
- `outputs/dashboard.png` — combined 3-panel view


## Notes on the ECB API

- Base pattern: `https://data-api.ecb.europa.eu/service/data/{flowRef}/{key}?format=csvdata`
- No authentication needed.
- Series keys were found by browsing the [ECB Data Portal](https://data.ecb.europa.eu),
  applying filters (frequency, reference area, adjustment, etc.), and copying
  the resulting "Series key" — the same workflow anyone would use to explore
  a new dataflow.
- If the ECB restructures a dataflow, `main.py`'s `dic` dict is the
  single place to update.

## Possible extensions

- Print a correlation matrix between inflation, the current account
and the policy rates over the fetched period.
- Add more series per domain (e.g. HICP sub-components, bilateral BOP flows,
  M3 monetary aggregates) using the same pattern.
- Swap the daily→monthly `first` resampling for `mean` or `last` to better reflect
  daily change or policy rate in effect at month-end

