from __future__ import print_function

from google.oauth2 import service_account
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']
private_key = ''
email = ''
uri = ''


def update_handler(event, context):
    service_info = {
        "private_key": private_key,
        "client_email": email,
        "token_uri": uri,
    }
    credentials = service_account.Credentials.from_service_account_info(service_info, scopes=SCOPES)
    sheets_service = build('sheets', 'v4', credentials=credentials)

    spreadsheet_id = sheet_id
    range_name = 'Sheet1'
    body = {
        'values': [['this', 'is', 'a', 'test']]
    }

    result = sheets_service.spreadsheets().values().append(spreadsheetId=spreadsheet_id,
                                                           range=range_name,
                                                           valueInputOption='RAW',
                                                           body=body).execute()
