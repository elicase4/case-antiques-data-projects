import gspread
import pandas

from pathlib import Path
from google.oauth2.service_account import Credentials


def load_google_sheet(sheet_id: str, worksheet_name: str = None) -> pandas.DataFrame:
    """
    Loads data from a specified Google Sheet into a pandas DataFrame.

    This function uses a service account to authenticate with the Google Sheets API
    and retrieve data from a specified sheet. The sheet must be shared with the
    service account email in advance. All records in the selected worksheet are returned
    as rows in a DataFrame.

    Args:
        sheet_id (str): The id of the Google Spreadsheet (identifiable by the Google Sheet url).
        worksheet_name (str, optional): The name of the worksheet/tab within the sheet.
            If None, the first worksheet (`sheet1`) will be used.

    Returns:
        pd.DataFrame: A DataFrame containing the data from the worksheet, with headers
        inferred from the first row.

    Raises:
        gspread.SpreadsheetNotFound: If the specified spreadsheet does not exist or
            is not shared with the service account.
        gspread.WorksheetNotFound: If the specified worksheet name does not exist in
            the spreadsheet.
        google.auth.exceptions.GoogleAuthError: If authentication with the service
            account fails.
    """

    credentials_path = Path(__file__).resolve(
    ).parents[1] / "auth" / "case-antiques-ml-projects-sheets-reader-credentials.json"

    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets.readonly",
        "https://www.googleapis.com/auth/drive.readonly"
    ]

    creds = Credentials.from_service_account_file(
        credentials_path, scopes=SCOPES)

    google_creds = gspread.authorize(creds)
    sheet = google_creds.open_by_key(sheet_id)
    worksheet = sheet.sheet1 if worksheet_name is None else sheet.worksheet(
        worksheet_name)
    data = worksheet.get_all_records()
    df = pandas.DataFrame(data)

    return df
