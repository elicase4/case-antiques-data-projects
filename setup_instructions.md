# Setup Instructions

## Environment Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Google Sheets Integration

1. Create a Google Cloud project and enable the Google Sheets and Drive APIs.
2. Create a Service Account and download the JSON key file.
3. Save the file as `google_credentials.json` in the project root.
4. Share the necessary Google Sheets with your service account email.

Use the `load_google_sheet()` function in `src/data_loader.py` to access your data.

```python
from src.data_loader import load_google_sheet

df = load_google_sheet("Sheet Name", "Worksheet Name")
```
