from datetime import date, timedelta
from pybaseball import statcast

start = date(2025,6,1)
for i in range(7):
    d = start + timedelta(days=1)
    df = statcast(start_dt=d.isoformat(), end_dt=d.isoformat())
    if len(df):
        df.to_parquet(rf"C:\Users\tmvig\OneDrive\Desktop\Work Samples\Databricks\statcast_{d.isoformat()}.parquet", index=False)
        print(d, df.shape)