import pandas as pd
from gspread_pandas import Spread, conf

def load_google_sheet(sheet_name, worksheet_name=None, credentials_path="google_credentials.json"):
    spread = Spread(sheet_name, config=conf.get_config(conf_dir='.', file_name=credentials_path))
    df = spread.sheet_to_df(index=None, sheet=worksheet_name)
    return df
